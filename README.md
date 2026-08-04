# 🐍 Pybo - Flask 게시판 프로젝트

플라스크(Flask) 프레임워크와 SQLAlchemy ORM을 활용하여 개발한 웹 게시판 애플리케이션입니다.

> 📚 **참고 교재 및 출처**  
> 본 프로젝트는 이지스퍼블리싱의 **[Do it! 점프 투 플라스크]**(박응용 저) 교재를 바탕으로 실습하고 학습한 내용을 기록한 프로젝트입니다.

---

## 🛠️ 사용 기술 및 환경 (Tech Stack)

* **Language:** Python 3.12+
* **Framework:** Flask
* **ORM:** Flask-SQLAlchemy, Flask-Migrate
* **Database:** SQLite
* **Template Engine:** Jinja2

---

## 📁 프로젝트 구조 (Directory Structure)

```text
myproject/
├── config.py             # 데이터베이스 및 애플리케이션 설정
├── pybo/
│   ├── __init__.py       # 애플리케이션 팩토리 (create_app)
│   ├── models.py         # SQLAlchemy DB 모델 (Question, Answer 등)
│   ├── templates/        # Jinja2 HTML 템플릿
│   │   └── question/
│   │       ├── question_list.html
│   │       └── question_detail.html
│   └── views/            # 블루프린트 라우팅 컨트롤러
│       ├── main_views.py
│       └── question_views.py
└── .gitignore