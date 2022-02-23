from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.course_data import course_data_markup, course_data_callback, get_back_markup
from loader import dp
from google_sheets.courses import get_courses_data
from states.course_data import GetCourseDataStates


@dp.message_handler(text="Информация об обучении")
async def show_courses(message: types.Message, state: FSMContext):
    await message.answer(
        text="Ищу информацию о курсах 🔎",
        reply_markup=types.ReplyKeyboardRemove()
    )
    data = get_courses_data()
    await state.update_data(courses_data=data)
    # courses_names: list = get_courses_names()
    # print(data)
    text: str = ""
    for courses_data in enumerate(data):
        text += f"{courses_data[0] + 1}) {courses_data[1].name}\nПодробнее: /course_{courses_data[0] + 1}\n\n"
    await message.answer(
        text=text,
    )
    await GetCourseDataStates.get_data.set()


@dp.callback_query_handler(course_data_callback.filter(option="get_back"), state=GetCourseDataStates.get_data)
async def get_back(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.answer()
    state_data = await state.get_data()
    courses_data = state_data.get("courses_data")
    course_index: int = int(callback_data.get("course_index"))
    course = courses_data[course_index]
    await callback.message.edit_text(
      text=course.description,
      reply_markup=course_data_markup(course_index, course.payment_link)
    )


@dp.message_handler(regexp=r"^/course_(\d+)$", state=GetCourseDataStates.get_data)
async def show_course_data(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    courses_data = state_data.get("courses_data")
    course_index: int = int(message.text.split('_')[1]) - 1
    try:
        course = courses_data[course_index]
        await message.answer(
          text=course.description,
          reply_markup=course_data_markup(course_index, course.payment_link)
        )
    except:
        await message.answer("Указано неверное значение")


@dp.callback_query_handler(course_data_callback.filter(option="price"), state=GetCourseDataStates.get_data)
async def show_course_price(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    state_data = await state.get_data()
    courses_data = state_data.get("courses_data")
    course_index: int = int(callback_data.get("course_index"))
    course = courses_data[course_index]
    await callback.message.edit_text(
        text=course.price,
        reply_markup=get_back_markup(course_index)
    )


@dp.callback_query_handler(course_data_callback.filter(option="format"), state=GetCourseDataStates.get_data)
async def show_course_format(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    state_data = await state.get_data()
    courses_data = state_data.get("courses_data")
    course_index: int = int(callback_data.get("course_index"))
    course = courses_data[course_index]
    await callback.message.edit_text(
        text=course.format,
        reply_markup=get_back_markup(course_index)
    )


@dp.callback_query_handler(course_data_callback.filter(option="payment_link"), state=GetCourseDataStates.get_data)
async def show_course_price(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    state_data = await state.get_data()
    courses_data = state_data.get("courses_data")
    course_index: int = int(callback_data.get("course_index"))
    course = courses_data[course_index]
    await callback.message.edit_text(
        text="Оплата происходит только через менеджера",
        reply_markup=get_back_markup(course_index)
    )

