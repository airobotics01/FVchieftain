from isaacsim.examples.interactive.base_sample import BaseSample
from isaacsim.core.utils.nucleus import get_assets_root_path
from isaacsim.robot.manipulators.examples.franka.tasks import PickPlace
from isaacsim.robot.manipulators.examples.franka.controllers import PickPlaceController
from isaacsim.robot.wheeled_robots.robots import WheeledRobot
from isaacsim.robot.wheeled_robots.controllers.wheel_base_pose_controller import WheelBasePoseController
from isaacsim.robot.wheeled_robots.controllers.differential_controller import DifferentialController
from isaacsim.core.api.tasks import BaseTask
from isaacsim.core.utils.types import ArticulationAction
from isaacsim.core.utils.string import find_unique_string_name
from isaacsim.core.utils.prims import is_prim_path_valid
import numpy as np


class RobotsPlaying(BaseTask): # pick & place + Jetbot 이동
    def __init__(self, name, offset=None):
        super().__init__(name=name, offset=offset)
        self._task_event = 0
        # Randomize the task a bit
        self._jetbot_goal_position = np.array([np.random.uniform(1.2, 1.6), 0.3, 0]) + self._offset # Jetbot 목표 위치 랜덤 설정
        self._pick_place_task = PickPlace(cube_initial_position=np.array([0.1, 0.3, 0.05]),
                                        target_position=np.array([0.7, -0.3, 0.0515 / 2.0]),
                                        offset=offset) # pickplace 객체 생성
        return

    def set_up_scene(self, scene): # 로봇을 환경에 추가
        super().set_up_scene(scene)
        self._pick_place_task.set_up_scene(scene) # pickplace 객체를 시뮬레이션 환경에 추가
        jetbot_name = find_unique_string_name(
            initial_name="fancy_jetbot", is_unique_fn=lambda x: not self.scene.object_exists(x)
        )
        jetbot_prim_path = find_unique_string_name(
            initial_name="/World/Fancy_Jetbot", is_unique_fn=lambda x: not is_prim_path_valid(x)
        )
        assets_root_path = get_assets_root_path()
        jetbot_asset_path = assets_root_path + "/Isaac/Robots/Jetbot/jetbot.usd" # Jetbot 로봇을 USD 파일을 통해 추가
        self._jetbot = scene.add(
            WheeledRobot(
                prim_path=jetbot_prim_path,
                name=jetbot_name,
                wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
                create_robot=True,
                usd_path=jetbot_asset_path,
                position=np.array([0, 0.3, 0]),
            )
        )
        self._task_objects[self._jetbot.name] = self._jetbot
        pick_place_params = self._pick_place_task.get_params()
        self._franka = scene.get_object(pick_place_params["robot_name"]["value"]) # Franka 로봇 가져옴
        current_position, _ = self._franka.get_world_pose()
        self._franka.set_world_pose(position=current_position + np.array([1.0, 0, 0])) # 초기 위치 설정
        self._franka.set_default_state(position=current_position + np.array([1.0, 0, 0]))
        self._move_task_objects_to_their_frame()
        return

    def get_observations(self): # Jetbot의 현재 위치와 방향 반환
        current_jetbot_position, current_jetbot_orientation = self._jetbot.get_world_pose()
        observations= {
            self.name + "_event": self._task_event, #change task event to make it unique
            self._jetbot.name: {
                "position": current_jetbot_position,
                "orientation": current_jetbot_orientation,
                "goal_position": self._jetbot_goal_position
            }
        }
        observations.update(self._pick_place_task.get_observations())
        return observations

    def get_params(self): # 로봇의 설정값(파라미터) 반환
        pick_place_params = self._pick_place_task.get_params()
        params_representation = pick_place_params
        params_representation["jetbot_name"] = {"value": self._jetbot.name, "modifiable": False}
        params_representation["franka_name"] = pick_place_params["robot_name"]
        return params_representation

    def pre_step(self, control_index, simulation_time): # Jetbot이 목표 위치에 도달하면 task_event를 1로 변경하고, 200 step 후 2로 변경하여 pick&place 동작이 시작되도록 설정
        if self._task_event == 0:
            current_jetbot_position, _ = self._jetbot.get_world_pose()
            if np.mean(np.abs(current_jetbot_position[:2] - self._jetbot_goal_position[:2])) < 0.04:
                self._task_event += 1 
                self._cube_arrive_step_index = control_index
        elif self._task_event == 1:
            if control_index - self._cube_arrive_step_index == 200:
                self._task_event += 1
        return

    def post_reset(self): # 시뮬레이션 리셋 후 로봇 상태 초기화
        self._franka.gripper.set_joint_positions(self._franka.gripper.joint_opened_positions)
        self._task_event = 0
        return


