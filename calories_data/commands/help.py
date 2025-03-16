def send_help(message, bot):
    help_text = (
        "Вот что я могу:\n"
        "/add - Добавить прием пищи\n"
        "/summary - Показать дневной отчет о калориях\n"
        "/reset - Сбросить данные за день\n"
        "/delete - Удалить прием пищи"
    )
    bot.reply_to(message, help_text)
