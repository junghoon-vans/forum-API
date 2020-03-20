forum-API
===
![Python](https://img.shields.io/badge/Python-3.7.6-green.svg)
![Docker](https://img.shields.io/badge/Docker-19.03.8-skyblue.svg)
![Postgres](https://img.shields.io/badge/PostgreSQL-10.0-blue.svg)
![Redis](https://img.shields.io/badge/Redis-latest-red.svg)

실행 방법
---

```bash
docker-compose up
```

루트 디렉토리에서 위 명령어로 서버를 실행합니다.


- 웹 브라우저에서 `127.0.0.1`로 접속해서 API call을 테스트하실 수 있습니다.
- API call에 사용되는 인자는 해당 페이지의 `Swagger API document`를 확인하시면 됩니다.
    - `Swagger UI` 적용을 위해 사용된 패키지는 `flask-restplus`입니다.

### 콘솔 사용 시, 주의할 점
- 콘솔에서 직접 API call을 테스트할 수 있습니다만, 사용자를 특정해야 하는 요청에는 `세션쿠키`를 전송해야만 합니다.
-  `세션쿠키`는 로그인 요청 시 HTTP 응답 헤더의 `Set-Cookie`에서 확인할 수 있습니다.

    <details><summary>콘솔 사용 예시</summary>
    <br>
    로그인 시

    ```
    http 127.0.0.1/user/login 'email=<email>' 'password=<password>'  HTTP/1.0 200 OK
    Content-Length: 69
    Content-Type: application/json
    Date: Thu, 19 Mar 2020 18:46:19 GMT
    Server: Werkzeug/0.16.1 Python/3.7.6
    Set-Cookie: session=eyJzZXNzaW9uIjoiNzU4MDFiZGYtNTkyOC00YjYwLTljZmMtMWJkNDAwMmZmYzU3In0.XnO9-w.JoWYrJwfpgPzxmUj4SEfkUYYVo4; HttpOnly; Path=/
    Vary: Cookie

    {
        "message": "Successfully Logged in",
        "status": "success"
    }
    ```

    로그아웃 시
    ```bash
    # httpie로 요청 시
    http 127.0.0.1/user/logout 'Cookie:session=eyJzZXNzaW9uIjoiNzU4MDFiZGYtNTkyOC00YjYwLTljZmMtMWJkNDAwMmZmYzU3In0.XnO9-w.JoWYrJwfpgPzxmUj4SEfkUYYVo4'

    HTTP/1.0 200 OK
    Content-Length: 70
    Content-Type: application/json
    Date: Thu, 19 Mar 2020 18:59:22 GMT
    Server: Werkzeug/0.16.1 Python/3.7.6
    Set-Cookie: session=; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Path=/    
    {
        "message": "Successfully Logged out",
        "status": "success"
    }
    ```

### 로컬 환경에서 flask 서버 실행

만약에 flask 서버를 별도로 로컬에서 구동해야 한다면, 패키지 설치가 된 가상환경을 준비해야 합니다. 
- 루트 디렉토리에 `venv` 생성 및 실행
- flask 디렉토리의 `requirements.txt`에 정의된 패키지 설치

또한 실행과 DB 연결에 필요한 환경변수도 설정해주어야 합니다.

<details><summary>환경변수 설정</summary>

    # DB 관련 변수
    export POSTGRES_DB="developer"
    export POSTGRES_USER="developer"
    export POSTGRES_PASSWORD="devpassword"
    export POSTGRES_URL="localhost:25000"

    export REDIS_HOST="localhost"
    export REDIS_PORT="25100"

    # 개발 모드
    export FLASK_CONFIG="dev"
</details>

> 위 환경변수는 도커 실행시 작동되는 DB로 연결하게 되어 있습니다.

DB 마이그레이션의 경우 `alembic`을 사용하시면 됩니다. 명령어는 다음과 같습니다.

```bash
alembic revision --autogenerate -m "message" # 마이그레이션 생성
alembic upgrade head # 마이그레이션 적용
```
> [env.py](flask\src\migrations\env.py)파일을 수정하여 [models.py](flask\src\app\models.py)와 연동하여 마이그레이션 파일을 생성하도록 설정하였습니다. 

API 구조
---

### User API

| URL | method | Usage | Session Cookie |
|-----|--------|-------|---------|
| /user/register | POST | 회원가입 | |
| /user/login | POST | 로그인 | 생성 |
| /user/logout | GET | 로그아웃 | 삭제 |

### Board API

| URL | method | Usage | Session Cookie |
|-----|--------|-------|---------|
| /board/ | POST | 게시판 생성 | 필요 |
| /board/\<str:board_name\> | DELETE | 게시판 제거 | 필요 |
| /board/\<str:board_name\> | PUT | 게시판 이름 변경 | 필요 |
| /board/\<int:page\> | GET | 게시판 목록 조회 | |

### DashBoard API

| URL | method | Usage | Session Cookie |
|-----|--------|-------|---------|
| /board/all/\<int:page\> | GET | 대시보드 조회 | |

### BoardArticle API

| URL | method | Usage | Session Cookie |
|-----|--------|-------|---------|
| /board/\<str:board_name\> | POST | 글 작성 | 필요 |
| /board/\<str:board_name\>/detail/\<int:article_id> | DELETE | 글 제거 | 필요 |
| /board/\<str:board_name\>/detail/\<int:article_id> | PUT | 글 수정 | 필요 |
| /board/\<str:board_name\>/detail/\<int:article_id> | GET | 글 내용 조회 | |
| /board/\<str:board_name\>/\<int:page\> | GET | 글 목록 조회 | |

> Session Cookie 필드에 필요로 작성된 부분은 API 요청시 `세션쿠키`를 함께 전송해야 하는 경우임

> page인자는 페이지네이션을 위한 것임

세션
---

redis DB를 활용하여 세션 기능을 구현하였습니다. 사용자 로그인 시 세션에 필요한 `key`를 쿠키로 반환하며, 이는 게시판이나 게시글을 수정하는 등의 요청에 필요합니다.

해당 설정은 [redis.py](flask\src\utils\redis.py) 파일에 정의되어 있습니다.


페이지네이션
---
`게시판 목록 조회`, `글 목록 조회`, `대시보드 조회`와 같은 목록을 반환하는 API는 페이지네이션을 적용하였습니다.

- 게시판 목록 조회
    - 전체 게시판 목록을 이름을 기준으로 내림차순
        - `offset` 방식으로 5개의 게시판 목록을 반환
- 글 목록 조회
    - 특정 게시판의 글 목록을 작성일을 기준으로 올림차순
        - `offset` 방식으로 5개의 게시글 목록을 반환
- 대시보드 조회
    - 전체 게시판 목록을 이름을 기준으로 내림차순
        - `offset` 방식으로 5개의 게시판 목록을 반환
    - 각 게시판의 글 목록을 작성일을 기준으로 올림차순
        - `limit` 방식으로 5개의 게시글 목록을 반환



디렉터리 구조
---

        .
        ├── README.md
        ├── docker-compose.yml
        ├── flask
        │   ├── Dockerfile
        │   ├── __init__.py
        │   ├── requirements.txt
        │   ├── src
        │   │   ├── __init__.py
        │   │   ├── alembic.ini
        │   │   ├── app
        │   │   │   ├── __init__.py
        │   │   │   ├── api
        │   │   │   ├── route
        │   │   │   ├── config.py
        │   │   │   └── models.py
        │   │   ├── manage.py
        │   │   ├── migrations
        │   │   │   ├── README
        │   │   │   ├── __init__.py
        │   │   │   ├── env.py
        │   │   │   ├── script.py.mako
        │   │   │   └── versions
        │   │   └── utils
        │   │       ├── __init__.py
        │   │       ├── redis.py
        │   │       ├── restplus.py      
        │   │       └── sqlalchemy.py
        │   └── uwsgi.ini
        └── nginx
            ├── Dockerfile
            └── default.conf
