from db import get_user_data
from summary import get_summary_text

def summary(message, bot):
    summary_text = get_summary_text(message.chat.id)
    bot.reply_to(message, summary_text)
