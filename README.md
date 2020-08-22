# django_foundation
Набор домашних заданий к курсу GeekBrains "Основы Django Framework"

## Урок 1. Знакомство с фреймворком

1. Подготовить исходники для проекта – 3 страницы из верстки магазина, и разместить их в одной папке.
2. Установить Django и PyCharm. Создать проект и в нем приложение «mainapp». Проверить, что все работает.
3. Разместить шаблоны и статические файлы в соответствующих папках. Настроить проект – файл settings.py. Отредактировать файл диспетчера URL-адресов urls.py.
4. Написать функции-обработчики для всех страниц – файл views.py в приложении «mainapp». Проверить работу всех страниц проекта в черновом режиме (без стилей и изображений).
5. Откорректировать пути к статическим файлам и адреса гиперссылок в меню. Проверить, что все работает как положено (стили и изображения грузятся, гиперссылки работают).
6. Сделать файл run.bat для быстрого запуска Django-сервера.

## Урок 2. Шаблон + Контекст = html

1. Реализовать наследование шаблонов в проекте. Меню подключить как подшаблон.
2. Реализовать в проекте механизмы работы со статическими файлами и URL-адресами, которые прошли на уроке.
3. Поработать с шаблонными тегами и фильтрами (заглавные буквы, вывод текущей даты в шаблоне).
4. Организовать вывод динамического контента на страницах (элементы меню, список товара, заголовок страницы).
5. \* Организовать загрузку динамического контента в контроллеры с жесткого диска (например, в формате «json»).

## Урок 3. Модели + ORM = данные

1. Настроить проект для работы с медиафайлами.
2. Создать модели в проекте (обязательно должно быть поле с изображениями) и выполнить миграции.
3. Поработать с моделями в консоли.
4. Создать суперпользователя. Настроить админку и поработать в ней.
5. Организовать работу с моделями в контроллерах и шаблонах.
6. Реализовать автоматическое формирование меню категорий по данным из модели.
7. \* Создать диспетчер URL в приложении. Скорректировать динамические URL
-адреса в шаблонах. Поработать с имитацией переходов по категориям в адресной строке браузера.
8. \* Организовать загрузку данных в базу из файла.

## Урок 4. Аутентификация и регистрация пользователя

1. Создать модель пользователя в проекте. Обязательно добавить поле с изображением и возрастом. Выполнить настройки в файле конфигурации.
2. Организовать загрузку данных в БД из файла.
3. Реализовать механизм аутентификации в проекте.
4. Реализовать механизм регистрации пользователя.
5. Организовать просмотр и редактирование данных пользователем.
6. \* Разобраться с механизмом валидации данных формы. Создать свои валидаторы.

## Урок 5. Пользователь + товар = корзина

1. Поработать с запросами в консоли через механизм Django ORM.
2. Реализовать механизм вывода товаров по категориям.
3. \* Организовать динамическую генерацию меню категорий и подсветку выбранной категории.
4. Создать приложение корзины.
5. Реализовать механизм добавления товара в корзину.
6. Вывести в меню счетчик купленных товаров.
7. \* Написать в модели корзины методы для определения общего количества и стоимости добавленных товаров. Вывести эти величины в меню вместо счетчика, сделанного на уроке.

## Урок 6. Корзина + AJAX + декораторы

1. Добавить к модели корзины методы и вывести в меню количество товара и их полную стоимость.
2. Реализовать механизм просмотра содержимого корзины и удаления товаров из нее.
3. Реализовать просмотр товара, скорректировать адреса в каталоге и на главной странице так, чтобы при нажатии на товар появлялась страница просмотра. Добавление товара в корзину теперь должно быть только с этой страницы.
4. Защитить доступ к корзине декоратором @login_required.
5. \* Реализовать асинхронное редактирование количества товаров в корзине при помощи AJAX.
6. \* Реализовать механизм вывода случайного товара на странице «горячее предложение», которая появляется при входе в каталог.

## Урок 7. Собственная админка

1. Создать приложение админки и интегрировать его в проект.
2. Реализовать механизм CRUD для объектов пользователей магазина. Можно полностью удалять объекты (не использовать свойство is_active).
3. Реализовать механизм CRUD для объектов категорий товара. Можно полностью удалять объекты (не использовать свойство is_active).
4. Защитить доступ к админке декоратором @user_passes_test.
5. \* Реализовать удаление через свойство is_active.
6. \* Реализовать «подсветку» в админке неактивных объектов пользователей и категорий.

## Урок 8. Полезное: страничный вывод, шаблонные фильтры, CBV

1. Реализовать работу с товарами в админке.
2. Организовать постраничный вывод в каталоге и админке.
3. Перевести как можно больше контроллеров в проекте на CBV (минимум по одному для каждого из рассмотренных классов).
4. Написать свои шаблонные фильтры и применить их.
5. \* Перевести админку на AJAX.