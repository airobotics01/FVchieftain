# 2025-01-23
## Isaac Sim 튜토리얼
+ **local 및 world 좌표 전환**

    W 여러 번 누름 : Move Global과 Move Local 사이 전환

    E 여러 번 누름 : rotate Global과 rotate Local 사이 전환

    Local 좌표계가 활성화되면 도구 모음 아이콘이 주황색으로 변함
    

+ **시점**

    먼저 물체를 create

    F : (물체 선택)선택한 물체를 중심으로 시점 전환 / (아무것도 선택 X)모두 확대된 시점 전환

    ALT + LMB(마우스 왼쪽) : 물체 주변 선회

    ALT + RMB(마우스 오른쪽) or 마우스 스크롤 : 물체 확대

    MMB(마우스 가운데) : 시점 이동


+ **스테이지 및 속성 패널**

    default_light : 도형을 비추는 빛을 키고 끔


+ **작업 공간 사용자 정의**
    
    사용자 인터페이스에서 패널의 크기 조정, 도킹, 도킹 해체, 추가 및 제거 등이 가능

    Window-Viewport-Viewport2 : 새 뷰포트가 생성

    뷰포트 2의 상단 헤더를 클릭 후 드래그 : 도킹 위젯 활성화

    뷰포트 2의 Perspective 카메라 버튼을 클릭 후 카메라를 Top View로 변경


+ **스테이지 속성 설정**
    
    2022.1 이전의 Isaac Sim은 단위가 cm이지만 지금은 기본값이 m임. 그러나 Omniverse Kit의 기본 단위는 여전히 cm임. 겉보기에 100배 정도 떨어진 USD 단위가 보이면 참고.

    기본 회전 순서는 X, Y 그리고 Z 순으로 회전을 실행하도록 설정됨.


+ **물리 장면 만들기**
    
    create-Physics-Physics Scene

    Broadphase Type : 물리 엔진이 많은 객체를 처리할 때 충돌 탐색을 빠르게 수행하기 위해 설계된 방법
    
    1. SAP (기본 설정, 소규모 시뮬레이션에 적합) 
    2. MBP (수백 개 이상의 물체가 있을 때 권장) 
    3. GPU MBP (GPU 가속을 활용하여 대규모 시뮬레이션 최적화)


+ **접지면 추가**

    create-Physics-Ground Plane : 접지면 추가

    Perspective-Show By Purpose-Render : 기본 그리드 설정


+ **조명**

    create-Light-Sphere Light

    Property 창에서 radius, shaping, color, Intensity 등 조절