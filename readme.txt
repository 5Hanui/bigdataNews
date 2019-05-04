# 구조
newsbigdata
    └ service           : 서비스 핵심 구현 패키지
        └ templates     : html 위치한곳
            └ mod       : 공용 html 파일
            └ pages     : 페이지당 콘텐츠가 실제 구현되는 파일
            *.html      : 페이지 자체 파일(구조가 구현된), 홈, 로그인, ...
        └ static        : 정적데이터 위치한곳
        └ __init__.py   : service 패키지 구현부분
    └ run.py            : 시작점
    └ readme.txt        : 서비스 설명