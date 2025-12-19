import telebot

TOKEN = "8573068742:AAF0EUjjaWI4FwJkcrzqLfSjaQ4BKoBTHYU"
CHAT_ID = 230939852 

bot = telebot.TeleBot(TOKEN)

def send_order(name, phone, bouquet):
    msg = f"Новый заказ!\nИмя: {name}\nТелефон: {phone}\nБукет: {bouquet}"
    bot.send_message(CHAT_ID, msg)

# Тестовое сообщение
send_order("Тест", "111111", "Букет тест")

