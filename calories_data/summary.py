from db import get_user_data

def get_summary_text(user_id):
    user_data = get_user_data(user_id)
    
    if not user_data:
        return "Ваш дневник питания пока пуст."
    
    total_calories = sum(item.calories for item in user_data)
    
    summary_text = "Ваши приемы пищи сегодня:\n"
    for item in user_data:
        summary_text += f"- {item.food}: {item.calories} ккал\n"
    summary_text += f"\nОбщее количество калорий: {total_calories} ккал"
    
    return summary_text
