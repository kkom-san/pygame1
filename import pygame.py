import pygame
pygame.init()
#화면 크기 설정
screen = pygame.display.set_mode((364,260))

#화면 타이틀 설정
pygame.display.set_caption("environment")

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/SEC/Pictures/background.jpg")

#캐릭터 이미지 불러오기
character = pygame.image.load("C:/Users/SEC/Pictures/character.png")

#이벤트 루프
running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
while running:
    for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
        if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
            running = False 
        
        if event.type == pygame.KEYDOWN: #키보드의 키가 눌러졌을 경우
            if event.key == pygame.K_a: #왼쪽 방향키가 눌렸을 때
                pass
            elif event.key == pygame.K_d: #오른쪽 방향키가 눌렸을 때
                pass
            elif event.key == pygame.K_s: #아래쪽 방향키가 눌렸을 때
                pass
            elif event.key == pygame.K_w: #위쪽 방향키가 눌렸을 때
                pass  
        if event.type == pygame.KEYUP: #방향키를 뗐을 때 캐릭터 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0



    screen.blit(background, (0, 0)) #배경에 이미지 그려주고 위치 지정
    screen.blit(character, (100,100))
    pygame.display.update()
    
    
    
