from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.webinars_data import webinar_link_markup
from loader import dp
from google_sheets.webinars import get_webinars_data
from states.webinars_data import GetWebinarDataStates


@dp.message_handler(text="Бесплатный вебинар 🔥")
async def show_courses(message: types.Message, state: FSMContext):
    await message.answer(
        text="Ищу информацию о вебинарах 🔎",
        reply_markup=types.ReplyKeyboardRemove()
    )
    webinars_data = get_webinars_data()
    print(webinars_data.quantity)
    for webinar in webinars_data.webinars:
        print(webinar)
    await message.answer(
        text=webinars_data.description
    )
    await state.update_data(webinars_data=webinars_data)
    await GetWebinarDataStates.get_data.set()


@dp.message_handler(state=GetWebinarDataStates.get_data)
async def get_webinar_number(message: types.Message, state: FSMContext):
    webinar_numer = message.text
    if webinar_numer.isdigit():
        state_data = await state.get_data()
        webinars_data = state_data.get("webinars_data")
        try:
            webinar = webinars_data.webinars[int(webinar_numer) - 1]
            await message.answer(
                text=webinar.description,
                reply_markup=webinar_link_markup(webinar.link)
            )
        except:
            await message.answer("Недопустимое значение числа")
    else:
        await message.answer("Необходимо ввести цифру")


