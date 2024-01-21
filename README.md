#  **Telegram_Bot_Quest**
Телеграм_бот_квест – это телеграмм-бот с текстовой RPG-игрой, которая позволит игрокам взаимодействовать и принимать решения. 

## **Техническое задание**
### **Цель**
Создать текстовую RPG-игру, которая позволит игрокам взаимодействовать и принимать решения. Реализовать игру нужно в виде телеграм-бота с использованием библиотеки telebot (pyTelegramBotAPI).
### **Основные функции бота**
#### **1. Начало игры**
- Игра может запускаться несколькими пользователями одновременно.
- При запуске бота игрок получает приветственное сообщение и предложение начать игру.
#### **2. Мир и локации**
- В игре должно быть как минимум три уровня, а в каждом из них — хотя бы одна локация. Локациями могут быть деревни, леса, города, здания, комнаты и т.д.
- У каждой локации должно быть описание, иллюстрация, сгенерированная нейросетью, и список доступных действий.
- Варианты ответа игрока должны быть представлены в виде кнопок.
- В зависимости от действий игрока есть разные варианты развития сюжета.
#### **3. Дополнительная функциональность**
По желанию можно добавить другие интересные функции. Например:
- поиск инвентаря,
- задания, которые меняют исход игры.

### **Чек-лист оценки проекта**
#### **Обязательные пункты:** 
##### **1. Сценарий**
- При сдаче проекта представлена документация с описанием сценария игры.
- Детально проработаны уровни игры.
##### **2. Иллюстрации**
- Для каждого уровня игры разработано не менее четырёх вариантов иллюстрации.
- На каждом уровне игры показано не меньше двух иллюстраций.
##### **3. Реализация**
- Профиль бота оформлен: у него есть имя, описание, информация, аватарка, команды бота.
- Варианты ответа пользователя представлены в виде кнопок.
Это базовые критерии. 

Кроме базовых критериев, рекомендуется соблюсти и следующие дополнительные условия:
- В коде реализованы все основные функции, описанные в ТЗ.
- Код разделён на модули: обработка сообщений и механика игры не должны быть в одном файле.
- Данные о локациях игры хранятся в отдельном JSON-файле, а не в самом коде проекта.
- Бот не падает при возникновении ошибки. В случае ошибки пользователю должно приходить сообщение, что что-то пошло не так.
- Бот запущен на удалённом сервере (необязательно).
- Код хорошо читается и понятно организован. Понятные комментарии и названия переменных приветствуются!

## **Структура игры**
### **1. Логика игрового сюжета** 
Логика игрового сюжета: ![Логика игрового сюжета](https://github.com/Sensei-PGD/Telegram_Bot_Quest/blob/main/schemes/The_logic_of_the_game.png)     

### **2. Структура бота с функциями** 
Общая структура бота:
- файл **data.py** с функциями по считыванию и сохранению данных пользователя
- JSON-файл **game_data.json** с локациями игры (локация : варианты ответа)
- JSON-файл **user_data.json** для хранения данных пользователя
- логика игры реализована в **bot.py**, при этом сюжет считывается из**game_data.json**
- файл **bot.py**, в котором реализованы все функции бота 
- бот считывает ник пользователя и обращается по нему
- кнопки для выбора ответа
Структура бота с функциями: ![Структура бота с функциями]()  
### **3. Принцип работы бота** 
Принцип работы бота: ![Принцип работы бота](https://github.com/Sensei-PGD/Telegram_Bot_Quest/blob/main/schemes/How_the_bot_works.jpg)    

### **4. Общее решение** 
Общее решение: ![Общее решение](https://github.com/Sensei-PGD/Telegram_Bot_Quest/blob/main/schemes/The_general_solution.jpg)    

## **Инструкция по установке и использованию проекта**
Для реализации проекта потребуется следующее:
### **Шаг 1. Установка ПО**
- Компилятор PyCharm Community Edition
- Язык программирования Python
### **Шаг 2. Установка пакетов**
- В данном случае при установке PyCharm Community Edition нужно установить библиотеку telebot, для этого открываем вкладку «Python Packages» и в поисковой строке вставляем: pyTelegramBotAPI. Скачиваем и переходим к следующему шагу.
### **Шаг 3. Написание кода**
- Теперь приступаем к написанию кода. Для этого можно обратиться в [GitHub](https://github.com/Sensei-PGD/Telegram_Bot_Quest.git) за ним. Создаем три файла: bot.py (головной файл), data.py (файл с функциями чтения и записи в json-формат) и game_data.json (файл с локациями). 
### **Шаг 4. Добавляем картинки**
- Мы должны в самом проекте создать папку «Image» и положить в него картинки. Для этого можно перейти в [облачное хранилище](https://github.com/Sensei-PGD/Telegram_Bot_Quest/tree/main/illustrations). Скачиваем и помещаем. Все изображения сгенерированы нейросетью [Kandinsky](https://fusionbrain.ai/?ref=vc.ru) 
### **Шаг 5. Создаем телеграмм-бота**
- Теперь, когда мы написали код, осталось создать самого бота в Телеграмме. Для этого нам поможет конструктор чат-ботов [BotFather](https://t.me/BotFather). С дальнейшей инструкцией вы можете ознакомиться по этой [ссылке на статью]( https://vc.ru/dev/903659-kak-sozdat-bota-v-telegram-za-5-minut-botfather)
### **Шаг 6. Финал**
- Подключаем токен в bot.py и проверяем нашего бота. 

## **Дополнительные источники**
- [Ссылка на телеграмм-бота](https://t.me/Anumi_assistent_bot)
- [Ссылка на облако с изображениями](https://disk.yandex.ru/d/nOqjwEqlcGkz0g) 
