import streamlit as st
import numpy as np

# --- 게임 초기 상태 설정 ---
def initialize_game():
    """게임 상태를 초기화하고 맵을 설정합니다."""
    # 5x5 맵 (0: 통로, 1: 벽, 2: 점, 3: 팩맨, 4: 유령)
    st.session_state.game_map = np.array([
        [1, 1, 1, 1, 1],
        [1, 2, 0, 2, 1],
        [1, 3, 1, 4, 1], # (2,1)에 팩맨(3), (2,3)에 유령(4) 초기 위치
        [1, 2, 0, 2, 1],
        [1, 1, 1, 1, 1]
    ], dtype=int)
    
    st.session_state.pacman_pos = [2, 1] # [row, col]
    st.session_state.ghost_pos = [2, 3]
    st.session_state.score = 0
    st.session_state.message = "팩맨 게임 시작! 방향 버튼을 눌러 이동하세요."
    st.session_state.game_over = False

# --- UI 함수: 맵 시각화 ---
def display_map():
    """맵 배열을 이모지로 변환하여 표시합니다."""
    # 맵 요소에 따른 이모지 매핑
    mapping = {
        0: "⬜", # 통로 (배경)
        1: "🟦", # 벽
        2: "🟡", # 점 (도트)
        3: "😀", # 팩맨 (P)
        4: "👻"  # 유령 (G)
    }
    
    display = ""
    for r in range(st.session_state.game_map.shape[0]):
        for c in range(st.session_state.game_map.shape[1]):
            display += mapping[st.session_state.game_map[r, c]]
        display += "\n"
    st.text(display)

# --- 게임 로직 함수 ---

def move_pacman(dr, dc):
    """팩맨을 (dr, dc)만큼 이동시키고 충돌을 처리합니다."""
    if st.session_state.game_over:
        return
        
    r, c = st.session_state.pacman_pos
    new_r, new_c = r + dr, c
