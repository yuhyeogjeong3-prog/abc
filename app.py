import pygame
import sys
import random

# 1. Pygame 초기화
pygame.init()

# --- 화면 및 설정 ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Breakout")
clock = pygame.time.Clock()
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# --- 게임 변수 ---
score = 0
lives = 3
game_over = False

# --- 스프라이트 클래스 ---

# 패들 클래스
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 30
        self.speed = 8

    def update(self):
        # 마우스로 패들 이동
        pos = pygame.mouse.get_pos()
        self.rect.centerx = pos[0]
        
        # 화면 경계 설정
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# 공 클래스
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 10
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = paddle.rect.top - 10 # 패들 위에서 시작
        self.speed_x = 5 * random.choice([-1, 1])
        self.speed_y = -5
        self.is_stuck = True # 처음에는 패들에 붙어 있음

    def update(self):
        if self.is_stuck:
            # 공이 패들에 붙어 있을 때
            self.rect.centerx = paddle.rect.centerx
        else:
            # 굴러가는 공
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            
            # 벽 충돌 (좌우)
            if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
                self.speed_x *= -1
            
            # 벽 충돌 (상단)
            if self.rect.top <= 0:
                self.speed_y *= -1
            
            # 바닥 충돌 (게임 오버 조건)
            if self.rect.bottom >= SCREEN_HEIGHT:
                global lives
                lives -= 1
                self.reset() # 공 위치 초기화
                
    def reset(self):
        """공의 위치와 속도를 초기화합니다."""
        self.rect.centerx = paddle.rect.centerx
        self.rect.bottom = paddle.rect.top - 10
        self.speed_x = 5 * random.choice([-1, 1])
        self.speed_y = -5
        self.is_stuck = True

# 벽돌 클래스
class Brick(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.width = 50
        self.height = 20
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# --- 함수: 벽돌 생성 ---
def setup_bricks():
    """초기 벽돌 배치를 생성합니다."""
    # 벽돌 색상 리스트
    brick_colors = [RED, GREEN, BLUE]
    
    for row in range(5): # 5줄
        color = brick_colors[row % len(brick_colors)]
        for col in range(10): # 10개씩
            x = col * 60 + 5 # 5픽셀 간격
            y = row * 30 + 50 # 50픽셀 위에서 시작
            brick = Brick(color, x, y)
            all_sprites.add(brick)
            bricks.add(brick)

# --- 텍스트 표시 함수 ---
def draw_text(surf, text, size, x, y, color=WHITE):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surf.blit(text_surface, text_rect)

# --- 게임 초기화 및 스프라이트 그룹 생성 ---
all_sprites = pygame.sprite.Group()
bricks = pygame.sprite.Group()
balls = pygame.sprite.Group()

# 객체 생성
paddle = Paddle()
ball = Ball()
all_sprites.add(paddle, ball)
balls.add(ball)

setup_bricks() # 벽돌 배치

# --- 메인 게임 루프 ---
running = True
while running:
    clock.tick(FPS)

    # 1. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 마우스 클릭 시 공 발사
        if event.type == pygame.MOUSEBUTTONDOWN and ball.is_stuck:
            ball.is_stuck = False

    # 2. 게임 오버 확인
    if lives <= 0:
        game_over = True
    
    if len(bricks) == 0:
        game_over = True
        
    if game_over:
        running = False # 게임 종료

    # 3. 게임 상태 업데이트
    all_sprites.update()
    
    # 4. 충돌 처리

    # a) 공과 패들의 충돌
    if pygame.sprite.collide_rect(ball, paddle):
        # 공이 패들 위쪽에 부딪혔을 때만 튕기도록
        if ball.rect.bottom >= paddle.rect.top and ball.speed_y > 0:
            ball.speed_y *= -1
            
            # 패들 중앙에서 벗어난 정도에 따라 X축 속도 조절
            diff = ball.rect.centerx - paddle.rect.centerx
            ball.speed_x += diff * 0.1 # 약간의 각도 변화

    # b) 공과 벽돌의 충돌
    brick_hits = pygame.sprite.spritecollide(ball, bricks, True) # True: 충돌한 벽돌 삭제
    for hit_brick in brick_hits:
        ball.speed_y *= -1 # Y축 방향 반전
        score += 10
        
    # 5. 화면 그리기
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # 6. UI 그리기
    draw_text(screen, f"Score: {score}", 24, SCREEN_WIDTH // 2, 15)
    draw_text(screen, f"Lives: {lives}", 24, 60, 15)

    # 7. 화면 업데이트
    pygame.display.flip()

# --- 게임 종료 화면 ---
if game_over:
    screen.fill(BLACK)
    if lives > 0:
         draw_text(screen, "YOU WIN!", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, GREEN)
    else:
         draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, RED)
    draw_text(screen, f"Final Score: {score}", 36, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
    pygame.display.flip()
    
    # 결과 화면을 3초간 보여준 후 종료
    time.sleep(3)


# 8. Pygame 종료
pygame.quit()
sys.exit()
