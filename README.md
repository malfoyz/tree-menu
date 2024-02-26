<h2 align="center">Tree menu on Django</h2>

Тестовое задание от UpTrader. Древовидное меню на Django.

### Инструменты разработки

**Стек:**
- Python = 3.9.0
- Django
- Postgres

## Старт

#### 1) Создать образ

    docker-compose build

##### 2) Запустить контейнер

    docker-compose up
    
##### 3) Перейти по адресу

    http://127.0.0.1:8000/

## Разработка с Docker

##### 1) Сделать форк репозитория

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) В корне проекта создать .env.dev

    DEBUG=1
    SECRET_KEY=django-insecure-u=fv=lpo$_fhi^u)woyle-%4-2vq-0-o=v9p7!qb31ny-db!-y
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    
    # Data Base
    POSTGRES_DB=tree_menu
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DATABASE=tree_menu
    POSTGRES_USER=tree_menu_user
    POSTGRES_PASSWORD=tree_menu_pass
    POSTGRES_HOST=tree_menu-db
    POSTGRES_PORT=5432
    
    DATABASE=postgres
    
##### 4) Создать образ

    docker-compose build

##### 5) Запустить контейнер

    docker-compose up
    
##### 6) Создать суперюзера

    docker exec -it tree-menu-tree_menu_back-1 python manage.py createsuperuser
                                                        
##### 7) Если нужно очистить БД

    docker-compose down -v
