from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from google_sheets.courses import get_courses_names


@dp.message_handler(text="Информация по курсу 📚")
async def show_courses(message: types.Message):
    await message.answer("Ищу информацию о курсах 🔎")
    courses_names: list = get_courses_names()
    text: str = ""
    for courses_data in enumerate(courses_names):
        text += f"{courses_data[0] + 1}) {courses_data[1]}\nПодробнее: /course_{courses_data[0]}\n\n"
    await message.answer(
        text=text
    )


