import streamlit as st
import numpy as np

# --- 게임 초기 상태 설정 ---
def initialize_game():
    """게임 상태를 초기화합니다."""
    # 벽돌: 3x5 행렬 (1 = 벽돌 있음, 0 = 벽돌 없음)
    st.session_state.bricks = np.ones((3, 5), dtype=int)
    # 공 위치 (단순화를 위해 1차원 x 위치만 사용)
    st.session_state.ball_x = 2
    # 공 이동 방향 (1=오른쪽, -1=왼쪽)
    st.session_state.ball_dir = 1
    # 패들 위치 (중앙 기준)
    st.session_state.paddle_x = 2
    # 점수
    st.session_state.score = 0
    # 게임 메시지
    st.session_state.message = "게임을 시작합니다! 패들을 움직여 공을 받아보세요."
    # 게임 상태
    st.session_state.game_over = False

# --- UI 함수: 벽돌 상태를 시각화 ---
def display_bricks():
    """벽돌 배열 상태를 이모지로 시각화하여 표시합니다."""
    display = ""
    for row in st.session_state.bricks:
        for brick in row:
            if brick == 1:
                display += "🧱"  # 벽돌 있음
            else:
                display += "⚪"  # 벽돌 깨짐
        display += "\n"
    st.text(display)

# --- UI 함수: 패들과 공 위치 시각화 ---
def display_game_area():
    """공과 패들의 위치를 시각화합니다."""
    game_line = ["_"] * 5  # 게임 영역 (5칸)
    
    # 공 위치 표시
    if 0 <= st.session_state.ball_x < 5:
        game_line[st.session_state.ball_x] = "🔴"
    
    # 패들 위치 표시 (패들은 공 아래, 패들 위치는 1칸)
    if 0 <= st.session_state.paddle_x < 5:
        paddle_line = ["-"] * 5
        paddle_line[st.session_state.paddle_x] = "🏓"
        
        st.text(" ".join(game_line))
        st.text(" ".join(paddle_line))

# --- 게임 로직 함수 ---
def move_paddle(direction):
    """패들을 왼쪽(-1) 또는 오른쪽(1)으로 이동시킵니다."""
    if st.session_state.game_over:
        return
        
    new_x = st.session_state.paddle_x + direction
    # 경계 검사 (0에서 4 사이)
    if 0 <= new_x
