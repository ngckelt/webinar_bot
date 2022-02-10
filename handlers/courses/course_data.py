from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from google_sheets.courses import get_courses_names


@dp.message_handler(regexp=r"^course_(\d+)$")
async def show_courses(message: types.Message):
    course_index: int = int(message.text.split('_')[1])
