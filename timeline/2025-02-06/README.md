# 2025-02-04
Isaac Sim 공식 홈페이지 튜토리얼 진행

## Hello World
1. Isaac Sim을 실행 후 Window-Examples-Robotics Examples를 해서 하단 바에 Robotics Examples 생성
2. General-Hello World를 클릭 후 Open Source Code를 눌러 VScode 실행
3. 코트를 수정 후 Ctrl + S로 저장하고 Isaac Sim에서 Load를 눌러 실행
앞으로 별다른 말이 없으면 첨부된 파이썬 코드는 hello_world_py에 입력 

## Singleton_World.py
HelloWorld_basic과 동일한데 코드의 유지보수가 어렵고 상대적으로 덜 안전하다.

## HelloWorld_basic.py
기본 코드로 시뮬레이션 환경을 가져오고, 기본 바닥을 추가.

## Adding_Scene.py
큐브를 한 개 추가하고 위치, 크기, 색을 설정할 수 있음.

## Inspecting_Object.py
기본 바닥과 하나의 큐브를 추가하고, 큐브의 위치, 방향 속도를 터미널에 출력.

## Continuous_Inspecting.py
Inspecting_Object와 거의 동일한데, 매 시뮬레이션 스텝마다 위치, 방향, 속도를 출력

## Launch_Python.py
Continuous_Inspecting과 유사한데, 500번의 스텝을 진행하고 Isaac Sim을 실행하고 있지 않아도 터미널에 다음 코드를 입력함으로 실행
./python.sh ./exts/isaacsim.examples.interactive/isaacsim/examples/interactive/user_examples/my_application.py

---
설치 및 실행에 대한 문제가 발생하지 않아서 튜토리얼을 진행하면서 공부해나갈 예정