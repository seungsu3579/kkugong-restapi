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
