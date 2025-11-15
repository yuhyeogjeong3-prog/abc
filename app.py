import pygame
import sys
import random

# 1. Pygame 초기화
pygame.init()

# --- 화면 및 게임 설정 ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter Game with Enemies")
clock = pygame.time.Clock() # FPS 관리를 위한 클록

# --- 색상 정의 ---
WHITE = (255, 255, 255)
RED = (255, 0, 0) # 플레이어 색상
BLUE = (0, 0, 255) # 총알 색상
GREEN = (0, 255, 0) # 적 색상
BLACK = (0, 0, 0)

# --- 글꼴 설정 (점수 표시용) ---
font = pygame.font.Font(None, 36) # 기본 글꼴, 크기 36

# --- 스프라이트 클래스 ---

# 플레이어 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 30
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        
        # 화면 경계 설정
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# 총
