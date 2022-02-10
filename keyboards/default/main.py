from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Бесплатный вебинар 🔥")],
        [KeyboardButton("Информация по курсу 📚")],
        [KeyboardButton("Связаться с менеджером 📞")],
    ],
    resize_keyboard=True
)


