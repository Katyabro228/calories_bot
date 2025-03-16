from db import delete_food_entry
from summary import get_summary_text

def delete_food(message, bot):
    bot.reply_to(message, "Напишите прием пищи, который хотите удалить, в формате: еда. Например: Яблоко")

def delete_food_entry_handler(message, bot):
    user_id = message.chat.id
    food = message.text.strip()
    if delete_food_entry(user_id, food):
        bot.reply_to(message, f"Удалено: {food}")
        summary_text = get_summary_text(user_id)
        bot.reply_to(message, summary_text)
    else:
        bot.reply_to(message, f"Не удалось найти: {food}")
