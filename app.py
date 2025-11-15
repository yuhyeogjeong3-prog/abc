import streamlit as st

# --- 초기 설정 ---
if 'count' not in st.session_state:
    st.session_state.count = 0

# --- 함수 정의 ---
def click_coin():
    """코인을 클릭 시 점수를 1 증가시키는 함수"""
    st.session_state.count += 1
    # 10점마다 보너스 메시지
    if st.session_state.count % 10 == 0:
        st.toast(f'🎉 보너스! {st.session_state.count}점 달성!', icon='🌟')

def reset_game():
    """점수를 0으로 초기화하는 함수"""
    st.session_state.count = 0
    st.toast('게임을 초기화했습니다!', icon='🔄')

# --- Streamlit UI 구성 ---

st.title('🪙 이미지 클리커 게임')
st.caption('코인을 클릭해서 점수를 올리세요!')

# 1. 현재 점수 및 시각화
st.subheader('현재 점수')
st.metric(label="누적 코인 획득량", value=st.session_state.count)

# 점수에 따른 축하 메시지
if st.session_state.count > 0:
    st.progress(min(st.session_state.count / 100, 1.0), text=f"다음 레벨까지: {100 - (st.session_state.count % 100)}점")
    if st.session_state.count >= 100:
         st.balloons()


st.divider()

# 2. 이미지 클릭 요소
# Streamlit의 버튼 대신, HTML/Markdown을 사용하여 이미지를 클릭 가능한 버튼처럼 만듭니다.
# 하지만 Streamlit의 내장 기능으로는 이미지 클릭 이벤트를 직접 처리할 수 없으므로,
# '이미지'와 '투명 버튼'을 겹쳐서 사용하는 것이 일반적인 방법입니다.

# 이 예시에서는 **이미지를 표시**하고, 그 **아래에 버튼**을 배치하여 클릭하게 합니다.

# 이미지 파일 경로 (반드시 이 파일이 스크립트와 같은 폴더에 있어야 합니다.)
IMAGE_PATH = "coin.png" 

try:
    # 이미지를 표시합니다.
    st.image(IMAGE_PATH, width=200)

    # 이미지 바로 아래에 실제 클릭 로직을 담당하는 버튼을 배치합니다.
    st.button(
        label='💰 코인 획득!', 
        on_click=click_coin, 
        use_container_width=True
    )
    st.caption('클릭할 때마다 점수가 올라갑니다.')

except FileNotFoundError:
    st.error(f"⚠️ **오류:** 이미지 파일 '{IMAGE_PATH}'를 찾을 수 없습니다. 스크립트와 같은 폴더에 넣어주세요.")
    # 파일이 없을 경우 임시 버튼으로 대체
    st.button('클릭해서 점수 올리기 (이미지 없음)', on_click=click_coin)


st.divider()

# 3. 게임 초기화 버튼
st.button('게임 초기화', on_click=reset_game)
