# shipping_test_task
Тестовое задание по созданию API приложения

Условие задачи: https://faint-adasaurus-4bc.notion.site/web-Python-Middle-c1467cf373c24f0cafb8bfe0fe77cc79

Requirements: Docker

Start:
- docker-compose bild  # создаём обра
- docker-compose up  # запускаем контейнер
- docker-compose exec cars_web python manage.py migrate --noinput  # делаем миграцию

Заходим в браузере на localhost:8000 или 127.0.0.1:8000
