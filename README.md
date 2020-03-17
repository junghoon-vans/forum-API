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
| / | GET | 게시판 목록 조회 |
| / | POST | 게시판 생성 |
| /\<str:board_name\> | PUT | 게시판 이름 변경 |
| /\<str:board_name\> | DELETE | 게시판 제거 |

### BoardArticle API

| URL | method | Usage |
|-----|--------|-------|
| /\<str:board_name\> | GET | 글 목록 조회 |
| /\<str:board_name\> | POST | 글 생성 |
| /\<str:board_name\>/\<int:article_id> | GET | 글 내용 조회 |
| /\<str:board_name\>/\<int:article_id> | PUT | 글 제목 혹은 내용 수정 |
| /\<str:board_name\>/\<int:article_id> | DELETE | 글 제거 |

### Dashboard API

| URL | method | Usage |
|-----|--------|-------|
| /dashboard | GET | 모든 게시판에서 최근 n개의 글의 제목 가져옴 |