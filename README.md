# flask_mini_JPC
oz 부트캠프 Flask mini project JPC 팀

주제 : 독서

독서에 관하여 즐겨읽는 책, 읽는 시간대, 일주일에 몇번 독서를 즐겨하는 지등의
질문을 하고 설문을 받는다.

유저 생성, 조회 함수 - 정미정
질문 및 선택지 생성, 조회 함수 - 박현성
이미지 생성, 조회 함수 - 최혜민

oz_form                        # 프로젝트 폴더 
├── app                        # Flask 애플리케이션 코드 폴더 
│   ├── __init__.py             # 앱 초기화 및 설정 파일
│   ├── sevices                # DB 상호작용 orm 코드 폴더
│   │   ├── users.py            # users 테이블 관련 orm 함수
│   │   ├── questions.py        # quetions 테이블 관련 orm 함수
│   │   ├── choices.py          # choices 테이블 관련 orm 함수
│   │   └── answers.py          # answers 테이블 관련 orm 함수
│   ├── models.py               # SQLAlchemy 모델 정의
│   ├── routes.py               # 뷰 및 라우트 정의
├── config.py                   # Flask 및 데이터베이스 설정 파일
├── requirements.txt          # 필요한 Python 패키지 목록
├── run.py                      # 개발환경에서 테스트 하는 실행 파일
├── wsgi.py                     # 배포환경에서의 실행 파일
└── migrations               # Flask-Migrate를 위한 데이터베이스 마이그레이션
