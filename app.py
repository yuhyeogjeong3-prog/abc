import streamlit as st
import random

# --- 상수 설정 ---
GAME_WIDTH = 5  # 게임 공간의 너비 (5칸)
ITEM_SPAWN_RATE = 0.5 # 장애물이 나타날 확률 (0.0 ~ 1.0)
SCORE_PER_MOVE = 5 # 이동할 때마다 얻는 점수

# --- 초기 상태 설정 ---
def initialize_game():
    """게임 상태를 초기화합니다."""
    # 맵: 2x5 (위는 장애물 라인, 아래는 플레이어 라인)
    st.session_state.map = [[0] * GAME_WIDTH, [0] * GAME_WIDTH]
    
    st.session_state.player_pos = GAME_WIDTH // 2  # 플레이어 초기 위치 (중앙)
    st.session_state.score = 0
    st.session_state.message = "게임 시작! 버튼을 눌러 이동하고 장애물을 피하세요."
    st.session_state.game_over = False
    
    # 플레이어 위치 설정
    st.session_state.map[1][st.session_state.player_pos] = 1
    # 초기 장애물 생성
    spawn_obstacles()

# --- UI 함수: 맵 시각화 ---
def display_map():
    """맵 상태를 이모지로 시각화하여 표시합니다."""
    mapping = {
        0: "⬜", # 빈 공간
        1: "🏃", # 플레이어
        2: "🚧"  # 장애물
    }
    
    display = ""
    # 윗줄 (장애물)
    for item in st.session_state.map[0]:
        display += mapping[item]
    display += "\n"
    # 아랫줄 (플레이어)
    for player in st.session_state.map[1]:
        display += mapping[player]
        
    st.text(display)

# --- 게임 로직 함수 ---

def spawn_obstacles():
    """새로운 장애물을 무작위로 생성합니다."""
    # 윗줄(장애물 라인) 초기화
    st.session_state.map[0] = [0] * GAME_WIDTH
    
    # 무작위로 장애물 생성
    for i in range(GAME_WIDTH):
        if random.random() < ITEM_SPAWN_RATE:
            st.session_state.map[0][i] = 2 # 장애물 (2) 생성

def move_player(direction):
    """
    플레이어를 이동시키고 다음 라운드를 진행합니다.
    direction: -1 (좌), 1 (우)
    """
    if st.session_state.game_over:
        return
        
    r, c = 1, st.session_state.player_pos
    new_c = c + direction
    
    # 1. 경계 확인
    if 0 <= new_c < GAME_WIDTH:
        # 현재 위치 지우기
        st.session_state.map[1][c] = 0
        
        #
