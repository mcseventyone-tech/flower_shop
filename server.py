from flask import Flask, request
from flask_cors import CORS  
from telegram_bot.bot import send_order


app = Flask(__name__)
CORS(app)

@app.route("/order", methods=["POST"])
def order():
    data = request.json
    print("Получен заказ:", data)  # <-- добавляем лог
    send_order(data['name'], data['phone'], data['bouquet'])
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)



