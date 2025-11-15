import streamlit as st

# --- 초기 설정 ---
# 'count'가 session_state에 없으면 0으로 초기화합니다.
if 'count' not in st.session_state:
    st.session_state.count = 0

# --- 함수 정의 ---
def click_button():
    """클릭 시 점수를 1 증가시키는 함수"""
    st.session_state.count += 1
    # 10점마다 보너스 메시지를 추가합니다.
    if st.session_state.count % 10 == 0:
        st.toast(f'🎉 보너스! {st.session_state.count}점 달성!', icon='🌟')

def reset_game():
    """점수를 0으로 초기화하는 함수"""
    st.session_state.count = 0
    st.toast('게임을 초기화했습니다!', icon='🔄')

# --- Streamlit UI 구성 ---

st.title('🖱️ 간단한 클리커 게임')
st.caption('버튼을 눌러 점수를 올리세요!')

# 현재 점수를 표시합니다.
st.metric(label="현재 점수", value=st.session_state.count)

# 클리커 버튼
st.button('클릭해서 점수 올리기!', on_click=click_button)

# 게임 초기화 버튼
st.button('점수 초기화', on_click=reset_game)

# --- 진행 상황 메시지 (선택 사항) ---
if st.session_state.count >= 50:
    st.success('대단해요! 50점 이상입니다!')
elif st.session_state.count >= 20:
    st.info('잘하고 있어요! 계속 눌러보세요!')

