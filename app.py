import streamlit as st
import random

# --- 초기 상태 설정 ---
def initialize_game_state():
    """게임 상태를 초기화합니다."""
    # 초기 체력, 탄약, 메시지 등을 설정합니다.
    if 'enemy_hp' not in st.session_state:
        st.session_state.enemy_hp = 100 
    if 'player_ammo' not in st.session_state:
        st.session_state.player_ammo = 10 
    if 'game_message' not in st.session_state:
        st.session_state.game_message = "게임을 시작합니다! '발사' 버튼을 누르세요."
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False

# --- 게임 로직 함수 ---

def shoot():
    """총알을 발사하는 로직"""
    if st.session_state.game_over:
        st.session_state.game_message = "게임이 끝났습니다! '다시 시작'을 눌러주세요."
        return

    if st.session_state.player_ammo <= 0:
        st.session_state.game_message = "🚨 탄약이 부족합니다! '재장전'을 하세요."
        return

    # 탄약 1 감소
    st.session_state.player_ammo -= 1

    # 데미지 계산 (랜덤하게 10에서 30 사이)
    damage = random.randint(10, 30)

    # 적 체력 감소
    st.session_state.enemy_hp -= damage

    # 메시지 업데이트
    st.session_state.game_message = f"🎯 발사! 적에게 {damage}의 데미지를 입혔습니다."

    # 승리 확인
    if st.session_state.enemy_hp <= 0:
        st.session_state.enemy_hp = 0
        st.session_state.game_message = "🎉 승리! 적을 물리쳤습니다!"
        st.session_state.game_over = True
    
    # 적의 반격 시뮬레이션
    if not st.session_state.game_over:
         st.toast("⚡ 적이 반격했습니다!", icon="💥")


def reload_ammo():
    """탄약을 재장전하는 로직"""
    if st.session_state.game_over:
        st.session_state.game_message = "게임이 끝났습니다! '다시 시작'을 눌러주세요."
        return
        
    st.session_state.player_ammo = 10
    st.session_state.game_message = "✅ 탄약을 재장전했습니다! 다시 발사하세요
