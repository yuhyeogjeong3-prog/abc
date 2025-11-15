import streamlit as st
import random

# --- 상수 설정 ---
GAME_WIDTH = 5  # 게임 공간의 너비 (5칸)
ITEM_SPAWN_RATE = 0.5 # 낙하물이 나타날 확률 (0.0 ~ 1.0)
SCORE_PER_DODGE = 10 # 피할 때마다 얻는 점수

# --- 초기 상태 설정 ---
def initialize_game():
    """게임 상태를 초기화합니다."""
    # 맵 상태 (0: 빈 공간, 1: 플레이어, 2: 낙하물)
    # 맵은 2x5 형태로, 위는 낙하물, 아래는 플레이어 위치
    st.session_state.map = [[0] * GAME_WIDTH, [0] * GAME_WIDTH]
    
    st.session_state.player_pos = GAME_WIDTH // 2  # 플레이어 초기 위치 (중앙)
    st.session_state.score = 0
    st.session_state.message = "게임 시작! '이동' 버튼을 누르거나 '다음 라운드'를 진행하세요."
    st.session_state.game_over = False
    
    # 플레이어 위치 설정
    st.session_state.map[1][st.session_state.player_pos] = 1

# --- UI 함수: 맵 시각화 ---
def display_map():
    """맵 상태를 이모지로 시각화하여 표시합니다."""
    mapping = {
        0: "⬜", # 빈 공간
        1: "🏃", # 플레이어
        2: "💣"  # 낙하물 (폭탄)
    }
    
    display = ""
    # 윗줄 (낙하물)
    for item in st.session_state.map[0]:
        display += mapping[item]
    display += "\n"
    # 아랫줄 (플레이어)
    for player in st.session_state.map[1]:
        display += mapping[player]
        
    st.text(display)

# --- 게임 로직 함수 ---

def move_player(direction):
    """플레이어를 왼쪽(-1) 또는 오른쪽(1)으로 이동시킵니다."""
    if st.session_state.game_over:
        return
        
    r, c = 1, st.session_state.
