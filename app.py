import random
import sys

def guess_number_game():
    """순수 Python으로 터미널에서 실행되는 숫자 맞추기 게임."""
    
    print("====================================")
    print("🔢 숫자 맞추기 게임을 시작합니다!")
    print("1부터 100 사이의 숫자를 맞춰보세요.")
    print("====================================")

    # 1. 정답 숫자 생성
    try:
        secret_number = random.randint(1, 100)
    except ValueError:
        print("오류: random 모듈 사용에 문제가 있습니다.")
        return

    attempts = 0 # 시도 횟수
    
    while True:
        try:
            # 2. 사용자 입력 받기
            guess = input("당신의 추측은? (숫자를 입력하세요): ")
            
            # '종료' 명령어 처리
            if guess.lower() in ('종료', 'exit'):
                print(f"게임을 종료합니다. 정답은 {secret_number}였습니다.")
                break

            # 3. 입력이 유효한 숫자인지 확인
            try:
                guess = int(guess)
            except ValueError:
                print("⚠️ 유효한 숫자를 입력하거나 '종료'를 입력하세요.")
                continue

            # 4. 범위 확인
            if guess < 1 or guess > 100:
                print("⚠️ 1부터 100 사이의 숫자를 입력해야 합니다.")
                continue

            attempts += 1

            # 5. 정답 확인 및 힌트 제공
            if guess < secret_number:
                print("⬆️ 더 높은 숫자입니다!")
            elif guess > secret_number:
                print("⬇️ 더 낮은 숫자입니다!")
            else:
                # 6. 정답! 게임 종료
                print("\n🎉🎉🎉 축하합니다! 🎉🎉🎉")
                print(f"정답은 {secret_number}였습니다.")
                print(f"총 {attempts}번 만에 맞추셨습니다!")
                break

        except KeyboardInterrupt:
            # Ctrl+C로 종료 시 처리
            print(f"\n\n[프로그램 강제 종료] 정답은 {secret_number}였습니다.")
            sys.exit()

if __name__ == "__main__":
    guess_number_game()
