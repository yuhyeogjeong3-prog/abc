import pygame
import sys
import random
import time

# 1. Pygame 초기화
pygame.init()

# --- 화면 및 게임 설정 ---
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Memory Game")
clock = pygame.time.Clock()
FPS = 30

# --- 색상 정의 ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CARD_COLOR = (100, 100, 255) # 카드 뒷면 색상

# --- 게임 상수 ---
GRID_SIZE = 4
CARD_COUNT = GRID_SIZE * GRID_SIZE
CARD_WIDTH = SCREEN_WIDTH // GRID_SIZE
CARD_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# --- 카드 내용 (색상) ---
# 8쌍의 고유한 색상 생성
UNIQUE_COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
    (0, 255, 255), (255, 0, 255), (255, 165, 0), (128, 0, 128)
]
# 16개의 카드 리스트 (각 색상이 두 번씩)
card_contents = UNIQUE_COLORS * 2 
random.shuffle(card_contents) # 무작위로 섞기

# --- 게임 상태 변수 ---
# 모든 카드가 덮여 있는 상태로 시작 (False: 덮힘, True: 앞면)
matched_cards = [[False] * GRID_SIZE for _ in range(GRID_SIZE)] 
revealed_cards =
