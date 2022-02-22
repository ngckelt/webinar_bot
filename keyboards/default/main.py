from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Информация об обучении")],
        [KeyboardButton("Бесплатные вебинары")],
        [KeyboardButton("Связь с менеджером")],
    ],
    resize_keyboard=True
)


