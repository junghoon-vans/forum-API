forum-API
===
![Python](https://img.shields.io/badge/Python-3.7.6-green.svg)
![Docker](https://img.shields.io/badge/Docker-19.03.8-skyblue.svg)
![Postgres](https://img.shields.io/badge/PostgreSQL-10.0-blue.svg)
![Redis](https://img.shields.io/badge/Redis-latest-red.svg)

flask-based bulletin board service API

API Structure
---

### User API

| URL | method | Usage |
|-----|--------|-------|
| /user/register | POST | 회원가입 |
| /user/login | POST | 로그인 |
| /user/logout | GET | 로그아웃 |

### Board API

| URL | method | Usage |
|-----|--------|-------|
| /board/ | GET | 게시판 목록 조회 |
| /board/ | POST | 게시판 생성 |
| /board/\<str:board_name\> | PUT | 게시판 이름 변경 |
| /board/\<str:board_name\> | DELETE | 게시판 제거 |

### BoardArticle API

| URL | method | Usage |
|-----|--------|-------|
| /board/\<str:board_name\> | GET | 글 목록 조회 |
| /board/\<str:board_name\> | POST | 글 생성 |
| /board/\<str:board_name\>/\<int:article_id> | GET | 글 내용 조회 |
| /board/\<str:board_name\>/\<int:article_id> | PUT | 글 제목 혹은 내용 수정 |
| /board/\<str:board_name\>/\<int:article_id> | DELETE | 글 제거 |

### Dashboard API

| URL | method | Usage |
|-----|--------|-------|
| /board/all | GET | 모든 게시판에서 최근 n개의 글의 제목 가져옴 |

How to run
---

- 루트 디렉토리에서 `docker-compose up` 명령어를 실행합니다.
    > 설정은 docker-compose.yml과 Dockerfile에 정의되어 있습니다.
- 이후 서버가 실행되면 4개의 도커 컨테이너가 실행됩니다.
    > flask, nginx, postgres, redis

Directory tree
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
        │   │   │   ├── config.py
        │   │   │   ├── models.py
        │   │   │   ├── controllers
        │   │   │   └── services
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
