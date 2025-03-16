from db import delete_food_entry

def delete_food(message, bot):
    bot.reply_to(message, "Напишите прием пищи, который хотите удалить, в формате: /delete еда. Например: /delete Яблоко")

def delete_food_entry_handler(message, bot):
    user_id = message.chat.id
    food = message.text[len('/delete '):].strip()
    if delete_food_entry(user_id, food):
        bot.reply_to(message, f"Удалено: {food}")
    else:
        bot.reply_to(message, f"Не удалось найти: {food}")
