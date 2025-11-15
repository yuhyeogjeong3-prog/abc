import pygame
import sys

# 1. Pygame 초기화
pygame.init()

# --- 화면 설정 ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Drawing Pad")

# --- 색상 및 설정 ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DRAW_COLOR = BLACK       # 기본 그리기 색상
DRAW_SIZE = 5            # 브러시 두께
current_pos = None       # 현재 마우스 위치
is_drawing = False       # 그리는 중인지 확인

# --- 초기 화면 ---
screen.fill(WHITE)

# --- 메인 게임 루프 설정 ---
clock = pygame.time.Clock()
running = True

# --- 메인 루프 ---
while running:
    # 60 FPS 설정
    clock.tick(60)

    # 1. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # --- 마우스 버튼 처리 ---
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 왼쪽 마우스 버튼 (그리기 시작)
                is_drawing = True
                current_pos = event.pos
            elif event.button == 3: # 오른쪽 마우스 버튼 (화면 지우기)
                screen.fill(WHITE)
                current_pos = None # 지우고 나면 현재 위치 초기화
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # 왼쪽 마우스 버튼 떼기 (그리기 종료)
                is_drawing = False
                current_pos = None
                
        elif event.type == pygame.MOUSEMOTION:
            # 2. 마우스 이동 및 선 그리기
            if is_drawing:
                # 이전 위치에서 현재 위치까지 선을 그립니다.
                if current_pos:
                    pygame.draw.line(screen, DRAW_COLOR, current_pos, event.pos, DRAW_SIZE)
                
                # 현재 위치를 다음 선을 위한 이전 위치로 업데이트
                current_pos = event.pos

        # --- 키보드 이벤트 처리 (색상 변경 등) ---
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K
