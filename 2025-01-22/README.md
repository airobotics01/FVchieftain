# 2025-01-22
## Isaac Sim
로보틱스 연구 및 개발을 위한 물리 기반 시뮬레이션 플랫폼으로, NVIDIA Omniverse 생태계의 일부.
로봇 시스템을 가상 환경에서 시뮬레이션하여 자율 로봇의 개발, 테스트, 검증을 가능하게 하며, 물리적으로 정확한 환경을 제공하여 현실적인 시뮬레이션을 수행.

###  Isaac Sim 주요 기능
1. 물리 기반 시뮬레이션

    PhysX 물리 엔진을 기반으로 충돌, 중력, 마찰 등의 물리 법칙을 현실적으로 구현.
    로봇의 운동학 및 동역학 시뮬레이션을 지원하여 정밀한 테스트 가능.
    복잡한 환경에서도 로봇의 행동을 정확하게 평가 가능.

2. AI 및 머신러닝 통합

    딥 러닝 및 강화 학습을 위한 NVIDIA AI 프레임워크와 통합.
    강화 학습(RL), SLAM(동시 위치 추정 및 지도 작성), 컴퓨터 비전과 같은 기술을 시뮬레이션 환경에서 테스트 가능.
    Omniverse Replicator를 이용한 대량의 합성 데이터 생성 지원.

3. 디지털 트윈 (Digital Twin)

    실제 로봇 및 환경을 그대로 가상 세계에 복제하여 테스트 및 최적화 가능.
    산업 자동화 및 스마트 공장 구현을 위한 디지털 트윈 솔루션 제공.

4. ROS/ROS 2 호환

    ROS(로봇 운영 체제) 및 ROS 2와의 완벽한 통합 지원.
    ROS 노드를 실행하고 Gazebo와 같은 기존 시뮬레이터에서의 마이그레이션 가능.
    ROS 기반의 센서 시뮬레이션(카메라, LiDAR, IMU) 및 로봇 동작 테스트 가능.

5. GPU 가속 및 RTX 렌더링

    NVIDIA의 RTX GPU를 활용한 실시간 레이트레이싱(ray tracing) 및 경로 추적(path tracing) 렌더링 제공.
    물리적으로 정확한 조명 및 반사 효과를 적용하여 고품질 시뮬레이션 환경 구축.

6. 다양한 센서 시뮬레이션 지원

    3D 카메라, LiDAR, IMU 등의 가상 센서를 통해 로봇의 감지 및 탐지 기능을 테스트.
    로봇 비전 및 자율 내비게이션 개발을 위한 정밀한 센서 모델 제공.

7. 클라우드 및 원격 시뮬레이션

    로컬 환경뿐만 아니라 클라우드 기반에서도 시뮬레이션을 실행하여 대규모 병렬 작업 가능.
    원격 로봇 시스템 테스트 및 배포 시 유용.
---
## NVIDIA Omniverse
실시간 3D 시뮬레이션 및 협업을 위한 플랫폼 및 생태계로, 다양한 산업(건축, 제조, 게임, 미디어 및 엔터테인먼트 등)에서 활용할 수 있도록 설계됨. 
AI, 물리 기반 시뮬레이션, 실시간 렌더링 등을 지원하여 복잡한 3D 워크플로우를 통합하고 협업할 수 있음.

### NVIDIA Omniverse 구성 요소
+ Omniverse Nucleus : 협업을 위한 데이터 저장 및 관리 서버.
    다양한 소프트웨어(Blender, Maya, Unreal Engine 등)와의 연결 지원.
    여러 사용자가 실시간으로 동일한 프로젝트에서 작업할 수 있도록 동기화 제공.

+ Omniverse Kit : 개발자를 위한 프레임워크로, 커스터마이징 가능한 3D 애플리케이션 및 도구 개발 가능.
    Python 및 C++로 확장 가능.

+ Omniverse Connectors : 기존 3D 툴(예: Autodesk Maya, 3ds Max, Unreal Engine, Blender)과 Omniverse를 연결하는 플러그인.
    USD(Universal Scene Description) 포맷을 활용하여 원활한 데이터 교환을 지원.

+ Omniverse Simulation : AI 및 물리 기반 시뮬레이션 엔진(PhysX, Flow, Flex 등) 포함.
    산업 환경에서 디지털 트윈(디지털 복제물) 생성 가능.

+ Omniverse RTX Renderer : NVIDIA의 RTX 기술을 활용한 실시간 물리 기반 렌더링(PBR).
    실시간 레이트레이싱 및 패스 트레이싱을 통한 고품질 시각화 제공.
---
## Nuclues
Omniverse 플랫폼의 데이터 관리 및 협업을 위한 핵심 서비스. 
여러 사용자가 동일한 3D 데이터와 자산(assets)을 실시간으로 공유하고 협업할 수 있도록 설계된 클라우드 기반 및 로컬 서버 솔루션을 제공.

### Nucleus 구성 요소
+ Nucleus Server : 로컬 및 클라우드 환경에서 실행되는 중앙 데이터 저장소.
    데이터를 호스팅하고 여러 사용자가 동시에 액세스할 수 있도록 함.

+ Nucleus Navigator : 파일 브라우저 역할을 하며, 사용자 인터페이스를 통해 Nucleus 서버의 데이터를 쉽게 탐색할 수 있음.
    파일 업로드, 다운로드, 권한 설정 가능.

+ Nucleus Connector : 타사 소프트웨어(Blender, Maya 등)에서 Omniverse Nucleus에 직접 연결하여 데이터를 업로드 및 동기화.

+ Nucleus Cache : 데이터를 빠르게 로드할 수 있도록 캐싱을 제공하여 성능 향상.

+ Nucleus Collaboration : 여러 사용자가 동일한 씬(scene)에서 작업할 때 충돌을 방지하고 변경 사항을 동기화하는 협업 기능.
---
## Isaac Sim 설치
1. NVIDIA Omniverse 다운로드

    런처 파일 Properties-Permissions-Allow executing file as program 체크 후 설치

2. Nucleus 설치

    Add Local Nucleus Service에서 +를 눌러서 Neuclues 설치

3. Isaac Sim 및 Cache 설치

    Exchange에서 Isaac Sim과 Cache 설치

4. Isaac Sima 실행

    Library에서 Launch
---
## Isaac Sim 튜토리얼
+ **기물 생성 및 이동**

    Create에서 기물 생성
    - 기즈모 : 3D 씬에서 객체(로봇, 센서, 환경 요소 등)를 조작(이동, 회전, 크기 조절)하기 위한 시각적 도구
    마우스로 기즈모를 통해 물체 이동 및 변형

    W : 이동 모드

    E : 회전 모드 

    R : 크기 모드

    ESC : 선택 취소

+ **Property**

    우측 하단의 Property 패널

    Transform에서 Translation(위치), Orient(방향), Scale(크기) 조절

