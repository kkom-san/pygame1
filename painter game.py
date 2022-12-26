import pygame
import random
import time


pygame.init() #초기화

#화면 크기 설정
screen_width = 800 # 가로 크기
screen_height = 450 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame. display.set_caption("painter game")
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("./화이트보드.jpg")

#캐릭터 불러오기
character = pygame.image.load("./내얼굴.png")
character_size = character.get_rect().size #캐릭터 이미지 사이즈 구하기
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
#캐릭터의 기준 좌표를 캐릭터의 왼쪽 상단으로 둔다.
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로 절반의 중간에 위치. 좌우로 움직이기
character_y_pos = screen_height - character_height #이미지가 화면 세로의 가장 아래 위치

#적캐릭터 불러오기
monster = pygame.image.load("./KakaoTalk_20221120_181613036.jpg")
monster_size = monster.get_rect().size
monster_width = monster_size[0]
monster_height = monster_size[1]
#적캐릭터의 기준 좌표를 x=random y=0 으로 둔다.
monster_x_pos = random.randint(0, screen_width - monster_width)
monster_y_pos = 0
monster_speed = 30

# #아이템 불러오기
# item = pygame.image.load("C:/Users/SEC/Pictures/신속신.jpg")
# item_size = item.get_rect().size
# item_width = item_size[0]
# item_height = item_size[1]
# #아이템의 기준 좌표를 x=random y=0 으로 둔다.
# item_x_pos = random.randint(0, 10000)
# item_y_pos = 0
# item_speed = 10


start_ticks = pygame.time.get_ticks()

#캐릭터 이동 좌표
to_x = 0
to_y = 0

#캐릭터 이동 속도 변수
character_speed = 0.5

# item_time1 = 55000
# item_time2 = 50000

total_time = 60000 #제한시간

life = 10

game_font = pygame.font.Font(None,40)
#이벤트 루프
num = 0
running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
while running:
    dt = clock.tick(15) #초당 프레임 수 fps 설정
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
    
    #적캐릭터 떨어지기 설정
    monster_y_pos += monster_speed
    monster_speed+=0.05

    if monster_y_pos > screen_height:
        monster_y_pos = 0
        monster_x_pos = random.randint(0, screen_width - monster_width)
        num +=1
    
    # if num >= 20:
    #     screen.blit(item, (item_x_pos, item_y_pos))
    #     item_y_pos += item_speed
    #     if item_y_pos > screen_height:
    #         time.sleep(10)
    #         item_y_pos = 0
    #         item_x_pos = random.randint(0, screen_width - monster_width)

    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    monster_rect = monster.get_rect()
    monster_rect.left = monster_x_pos
    monster_rect.top = monster_y_pos
    
    if character_rect.colliderect(monster_rect):
        life -= 1
        if life == 0:
            running = False
        
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
    screen.blit(monster, (monster_x_pos, monster_y_pos))
    
    elapsed_time = (pygame.time.get_ticks() - start_ticks/1000)
    
    if (elapsed_time < 20000) & (elapsed_time >= 10000):
        distrupt_box = pygame.draw.rect(screen, color=(255,255,255), rect=[0, 0, 800, 300])
    
    guage_message = game_font.render(str(life), True, (255, 0, 0))
    
    screen.blit(guage_message,(10,50))
    
    life_gauge = pygame.draw.rect(screen, color=(255,0, 0), rect=[50, 50, life*10, 30])
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True,
                            (255, 0, 0))
    screen.blit(timer,(10,10))
        
    
    if total_time - elapsed_time <= 0:
        print("you win!")
        running = False
    
    
    pygame.display.update()


#pygame 종료
pygame.quit()
