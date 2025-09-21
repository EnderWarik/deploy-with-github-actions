ВЫПОЛНЕН ЧЕЛЛЕНДЖ
[Helios Deploy Action v0.0.1](https://github.com/EnderWarik/helios-deploy-action/releases/tag/v0.0.1)



## Исследования:
1.Отечественные CDN для ускорения доставки контента

Российские CDN (Yandex Cloud CDN, VK Cloud, Selectel, Cloud.ru) имеют узлы по РФ и снижают задержки для аудитории внутри страны.

-Возможности Gitverse для реализации CI/CD.

GitVerse — отечественная платформа хостинга кода с аналогом GitHub Actions для автоматизации CI/CD.
Поддерживается привычный YAML-синтаксис, триггеры на push/PR/release и запуск пайплайнов на runners.
Пайплайны позволяют собирать, тестировать и деплоить проекты, храня артефакты и метрики качества в одной экосистеме.
Есть ограничения, но они связаны с молодостью платформы и развивающейся экосистемой.

-Какие существуют варианты деплоя статического сайта в продакшен среду и какие технические инструменты для этого могут потребоваться, приведите примеры.

VPS + Nginx/Apache: положить сборку в root, настроить Let’s Encrypt/Certbot для ssl.
Docker: собрать образ на базе nginx:alpine со статикой и деплоить на сервер/в K8s; удобно для CI/CD и изоляции.
Object Storage + CDN (Yandex/Selectel/VK Cloud): хостить статику в S3-бакете, привязать домен, включить CDN.
SaaS-платформы авто-деплоя (аналогично Netlify/Vercel): подключить репозиторий, автосборка и публикация на CDN (для РФ — смотреть локальные аналоги или self-hosted).
Git-Pages-подход: публикация из репозитория по push;

## Отчет:
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

![Проверка деплоя](images/Снимок%20экрана%202025-09-21%20в%2021.32.56.png)

10.Отлаживаем
![Проверка](images/Снимок%20экрана%202025-09-21%20в%2021.44.12.png)