# # 이 파일에 게임 스크립트를 입력합니다.

# # image 문을 사용해 이미지를 정의합니다.
# # image eileen happy = "eileen_happy.png"

# # 게임에서 사용할 캐릭터를 정의합니다.
# define e = Character('아이린', color="#c8ffc8")


# # 여기에서부터 게임이 시작합니다.
# label start:

#     e "새로운 렌파이 게임을 만들었군요."

#     e "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

#     return

init:
    define principal = ("교장")
    define student1 = ("학생1")
    define student2 = ("학생2")
    define student3 = ("학생3")
    define student4 = ("학생4")
    define guide = ("지도 선생님")
    define game = ("game")
    define game = ("game")
    image school entrance = "school_entrance.jpg"
    image school classroom = "school_classroom.jpg"
    image school garden = "school_garden.jpg"
    image school green potion = "school_green_potion.jpg"
    image school potion = "school_potion.jpg"
    image school blue potion = "school_blue_potion.jpg"
    image teacher principal = "principal.png"
    image teacher guide = "guide_teacher.png"
    image character one = "character1.png"
    image character two = "character2.png"
    image students = "students.png"

# script.rpy

# 게임 시작 화면
label start:
    play music "bg-start.mp3" loop
    scene school entrance with dissolve
    pause 2.0
    # play music "bg-start.mp3" fadeout(2.0)
    show teacher principal
    play sound ["0.mp3", "<silence .3>", "1.mp3"]
    principal "환영합니다, 새로운 학생 여러분! 스톤브릿지 마법학교에 오신 걸 진심으로 환영합니다."
    hide teacher
    show character one
    play sound ["2.mp3", "<silence .3>", "3.mp3"]
    student1 "와, 정말 멋지시네요! 이곳이 바로 스톤브릿지 마법학교인가요?"
    hide character one
    show character two
    play sound ["4.mp3", "<silence .3>", "5.mp3"]
    student2 "좋아! 이곳에서 우리도 놀라운 마법을 배울 수 있을 거야."
    hide character
    show teacher guide
    play sound ["6.mp3", "<silence .3>", "7.mp3"]
    guide "맞아요, 이곳은 마법의 세계를 탐험하고 놀라운 능력을 발전시킬 수 있는 곳이에요. 여러분은 놀라운 여정을 시작하게 될 거예요."
    stop music fadeout 2.0
    jump scene_exploration

# 학교 탐험 화면
label scene_exploration:
    play music "bg-classroom.mp3" loop
    scene school classroom
    pause 2.0
    show students
    play sound ["8.mp3", "<silence .3>", "9.mp3"]
    student3 "여기 강의실도 너무 신기하고, 저기 연구실도 봐! 정말 대단한 곳이네요."
    play sound "10.mp3"
    student4 "지도 선생님이 말한 대로, 우리에게 많은 것을 가르쳐줄 것 같아요."
    menu:
        "어떤 마법 물약을 먼저 배워볼까요?":
            jump potion_lesson
        "정원에서 캐릭터들을 만나러 가볼까요?":
            jump garden_encounter
# =======================

# 마법 물약 수업 화면
label potion_lesson:
    # 배경 설정
    scene school potion
    pause 2.0

    # 마법 물약 수업 대사
    show teacher guide# serious
    play sound ["11.mp3", "<silence .3>", "12.mp3"]
    guide "안녕하세요! 오늘은 마법 물약 수업을 시작하겠습니다."

    # 플레이어 선택 대사
    menu:
        "초록 물약을 만들어봅시다.":
            jump green_potion
            stop music fadeout 2.0
        "파란 물약을 만들어봅시다.":
            jump blue_potion
            stop music fadeout 2.0

# 마법 물약 수업 - 초록 물약 화면
label green_potion:
    # 배경 설정
    play music "bg-potion1.mp3" loop
    scene school green potion
    pause 2.0

    # 빨간 물약 만들기 대사
    show teacher guide# excited
    play sound ["13.mp3", "<silence .3>", "14.mp3"]
    guide "잘했어요! 이제 초록 물약을 완성했어요."

    # 결과 대사
    "당신은 성공적으로 초록 물약을 만들어 냈습니다."

    # 플레이어 선택 대사
    menu:
        "다음 수업으로 넘어갑시다.":
            jump garden_encounter
            stop music fadeout 2.0

# 마법 물약 수업 - 파란 물약 화면
label blue_potion:
    # 배경 설정
    play music "bg-potion2.mp3" loop
    scene school blue potion
    pause 2.0

    # 파란 물약 만들기 대사
    show teacher guide# sad
    play sound ["15.mp3", "<silence .3>", "16.mp3"]
    guide "앗, 조금 실패한 것 같군요. 다음엔 더 잘 할 수 있죠?"

    # 결과 대사
    "당신은 뭔가 잘못된 결과를 얻었습니다. 더 노력해야겠군요."

    # 플레이어 선택 대사
    menu:
        "다음에 다시 도전해봅시다.":
            jump garden_encounter
            stop music fadeout 2.0

# 정원에서 캐릭터들을 만나러 가는 화면
label garden_encounter:
    # 배경 설정
    play music "bg-garden.mp3" loop
    scene school garden
    pause 2.0

    # 정원에서 캐릭터들을 만나는 대사
    show character one
    play sound ["17.mp3", "<silence .3>", "18.mp3"]
    student1 "안녕하세요! 저는 학생1이에요."
    hide chracter
    show character two
    play sound ["19.mp3", "<silence .3>", "20.mp3"]
    student2 "반가워요! 저는 학생2라고 해요."

    # 플레이어 선택 대사
    menu:
        "각 캐릭터들과 대화를 나눠보세요.":
            jump conversation_character1
        "정원의 다른 장소들을 둘러보겠어요.":
            jump explore_garden

# 캐릭터1과의 대화 화면
label conversation_character1:
    # 배경 설정
    scene school garden

    # 캐릭터1과의 대화 대사
    show character one
    play sound "21.mp3"
    student1 "오랜만에 정원에서 산책하는 건 기분이 좋네요."

    # 플레이어 선택 대사
    menu:
        "다른 캐릭터들과도 이야기를 나눠볼까요?":
            jump garden_encounter
        "정원을 더 둘러볼까요?":
            jump explore_garden

# 정원 탐험 화면
label explore_garden:
    # 배경 설정
    scene school garden

    # 정원 탐험 대사
    show students# normal
    student1 "정원"
