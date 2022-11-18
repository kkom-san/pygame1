import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 800 # 가로 크기
screen_height = 450 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame. display.set_caption("painter game")

#FPS 설정
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/SEC/Pictures/화이트보드.jpg")

#캐릭터 불러오기
character = pygame.image.load("C:/Users/SEC/Pictures/내얼굴.png")
character_size = character.get_rect().size #캐릭터 이미지 사이즈 구하기
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
#캐릭터의 기준 좌표를 캐릭터의 왼쪽 상단으로 둔다.
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로 절반의 중간에 위치. 좌우로 움직이기
character_y_pos = screen_height - character_height #이미지가 화면 세로의 가장 아래 위치

#캐릭터 이동 좌표
to_x = 0
to_y = 0

#캐릭터 이동 속도 변수
character_speed = 0.5

#이벤트 루프
running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
while running:
    dt = clock.tick(10) #초당 프레임 수 fps 설정
    for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
        if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
            running = False

        if event.type == pygame.KEYDOWN: #키보드의 키가 눌러졌을 경우
            if event.key == pygame.K_a: #왼쪽 방향키가 눌렸을 때
                to_x -= character_speed
            elif event.key == pygame.K_d: #오른쪽 방향키가 눌렸을 때
                to_x += character_speed
            elif event.key == pygame.K_s: #아래쪽 방향키가 눌렸을 때
                to_y += character_speed
            elif event.key == pygame.K_w: #위쪽 방향키가 눌렸을 때
                to_y -= character_speed

        if event.type == pygame.KEYUP: #방향키를 뗐을 때 캐릭터 멈춤
            if event.key == pygame.K_a or event.key == pygame.K_d:
                to_x = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #왼쪽, 오른쪽 경계 정하기
    if character_x_pos < 50:
        character_x_pos = 50

    elif character_x_pos > 700:
        character_x_pos = 700

    #위, 아래쪽 경계 정하기
    if character_y_pos < 80:
        character_y_pos = 80

    elif character_y_pos > 350:
        character_y_pos = 350

    screen.blit(background, (0, 0)) #배경에 이미지 그려주고 위치 지정
    screen.blit(character, (character_x_pos, character_y_pos)) #배경에 캐릭터 그려주기
    pygame.display.update()


#pygame 종료
pygame.quit()