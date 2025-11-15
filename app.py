import pygame
import sys
import random

# 1. Pygame 초기화
pygame.init()

# --- 화면 설정 ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Shooter Game")

# --- 색상 정의 ---
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# --- 플레이어 클래스 ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])  # 50x50 크기의 사각형
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2  # 중앙 시작
        self.rect.bottom = SCREEN_HEIGHT - 30  # 화면 하단에 위치
        self.speed = 5

    def update(self):
        # 키 입력 처리
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: # 왼쪽 화살표 또는 A키
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: # 오른쪽 화살표 또는 D키
            self.rect.x += self.speed
        
        # 화면 경계 설정
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        # 총알을 생성하고 모든 스프라이트 그룹에 추가
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# --- 총알 클래스 ---
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([5, 15]) # 5x15 크기의 사각형
        self.image.fill(BLUE)
        self.rect = self.image.get_rect
