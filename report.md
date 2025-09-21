1.
Установка Python 
```bash
brew update
brew install python
python3 --version
```
Проверка pip
```bash
pip3 --version
```

![Установка Python](images/Снимок%20экрана%202025-09-21%20в%2019.35.19.png)

2.Установка virtualenv
```bash
python3 -m pip install --user virtualenv
python3 -m virtualenv --version
virtualenv --version
```
![Проверка virtualenv](images/Снимок%20экрана%202025-09-21%20в%2019.40.01.png)

3.Создание каталога и активация виртуального окружения
```
python3 -m virtualenv .venv
source .venv/bin/activate
```
![Создание каталога](images/Снимок%20экрана%202025-09-21%20в%2019.44.48.png)

4.Установка Nikola
```bash
pip install "nikola"
nikola version
```
