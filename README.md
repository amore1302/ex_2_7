﻿#Проект укорачивает ссылки с помощью сервиса bitly

##Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.

##Что надо сделать bitly
Для работы программв используется сервис bitly
Вы должны зарегистрироваться на этом сервисе и получить там секретный ключ
Секретный ключ определяет Ваши ссылки на сервесе bitly

##Виртуальное окружение программы
Секретный ключ необходимо разместить в файле .env
Файл .env должен быть из одной строки вида :
TOKEN_BIT_LY=Вашсекретный_ключ
Внимание  TOKEN_BIT_LY  должно быть написано в верхнем ргистре

##что надо установить
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
pip install -r requirements.txt
для выполнения необходимо также установить пакеты :
argparse
sys
dotenv
