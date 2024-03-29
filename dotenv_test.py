# Импортируем модуль os
import os
# Импортируем модуль sys
import sys
import dotenv

dotenv.load_dotenv()


while True:
    # Принимаем имя переменной среды
    key_value = input("Enter the key of the environment variable:")
    # Проверяем, инициализирована ли переменная
    try:
        if os.environ[key_value]:
            print("The value of", key_value, " is ", os.environ[key_value])
    # Если переменной не присвоено значение, то ошибка
    except KeyError:
        print(key_value, "environment variable is not set.")
    # Завершаем процесс выполнения скрипта
    sys.exit(1)
