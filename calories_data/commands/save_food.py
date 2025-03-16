from db import UserData, session

def save_food(message, bot):
    user_id = message.chat.id
    try:
        food, calories = message.text.split(',')
        food = food.strip()
        calories = int(calories.strip())
        if calories <= 0:
            raise ValueError("Калории должны быть положительным числом.")
        
        user_data = UserData(user_id=user_id, food=food, calories=calories)
        session.add(user_data)
        session.commit()
        bot.reply_to(message, f"Добавлено: {food} ({calories} ккал)")
    except ValueError as e:
        bot.reply_to(message, f"Пожалуйста, используйте правильный формат: еда, калории. Калории должны быть числом.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        bot.reply_to(message, "Произошла непредвиденная ошибка. Пожалуйста, попробуйте еще раз.")
