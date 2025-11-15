import streamlit as st

# 1. 제목(Title) 추가하기
st.title('👋 첫 번째 Streamlit 앱')

# 2. 텍스트 표시하기
st.write('이것은 Streamlit으로 만든 아주 간단한 웹 페이지입니다.')

# 3. 버튼 위젯 추가하고 상호작용하기
if st.button('클릭해 보세요!'):
    st.write('버튼이 클릭되었습니다! 감사합니다! 😊')
else:
    st.write('위에 있는 버튼을 눌러보세요.')
