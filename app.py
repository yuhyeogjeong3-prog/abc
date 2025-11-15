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
    if 0 <= new_x < 5:
        st.session_state.paddle_x = new_x
        st.session_state.message = "패들을 이동했습니다."
    else:
        st.session_state.message = "더 이상 움직일 수 없습니다."

def move_ball():
    """공을 한 칸 이동시키고 충돌을 처리합니다."""
    if st.session_state.game_over:
        return

    # 공 위치 업데이트
    st.session_state.ball_x += st.session_state.ball_dir
    
    new_message = ""

    # 1. 벽 충돌 (좌우 경계)
    if st.session_state.ball_x <= 0 or st.session_state.ball_x >= 4:
        st.session_state.ball_dir *= -1 # 방향 반전
        new_message = "벽에 맞고 튕겼습니다!"

    # 2. 벽돌 충돌 시뮬레이션 (간단화: 공이 가장 위로 올라갔을 때만 처리)
    if st.session_state.ball_x == 2 and st.session_state.bricks[0, 2] == 1:
        # 중앙 벽돌을 맞았다고 가정
        st.session_state.bricks[0, 2] = 0
        st.session_state.score += 10
        st.session_state.ball_dir *= -1
        new_message = f"🌟 벽돌을 깼습니다! (+10점)"
    
    # 3. 패들 충돌 (공이 가장 아래로 내려왔을 때)
    elif st.session_state.ball_x == 2:
        if st.session_state.ball_x == st.session_state.paddle_x:
            st.session_state.ball_dir *= -1
            new_message = "✨ 패들로 공을 받았습니다!"
        else:
            # 패들로 못 받음 = 게임 오버
            st.session_state.message = f"💔 공을 놓쳤습니다! 최종 점수: {st.session_state.score}"
            st.session_state.game_over = True
            return

    # 4. 승리 확인
    if np.sum(st.session_state.bricks) == 0:
        st.session_state.message = f"🏆 모든 벽돌을 깼습니다! 승리! 최종 점수: {st.session_state.score}"
        st.session_state.game_over = True
    
    if new_message:
        st.session_state.message = new_message
    
    # 게임 루프를 수동으로 다시 실행하도록 버튼을 활성화

# --- Streamlit UI 구성 ---

st.title('🧱 텍스트 벽돌깨기 시뮬레이션')
st.caption('이것은 Streamlit의 한계로 인해 **그래픽 없는 텍스트 기반 시뮬레이션**입니다.')

if 'bricks' not in st.session_state:
    initialize_game()

# 1. 게임 상태 및 점수 표시
st.subheader('게임 정보')
col1, col2 = st.columns(2)
col1.metric("점수", st.session_state.score)
col2.metric("남은 벽돌 수", np.sum(st.session_state.bricks))

st.divider()

# 2. 게임 화면
st.subheader('게임 화면')
display_bricks()
display_game_area()
st.text_area("메시지", value=st.session_state.message, height=50, disabled=True)

# 3. 조작 버튼
st.subheader('조작')
col_left, col_move, col_right, col_reset = st.columns(4)

col_left.button('◀️ 왼쪽', on_click=lambda: move_paddle(-1), use_container_width=True, disabled=st.session_state.game_over)
col_right.button('▶️ 오른쪽', on_click=lambda: move_paddle(1), use_container_width=True, disabled=st.session_state.game_over)
col_move.button('🚀 공 이동 (클릭)', on_click=move_ball, use_container_width=True, disabled=st.session_state.game_over)

col_reset.button('🔄 다시 시작', on_click=initialize_game, use_container_width=True)
