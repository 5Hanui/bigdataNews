# 서버 시작점
# 서버 가동에만 구현 집중
# 포트, 호스트, 상용/테스트 => 환경 변수로 설정
from service import createApp 

app = createApp()

if __name__ == '__main__':
    app.run(debug=True)  # 디버그하면서 바로 반영.
