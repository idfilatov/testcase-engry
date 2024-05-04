# Testcase Engry

## :gear: Как завести проект

:snake: Поставить python 3.11  

- `python -m venv .venv`
- `source .venv/bin/activate (Linux)`  
- `.venv\Scripts\activate (Windows)`
- `pip install -r requirements.txt`
- `pip install -r requirements-test.txt`  


### :green_circle: Запуск проекта локально для разработки
`python -m app.main --port 9009`


### :microscope: Запуск тестов
`python -m pytest`

### :whale2: Сборка контейнера с приложением
`docker build -t testcase_engry:latest .`

### :whale: Запуск контейнера с приложением
`docker run --restart=always -d -p 8000:9009 --name engry testcase_engry:latest`
