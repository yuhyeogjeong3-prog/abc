import streamlit as st
import time
import random

# --- 초기 상태 설정 ---
def initialize_game():
    """게임 상태를 초기화합니다."""
    st.session_state.score = 0
    # 마지막 박자가 발생한 시점 (초)
    st.session_state.last_beat_time = time.time()
    # 현재 박자 번호
    st.session_state.beat_count = 0
    # 게임 메시지
    st.session_state.game_message = "게임 시작! 아래 '버튼'을 박자에 맞춰 누르세요."
    # 게임 시작 시간
    st.session_state.start_time = time.time()
    # 게임 실행 여부
    st.session_state.running = True
    # 박자 간격 (2.0초마다 박자가 나옴)
    st.session_state.beat_interval = 2.0
    # 박자 허용 범위 (±0.5초 이내에 눌러야 함)
    st.session_state.tolerance = 0.5 

# --- 게임 로직 함수 ---

def check_hit():
    """사용자가 버튼을 눌렀을 때 타이밍을 확인합니다."""
    if not st.session_state.running:
        st.session_state.game_message = "게임을 다시 시작해 주세요."
        return

    press_time = time.time()
    
    # 마지막 박자 이후 경과 시간 (이전 박자 이벤트 이후 시간)
    time_since_last_beat = press_time - st.session_state.last_beat_time
    
    # 1. 사용자가 이번 박자를 놓쳤는지 확인 (다음 박자 간격의 1.5배 이상 시간이 지났으면 놓친 것으로 간주)
    if time_since_last_beat > st.session_state.beat_interval * 1.5:
        st.session_state.game_message = f"❌ 놓침! 박자가 너무 늦었습니다."
        st.toast("Too Late!", icon="👎")
        # 다음 박자 시점을 현재 시점으로 보정
        st.session_state.last_beat_time = press_time
        return
        
    # 2. 이번 박자의 정중앙 시간 (마지막 박자 시점 + 박자 간격)
    exact_beat_time = st.session_state.last_beat_time + st.session_state.beat_interval
    time_diff = abs(press_time - exact_beat_time)
    
    if time_diff <= st.session_state.tolerance:
        # 허용 범위 내에 누름 (성공)
        st.session_state
