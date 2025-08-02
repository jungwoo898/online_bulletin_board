# Pybo 게시판

Flask와 SQLAlchemy로 구현된 간단한 질문/답변 게시판입니다. 회원 가입, 로그인, 글 작성과 추천 기능을 포함하고 있습니다.

## 폴더 구조

- `pybo/` - 애플리케이션 코드와 뷰, 모델, 폼이 위치합니다.
- `config/` - 개발 및 배포 환경 설정 파일.
- `venv/` - 가상환경(예시에 포함되어 있으나 필요시 새로 생성 가능).

## 필요 패키지

다음 패키지가 필요합니다. 버전은 예시입니다.

```
Flask==3.1.0
Flask-Migrate==4.1.0
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.2
email-validator==2.2.0
SQLAlchemy==2.0.40
WTForms==3.2.1
Jinja2==3.1.6
Werkzeug==3.1.3
Mako==1.3.9
blinker==1.9.0
colorama==0.4.6
```

## 실행 방법

1. Python 가상환경을 생성하고 위의 패키지를 설치합니다.
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows의 경우 venv\Scripts\activate
   pip install Flask Flask-Migrate Flask-SQLAlchemy Flask-WTF email-validator SQLAlchemy WTForms Jinja2 Werkzeug Mako blinker colorama
   ```
2. 환경 변수를 설정합니다.
   ```bash
   export FLASK_APP=pybo
   export APP_CONFIG_FILE=config/development.py
   ```
3. 데이터베이스를 초기화합니다.
   ```bash
   flask db upgrade
   ```
4. 애플리케이션을 실행합니다.
   ```bash
   flask run
   ```
   기본적으로 `http://127.0.0.1:5000` 에서 서비스가 시작됩니다.

## 기능 요약

- 질문 목록 조회 및 검색
- 질문과 답변 작성/수정/삭제
- 사용자 가입과 로그인/로그아웃
- 추천(투표) 기능 및 작성자 권한 검사

즐겁게 사용해 보세요!
