# :t-shirts: 꾸공 Rest API server code

---

### 목차

- 1. 꾸공 프로젝트
- 2. 개발환경
- 3. 설치

---

## 1. 꾸공 프로젝트

추후 작성

## 2. 개발환경

docker image로 관리

- docker hub으로 부터 image 다운

  > `$ docker pull seungsu3579/django_env:1.2`

- 컨테이너 실행

  > `$ docker run -idt -v (rest_api_directory):/root/kkugong_server -p (8000):8000 --name=kkugong_api seungsu3579/django_env:1.2 /usr/bin/zsh`

- 컨테이너 진입(zsh 쉘 프로세스에 접속)

  > `$ docker exec -it kkugong_api /usr/bin/zsh`

## 3. 설치

pipenv로 파이썬 라이브러리 버전관리

- 파이썬3 가상환경 생성

  > `$ pipenv --three`

- 기타 라이브러리 자동 설치

  > `$ pipenv install --pre`

- django server 실행

  > `$ python manage.py runserver 0.0.0.0:8000`

## 4. MysqlDB 연결

장고의 디폴트 데이터베이스(SQLite)를 사용하기에는 제약이 있었다.

- 1. docker image로 관리, data는 볼륨 마운트를 통해 로컬에 저장

> `$ docker run -d --name=mysql -e MYSQL_ROOT_PASSWORD=(pw) -v (data_directory):/var/lib/mysql seungsu3579/mysql:1.0 /bin/bash`

- 2. mysql 컨테이너에 접속하여 django rest api 용 관리자 계정 생성 후 권한 할당

> `$ docker exec -it mysql mysql -u root -p` > `mysql> create user '(id)'@'%' identified by '(pw)';` > `mysql> grant all privileges on (database).* to '(id)'@'%';`

- 3. django의 settings.py에 DATABASE설정 변경

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '(database_name)',
        'USER': '(admin_id)',
        'PASSWORD': '(admin_pw)',
        'HOST': '(mysql container IP)',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}
```

- migrate!
