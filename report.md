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
# c рекомендованным доп пакетам
pip install "nikola[extras]"
nikola version
```
![Установка Nikola](images/Снимок%20экрана%202025-09-21%20в%2019.50.31.png)

5. Пуш в репозиторий
```bash
# репо уже был склонен с гитхаба
git add -A
git commit -m "init"
git push -u origin
```
![Пуш в репозиторий](images/Снимок%20экрана%202025-09-21%20в%2019.58.41.png)

6. Настройка Actions 

- build: checkout репозитория; установка Python; установка Nikola; сборка `nikola build`; загрузка артефакта `output/`.
- deploy: скачивание артефакта; упаковка в `site.tgz`; установка `sshpass`; доверие ключу Helios; `scp` архива; распаковка в `~/public_html` (с очисткой при `clean=true`).



7. активация аккаунта на Helios. 
https://github.com/Roggired/ITMO/blob/master/general/how-to-connect-to-helios.md

8. Корректируем yml-файл под место куда деплоим
Деплою в ~/public_html

9. Проверяем, что все задеплоилось


10.Отлаживаем