class HelloWorld(BaseSample): # 다중 작업 관리 및 물리 시뮬레이션 실행
    def __init__(self) -> None:
        super().__init__()
        # Add lists for tasks,
        self._tasks = []
        self._num_of_tasks = 3 # 이 숫자만큼 매니퓰레이터와 jetbot 생성됨 
        #  Add lists for controllers
        self._franka_controllers = []
        self._jetbot_controllers = []
        # Add lists for variables needed for control
        self._jetbots = []
        self._frankas = []
        self._cube_names = []
        return

    def setup_scene(self): # 여러 개의 RobotPlaying 작업을 추가
        world = self.get_world()
        for i in range(self._num_of_tasks):
            world.add_task(RobotsPlaying(name="my_awesome_task_" + str(i), offset=np.array([0, (i * 2) - 3, 0]))) # offset은 위치 설정. 
        return

    async def setup_post_load(self): # pickplacecontroller를 생성해 pick & place 동작을 수행하도록 설정
        self._world = self.get_world()
        for i in range(self._num_of_tasks):
            self._tasks.append(self._world.get_task(name="my_awesome_task_" + str(i)))
            # Get variables needed for control
            task_params = self._tasks[i].get_params()
            self._frankas.append(self._world.scene.get_object(task_params["franka_name"]["value"]))
            self._jetbots.append(self._world.scene.get_object(task_params["jetbot_name"]["value"]))
            self._cube_names.append(task_params["cube_name"]["value"])
            # Define controllers
            self._franka_controllers.append(PickPlaceController(name="pick_place_controller",
                                                                gripper=self._frankas[i].gripper,
                                                                robot_articulation=self._frankas[i],
                                                                # Change the default events dt of the
                                                                # pick and place controller to slow down some of the transitions
                                                                # to pick up further blocks
                                                                # Note: this is a simple pick and place state machine
                                                                # based on events dt and not event success
                                                                # check the different events description in the api
                                                                # documentation
                                                                events_dt=[0.008, 0.002, 0.5, 0.1, 0.05, 0.05, 0.0025, 1, 0.008, 0.08]))
            self._jetbot_controllers.append(WheelBasePoseController(name="cool_controller",
                                                                    open_loop_wheel_controller=
                                                                      DifferentialController(name="simple_control",
                                                                                             wheel_radius=0.03, wheel_base=0.1125)))
        self._world.add_physics_callback("sim_step", callback_fn=self.physics_step)
        await self._world.play_async()
        return

    async def setup_post_reset(self): # Franka 컨트롤러 및 Jetbot 이동 컨트롤러 초기화
        for i in range(len(self._tasks)):
            # Reset all controllers
            self._franka_controllers[i].reset()
            self._jetbot_controllers[i].reset()
        await self._world.play_async()
        return

    def physics_step(self, step_size): # Jetbot이 목표 위치로 이동하도록 휠 모터에 속도 명령 전달
        current_observations = self._world.get_observations()
        for i in range(len(self._tasks)):
            # Apply actions for each task
            if current_observations[self._tasks[i].name + "_event"] == 0:
                self._jetbots[i].apply_wheel_actions(
                    self._jetbot_controllers[i].forward(
                        start_position=current_observations[self._jetbots[i].name]["position"],
                        start_orientation=current_observations[self._jetbots[i].name]["orientation"],
                        goal_position=current_observations[self._jetbots[i].name]["goal_position"]))
            elif current_observations[self._tasks[i].name + "_event"] == 1: 
                self._jetbots[i].apply_wheel_actions(ArticulationAction(joint_velocities=[-8.0, -8.0]))
            elif current_observations[self._tasks[i].name + "_event"] == 2: # Jetbot이 목표 위치에 도착하면 Pick & Place 동작 수행
                self._jetbots[i].apply_wheel_actions(ArticulationAction(joint_velocities=[0.0, 0.0]))
                actions = self._franka_controllers[i].forward(
                    picking_position=current_observations[self._cube_names[i]]["position"],
                    placing_position=current_observations[self._cube_names[i]]["target_position"],
                    current_joint_positions=current_observations[self._frankas[i].name]["joint_positions"])
                self._frankas[i].apply_action(actions)
        return

    # This function is called after a hot reload or a clear
    # to delete the variables defined in this extension application
    def world_cleanup(self): # 시뮬레이션 종료 또는 초기화 시 메모리 정리
        self._tasks = []
        self._franka_controllers = []
        self._jetbot_controllers = []
        self._jetbots = []
        self._frankas = []
        self._cube_names = []
        return