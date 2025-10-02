THEME = 'custom'

BLOG_TITLE = "EnderWar Site"
BLOG_DESCRIPTION = "Кастомная тема Nikola"
BLOG_AUTHOR = "Алексей Москалёв"

DEFAULT_LANG = "ru"
TIMEZONE = "Europe/Moscow"

POSTS = ()
PAGES = (("pages/*.md", "pages", "page.tmpl"),)

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/pages/home/", "Главная"),
        ("/pages/report/", "Отчёт"),
    ),
}

# Базовые опции
TYPOGRIFY = True
USE_BUNDLES = False
INDEX_PATH = ""

