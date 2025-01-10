# flask_mini_JPC
oz 부트캠프 Flask mini project JPC 팀


#표시하기 하고 옆에 이름 적기

##생성 완료 시 폴더 또는 파일 옆 ⭐️
##파일 업데이트 🚀
##파일 수정 🍀
##셍성 해야하는 파일 ❌

oz_form/⭐️                        # 프로젝트 폴더 
├── app/⭐️                        # Flask 애플리케이션 코드 폴더 
│   ├── __init__.py             # 앱 초기화 및 설정 파일
│   ├── sevices/⭐️                # DB 상호작용 orm 코드 폴더
│   │   ├── users.py            # users 테이블 관련 orm 함수
│   │   ├── questions.py        # quetions 테이블 관련 orm 함수
│   │   ├── choices.py          # choices 테이블 관련 orm 함수
│   │   └── answers.py          # answers 테이블 관련 orm 함수
│   ├── models.py               # SQLAlchemy 모델 정의
│   ├── routes.py               # 뷰 및 라우트 정의
├── config.py                   # Flask 및 데이터베이스 설정 파일
├── requirements.txt⭐️          # 필요한 Python 패키지 목록
├── run.py                      # 개발환경에서 테스트 하는 실행 파일
├── wsgi.py                     # 배포환경에서의 실행 파일
└── migrations/⭐️                 # Flask-Migrate를 위한 데이터베이스 마이그레이션

#업뎃 정보 gitmoji사용하기

git add (파일명) -원하는 파일 커밋 해준다
gitmoji -c - 커밋한 파일에 대해 설명하기 위한 이모지 선택 후 제목과 내용을 적어준다.
*만약 적다가 모르고 엔터 눌러도 당황하지 않기
git log - 작성한 메세지 확인
git commit --amend - 깃 메세지 변경 코드 적어준 후 "i"를 눌러 인서트 모드로 진입 후 메세지 변경, "esc" 눌러주고 ":wq" 마지막으로 저장하고 나가기 까지 눌러주면 변경 완료!!
git log 마무리 확인!