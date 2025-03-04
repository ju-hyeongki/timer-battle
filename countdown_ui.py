import pygame

# Pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Logo Display")

# 이미지 불러오기 및 크기 조절
logo = pygame.image.load("nextg_logo.png")
logo = pygame.transform.scale(logo, (200, 100))  # 크기 조절 (원하는 크기로 수정 가능)

# 이미지 위치 설정 (정가운데)
logo_rect = logo.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# 게임 루프
running = True
while running:
    screen.fill((0, 0, 0))  # 배경을 검은색으로 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 이미지 그리기
    screen.blit(logo, logo_rect)

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()
