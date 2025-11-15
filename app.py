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

# 총알 클래스
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([5, 15])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# 적 클래스
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width) # 무작위 X 위치
        self.rect.y = random.randrange(-100, -40) # 화면 위쪽에서 시작
        self.speedy = random.randrange(1, 4) # 무작위 하강 속도

    def update(self):
        self.rect.y += self.speedy
        # 적이 화면 아래로 나가면 다시 위로 이동
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 4)

def spawn_new_enemy():
    """새로운 적을 생성하여 게임에 추가합니다."""
    e = Enemy()
    all_sprites.add(e)
    enemies.add(e)

def draw_score(surf, text, x, y):
    """점수를 화면에 그립니다."""
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# --- 게임 초기화 및 스프라이트 그룹 생성 ---
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

score = 0

# 적 5마리 초기 생성
for i in range(5):
    spawn_new_enemy()

# --- 메인 게임 루프 ---
running = True
while running:
    # 60 FPS 설정
    clock.tick(60)

    # 1. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 스페이스바 누르면 총알 발사
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # 2. 게임 상태 업데이트
    all_sprites.update()
    
    # 3. 충돌 처리
    
    # 총알과 적의 충돌 (hits는 충돌한 총알과 적의 딕셔너리)
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True) 
    
    # 충돌이 발생하면
    for hit in hits:
        score += 10 # 점수 10점 추가
        spawn_new_enemy() # 새로운 적 생성
        
    # 플레이어와 적의 충돌
    hits = pygame.sprite.spritecollide(player, enemies, True) # True: 충돌 시 적 삭제
    if hits:
        # 💥 게임 오버 처리
        running = False
        st.error(f"게임 오버! 최종 점수: {score}")

    # 4. 화면 그리기
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_score(screen, f'Score: {score}', SCREEN_WIDTH // 2, 10) # 점수 표시

    # 5. 화면 업데이트 (실제 화면에 표시)
    pygame.display.flip()

# 6. Pygame 종료
pygame.quit()
sys.exit()
