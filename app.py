import streamlit as st

# --- 원소 데이터 ---
# (번호: [원소 이름, 기호]) 형태로 저장
ELEMENTS = {
    1: ["수소", "H"], 2: ["헬륨", "He"], 3: ["리튬", "Li"], 4: ["베릴륨", "Be"],
    5: ["붕소", "B"], 6: ["탄소", "C"], 7: ["질소", "N"], 8: ["산소", "O"],
    9: ["플루오린", "F"], 10: ["네온", "Ne"], 11: ["나트륨", "Na"], 12: ["마그네슘", "Mg"],
    13: ["알루미늄", "Al"], 14: ["규소", "Si"], 15: ["인", "P"], 16: ["황", "S"],
    17: ["염소", "Cl"], 18: ["아르곤", "Ar"], 19: ["칼륨", "K"], 20: ["칼슘", "Ca"]
    # 더 많은 원소를 추가할 수 있습니다.
}

def get_element_info(atomic_number):
    """원자 번호에 해당하는 원소 이름과 기호를 반환합니다."""
    return ELEMENTS.get(atomic_number) # 딕셔너리에서 번호로 검색

# --- Streamlit UI 구성 ---

st.title('⚛️ 원자 번호로 원소 찾기')
st.caption('1번부터 20번까지의 원소를 검색할 수 있습니다.')

# 1. 사용자 입력 (원자 번호)
# 슬라이더 또는 숫자 입력 위젯을 사용할 수 있습니다.
atomic_number = st.slider(
    '원자 번호를 선택하세요:', 
    min_value=1, 
    max_value=20, 
    value=6, # 기본값은 탄소(6)
    step=1
)

st.subheader(f'선택된 번호: {atomic_number}번')

# 2. 결과 처리 및 출력
element_info = get_element_info(atomic_number)

if element_info:
    # 원소 정보가 있을 경우
    name, symbol = element_info
    
    st.success(f"✅ {atomic_number}번 원소는 **{name}** 입니다.")
    
    st.metric(
        label="원소 기호", 
        value=symbol,
        help=f'{name}의 원소 기호입니다.'
    )
    
else:
    # 원소 정보가 딕셔너리에 없을 경우 (예: 20번을 초과하는 번호 입력 시)
    st.warning("⚠️ 해당 번호의 원소 정보가 데이터에 없습니다.")
