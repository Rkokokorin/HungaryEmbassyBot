import json

import requests

def get_chat_id():
    object1 = read_json("bot.json")
    token = object1.get("token")
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    print(requests.get(url).json())

def send_telegram_update():
    object1 = read_json("bot.json")
    token = object1.get("token")
    chat_id = object1.get("chat_id")
    message = "POSSIBLY TIME FOUND, CHECK PC"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())

def read_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {path} не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {path}.")
    return None

if __name__ == '__main__':
    get_chat_id()
    send_telegram_update()