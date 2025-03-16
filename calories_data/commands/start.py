from telebot import types

def send_welcome(message, bot):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    add = types.KeyboardButton('/add')
    summary = types.KeyboardButton('/summary')
    reset = types.KeyboardButton('/reset')
    help = types.KeyboardButton('/help')
    delete = types.KeyboardButton('/delete')
    markup.add(
        add, delete,
        summary, reset,
        help
    )
    bot.reply_to(message, "Привет! Я бот для расчета калорий и ведения дневника питания. Напиши /help, чтобы узнать, что я умею!", reply_markup=markup)
