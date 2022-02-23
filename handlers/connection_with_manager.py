from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.main import main_markup
from keyboards.inline.course_data import course_data_callback
from loader import dp
from keyboards.default.get_phone import get_phone_markup
from states.connection_with_managers import ConnectionWithManagerStates
from states.course_data import GetCourseDataStates


@dp.callback_query_handler(course_data_callback.filter(option="connect_with_manager"), state=GetCourseDataStates.get_data)
async def connection_with_manager_by_inline_button(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(
        text="Напишите, пожалуйста, как вас зовут 📲",
        reply_markup=types.ReplyKeyboardRemove()
    )
    await ConnectionWithManagerStates.get_name.set()


@dp.message_handler(text="Связь с менеджером")
async def connection_with_manager(message: types.Message):
    await message.answer(
        text="Напишите, пожалуйста, как вас зовут 📲",
        reply_markup=types.ReplyKeyboardRemove()
    )
    await ConnectionWithManagerStates.get_name.set()


@dp.message_handler(state=ConnectionWithManagerStates.get_name)
async def get_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer(
        text="Отправьте номер телефона, по которому менеджер АСИЗ может вам перезвонить",
        reply_markup=get_phone_markup
    )
    await ConnectionWithManagerStates.get_phone.set()


async def finish_connection(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    name = state_data.get("name")
    phone = state_data.get("phone")
    await message.answer(
        text="Данные успешно отправлены менеджеру",
        reply_markup=main_markup
    )
    await state.finish()


@dp.message_handler(content_types=types.ContentTypes.CONTACT, state=ConnectionWithManagerStates.get_phone)
async def get_phone(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone=phone_number)
    await finish_connection(message, state)


@dp.message_handler(state=ConnectionWithManagerStates.get_phone)
async def get_phone(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone=phone_number)
    await finish_connection(message, state)

