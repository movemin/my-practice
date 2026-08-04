# /Users/dong-minlee/projects/myproject/config.py
import os

BASE_DIR = os.path.dirname(__file__)

# SQLite DB 파일 경로 설정
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
