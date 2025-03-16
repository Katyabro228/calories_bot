from db import clear_user_data

def reset_data(message, bot):
    user_id = message.chat.id
    clear_user_data(user_id)
    bot.reply_to(message, "Ваш дневник питания очищен.")
