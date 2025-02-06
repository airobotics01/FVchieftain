# 2025-01-24
rdp로 서버용 컴퓨터에서 isaac sim 새로 설치 후 실행

## Isaac Sim 인터페이스

### Physics scenes 관련 속성
1. Gravity Direction (X, Y, Z) : 중력 방향을 설정하는 옵션. X, Y, Z 축 값으로 중력이 작용하는 방향을 지정.

2. Gravity Magnitude : 중력 크기를 설정.

3. Collision System : 충돌 시스템을 설정하는 옵션. 
    + PCM (Persistent Contact Manifold): 충돌 감지에서 더 안정적인 결과를 제공하며 성능을 최적화.

    + Legacy: 이전 버전 충돌 시스템, 호환성을 위해 사용.

4. Solver Type : 물리 계산의 솔버 유형을 선택.

    + TGS (Temporal Gauss-Seidel): 더 높은 안정성과 정확성을 제공하는 솔버.

    + PGS (Projected Gauss-Seidel): 비교적 성능이 우수하지만 정확도가 떨어질 수 있음.

5. Broadphase Type : 충돌 감지 시 Broadphase 알고리즘을 선택. 충돌 가능성이 높은 객체들을 미리 필터링하는 단계.

6. Enable CCD 
    + CCD (Continuous Collision Detection): 빠르게 움직이는 객체가 다른 객체를 통과하지 않도록 충돌을 더 정확히 계산. 활성화하면 물리 시뮬레이션의 정확도가 높아지지만 성능이 저하될 수 있음.

7. Enable GPU Dynamics : GPU를 활용하여 물리 시뮬레이션을 가속화. 활성화 시 GPU에서 동역학 연산을 처리해 CPU 부담을 줄이고 성능을 향상.

8. Inverted Collision Group Filter : 충돌 그룹 필터를 반전. 특정 그룹 간의 충돌을 방지하거나 허용할 때 사용.

9. Maximum Position Iteration Count : 물리 엔진에서 위치 해결을 위한 최대 반복 횟수를 설정. 값이 높을수록 더 정확하지만 성능에 영향.

10. Maximum Velocity Iteration Count : 물리 엔진에서 속도 해결을 위한 최대 반복 횟수를 설정.  값이 높으면 물리 시뮬레이션의 정확도가 향상되지만 성능이 저하될 수 있음.

11. Minimum Position Iteration Count : 위치 계산을 위한 최소 반복 횟수를 지정. 낮은 값은 빠른 계산을 가능하게 하지만 정확성이 떨어질 수 있음.

12. Minimum Velocity Iteration Count : 속도 계산을 위한 최소 반복 횟수를 설정.  성능과 정확성 간의 균형을 맞추는 데 사용.

13. Report Kinematic vs Kinematic Pairs : 키네마틱 객체 간의 충돌을 보고할지 여부를 설정. 키네마틱 객체는 물리적 시뮬레이션에 영향을 받지 않고 수동으로 이동하는 객체.

14. Report Kinematic vs Static Pairs : 키네마틱 객체와 정적인 객체 간의 충돌을 보고할지 여부를 설정. 정적인 객체는 움직이지 않는 물체를 의미.

15. Time Steps Per Second : 물리 시뮬레이션의 시간 스텝(프레임) 비율을 설정. 값이 높을수록 시뮬레이션이 더 정확하지만 성능에 영향.

16. Advanced : 고급 설정을 확장하여 더 세부적인 물리 시뮬레이션 옵션을 설정.

---
### physics 관련 용어
1. Rigid Body Enabled : 강체 물리 시뮬레이션을 활성화할지 여부를 설정. 체크되어 있으면 해당 객체가 물리 엔진에서 강체로 동작.

2. Kinematic Enabled : 객체를 키네마틱 객체로 설정. 키네마틱 객체는 물리 시뮬레이션의 영향을 받지 않고, 프로그래밍이나 애니메이션으로 직접 이동.

3. Simulation Owner : 물리 시뮬레이션의 소유자를 설정하는 옵션. 주로 여러 객체 간 관계를 정의하거나 특정 컨텍스트에서 시뮬레이션을 관리할 때 사용.

4. Starts as Asleep : 시뮬레이션 시작 시 객체가 수면 상태(Sleep)인지 여부를 설정. 수면 상태에서는 물리 연산이 일시적으로 비활성화되어 성능 최적화를 도움.

5. Velocities in Local Space ; 속도를 로컬 좌표계를 기준으로 적용할지 여부를 설정. 활성화되면 객체의 속도가 객체의 회전에 따라 로컬 방향으로 적용.

6. Linear Velocity (X, Y, Z) : 객체의 선형 속도를 설정. X, Y, Z 축 각각의 속도를 지정하여 움직이는 방향과 크기를 정의.

7. Angular Velocity (X, Y, Z) : 객체의 각속도를 설정. X, Y, Z 축을 기준으로 회전 속도를 지정.

8. Linear Damping : 객체의 선형 속도에 적용되는 감쇠 계수. 값이 높을수록 객체가 더 빨리 멈춤.

9. Angular Damping : 객체의 각속도에 적용되는 감쇠 계수. 값이 높을수록 회전이 더 빨리 멈춤.

10. Max Linear Velocity : 객체가 가질 수 있는 최대 선형 속도를 제한. 값이 inf일 경우 속도 제한이 없음. 

11. Max Angular Velocity : 객체가 가질 수 있는 최대 각속도를 제한. 값이 inf일 경우 각속도 제한이 없음.

12. Sleep Threshold : 객체가 멈춘 상태로 간주되는 기준값. 값이 낮으면 객체가 더 쉽게 멈추고 수면 상태로 전환.

13. Enable CCD : CCD (Continuous Collision Detection)를 활성화. 빠르게 움직이는 객체의 충돌을 더 정확히 계산하여 객체가 다른 객체를 통과하지 않도록 함.

14. Disable Gravity : 중력을 비활성화. 체크하면 해당 객체는 중력의 영향을 받지 않음.

15. Locked Pos Axis (X, Y, Z) : 객체의 위치 이동을 특정 축에서 잠금.

16. Locked Rot Axis (X, Y, Z) : 객체의 회전을 특정 축에서 잠금. 
---
이후 ROS2를 연결해보려 했으나 서버컴퓨터에 ROS 설치 중 문제가 생겨 중단