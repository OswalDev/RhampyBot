import requests
import random
import mysql.connector

# Define the function for the /start command
def start(chat_id):
    url = f'https://api.telegram.org/bot6020925389:AAF-tKDNyZiRg9Rxc8ymddXr-p-I2t2Drck/sendMessage'
    payload = {'chat_id': chat_id, 'text': 'Milu tengo la panocha calentorra'}
    requests.post(url, data=payload)

# Define the function for the /random command
def random_comment(chat_id):
    number = random.randint(0, 12)
    rhampySays = ["Chufa chufa", "luuu", "Ando calentorra luuuu", "jajaj", "jajaja", "jaj", "Sal? Chicha", "Sal? Chichicha", "Talking to the Luuuu", "Es la hora del platano, chicheñol", "Fai chupame la paleta y déjamela como un lienzo de colores", "Luu, estoy ridícula"]
    url = f'https://api.telegram.org/bot6020925389:AAF-tKDNyZiRg9Rxc8ymddXr-p-I2t2Drck/sendMessage'
    payload = {'chat_id': chat_id, 'text': f"{rhampySays[number-1]}"}
    requests.post(url, data=payload)

# Define the function for the /help command
def help(chat_id):
    url = f'https://api.telegram.org/bot6020925389:AAF-tKDNyZiRg9Rxc8ymddXr-p-I2t2Drck/sendMessage'
    payload = {'chat_id': chat_id, 'text': 'Here are the available commands:\n/start - Start the bot\n/random - Generate a random rhampy comment\n/help - Display the help message\n/info - Display information about the bot\n/status - Display the current status of the bot'}
    requests.post(url, data=payload)

# Define the function for the /info command
def info(chat_id):
    url = f'https://api.telegram.org/bot6020925389:AAF-tKDNyZiRg9Rxc8ymddXr-p-I2t2Drck/sendMessage'
    payload = {'chat_id': chat_id, 'text': 'This bot was created using Python and the Telegram API for the single purpose of trolling rhampy.'}
    requests.post(url, data=payload)

# Define the function for the /status command
def status(chat_id):
    url = f'https://api.telegram.org/bot6020925389:AAF-tKDNyZiRg9Rxc8ymddXr-p-I2t2Drck/sendMessage'
    payload = {'chat_id': chat_id, 'text': 'Mas cachonde que milu viendole las patas a mari'}
    requests.post(url, data=payload)

# Defining mysql database

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="flame",
  password="yourpassword"
)

print(mydb)

# Poll for new updates and handle them
def main():
    last_update_id = None
    while True:
        url = f'https://api.telegram.org/bot6020925389:AAF-tKDNyZiRg9Rxc8ymddXr-p-I2t2Drck/getUpdates'
        params = {'timeout': 60, 'offset': last_update_id}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            updates = response.json()['result']
            if updates:
                for update in updates:
                    last_update_id = update['update_id'] + 1
                    if 'message' in update:
                        message = update['message']
                        chat_id = message['chat']['id']
                        text = message.get('text', '')
                        # text = message['text']
                        if text == '/start':
                            start(chat_id)
                        elif text == '/random':
                            random_comment(chat_id)
                        elif text == '/help':
                            help(chat_id)
                        elif text == '/info':
                            info(chat_id)
                        elif text == '/status':
                            status(chat_id)

if __name__ == '__main__':
    main()