from flask import Flask, send_from_directory
from flask_cors import CORS
from telegram_bot.bot import send_order  # твоя функция для Telegram

app = Flask(__name__, static_folder='.')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/order', methods=['POST'])
def order():
    data = request.json
    name = data.get('name')
    phone = data.get('phone')
    bouquet = data.get('bouquet')
    send_order(name, phone, bouquet)
    return {'status': 'ok'}

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Render задаёт свой порт
    app.run(host='0.0.0.0', port=port)





