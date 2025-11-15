import streamlit as st
import time
import random

# --- 상수 설정 ---
# 박자 간격 (블록이 이동하는 주기, 1.5초)
BEAT_INTERVAL = 1.5 
# 정확도 허용 범위 (±0.3초 이내에 눌러야 함)
TOLERANCE = 0.3 
# 초기 탑 너비 (최대 5칸)
INITIAL_WIDTH = 5

# --- 초기 상태 설정 ---
def initialize_game():
    """게임 상태를 초기화합니다."""
    st.session_state.score = 0
    st.session_state.stack_height = 0     # 쌓은 블록 개수
    st.session_state.current_width = INITIAL_WIDTH # 현재 탑의 너비
    st.session_state.last_beat_time = time.time() # 마지막 박자 시간
    st.session_state.game_message = "탑 쌓기 게임 시작! '쌓기' 버튼을 박자에 맞춰 누르세요."
    st.session_state.running = True
    st.session_state.game_over = False

# --- 게임 로직 함수 ---

def stack_block():
    """'쌓기' 버튼 클릭 시 호출되며, 타이밍을 확인하고 블록을 쌓습니다."""
    if st.session_state.game_over or not st.session_state.running:
        st.session_state.message = "게임을 다시 시작해 주세요."
        return

    press_time = time.time()
    
    # 마지막 정박자 이후 경과 시간
    time_since_last_beat = press_time - st.session_state.last_beat_time
    
    # 가장 가까운 정박자 시점과의 시간 차이 계산
    # (이번 박자의 정중앙 시간 = 마지막 박자 시간 + 박자 간격)
    exact_beat_time = st.session_state.last_beat_time + BEAT_INTERVAL
    time_diff = abs(press_time - exact_beat_time)

    # 1. 타이밍 정확도 판단
    if time_diff <= TOLERANCE:
        # 허용 범위 내에 성공적으로 누름
        
        # 2. 정확도에 따른 블록 너비 및 점수 조정
        if time_diff < 0.1:
            # ✨ Perfect (오차 0.1초 미만)
            accuracy_score = 10
            cut_amount = 0 # 너비 변화 없음
            st.session_state.game_message = f"✨ Perfect! (너비 {st.session_state.current_width} 유지)"
            st.toast("Perfect!", icon="⭐")
        elif time_diff < TOLERANCE / 2:
            # ✅ Good (오차 중간)
            accuracy_score = 5
            cut_amount = 1 # 너비 1 감소
            st.session_state.game_message = f"✅ Good! (너비 {st.session_state.current_width} -> {max(1, st.session_state.current_width - cut_amount)})"
            st.toast("Good!", icon="👍")
        else:
            # 🔶 Ok (오차 최대치 근처)
            accuracy_score = 2
            cut_amount = 2 # 너비 2 감소
            st.session_state.game_message = f"🔶 Ok! (너비 {st.session_state.current_width} -> {max(1, st.session
