from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.course_data import course_data_markup, course_data_callback, get_back_markup
from loader import dp
from google_sheets.webinars import get_webinars_data
from states.course_data import GetCourseDataStates


@dp.message_handler(text="Бесплатный вебинар 🔥")
async def show_courses(message: types.Message, state: FSMContext):
    await message.answer("Ищу информацию о вебинарах 🔎")
    data = get_webinars_data()
    print(data)
    # data = get_courses_data()
    # await state.update_data(courses_data=data)
    # # courses_names: list = get_courses_names()
    # # print(data)
    # text: str = ""
    # for courses_data in enumerate(data):
    #     text += f"{courses_data[0] + 1}) {courses_data[1].name}\nПодробнее: /course_{courses_data[0] + 1}\n\n"
    # await message.answer(
    #     text=text,
    # )
    # await GetCourseDataStates.get_data.set()


