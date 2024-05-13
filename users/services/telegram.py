import requests
import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_MAIN_URL = os.getenv('TELEGRAM_MAIN_URL')


def telegram_bot_message(message, chat_id):
    """the function of sending a message using the Telegram webhook"""
    send_text = f'{TELEGRAM_MAIN_URL}{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
    response = requests.get(send_text)
    return response.json()
