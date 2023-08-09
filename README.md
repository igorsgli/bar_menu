# "Bar menu" / "Барное меню"
An online service for publishing recipes for your favorite cocktails, with the ability to subscribe to publications of other users, add your favorite cocktails to your Favorites, and also download a summary list of the ingredients of your favorite cocktails, which will be useful in the store.
***********************
Онлайн-сервис для публикации рецептов своих любимых коктейлей, с возможностью подписываться на публикации других пользователей, добавлять понравившиеся коктейли в "Избранное", а также скачать сводный список ингредиентов понравившихся коктейлей, который пригодится в магазине.

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
