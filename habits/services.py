from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN
import requests

URL = TELEGRAM_URL
TOKEN = TELEGRAM_TOKEN


def send_message(text, chat_id):
    requests.post(
        url=f'{URL}{TOKEN}/sendMessage',
        data={
            'chat_id': chat_id,
            'text': text
        }
    )
