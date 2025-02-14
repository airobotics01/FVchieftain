여러 개의 Jetbot 로봇이 물체를 이동시키고, 로봇 팔이 집어서 옮기는 코드

self._num_of_tasks 의 값을 조절함으로 생성되는 로봇의 개수를 조절할 수 있음.
def setup_scene에서 offset도 같이 변경해서 화면에 로봇이 정면으로 나오게 해야 함.


3,4번 줄에서 PickPlace와 PickPlaceController를 import하는데 이 모듈로 Pick & Place를 함.
그래서 2개의 모듈에 대해서 알아보고 활용할 예정.