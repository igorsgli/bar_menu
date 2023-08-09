# "Bar menu" / "Барное меню"
Service for storing, publishing and managing the recipes of your favorite cocktails.
***********************
Сервис для хранения, публикации и управления рецептами своих любимых коктейлей.

### Stack / Стек:
* Python
* Django
* Django REST framework
* PostgresSQL
* React (basics)
* Gunicorn
* Nginx
* Docker

## Launch the project / Инструкции по запуску

### 1. Git clone / Клонировать репозиторий:
```
git clone https://github.com/igorsgli/bar_menu.git
cd bar_menu
```
### 2. Rename .env_example to .env / Переименовать файл .env_example в .env:
```
cd infra
mv ./.env_example ./.env
```
### 3. Run docker-compose / Запустить docker-compose:
```
docker-compose up -d --build
```
### 4. Site is available at / Сайт доступен по адресу:
```
http://localhost/
```
### 5. Project documentation is available at / Документация доступна по адресу:
```
http://localhost/api/docs/
```
