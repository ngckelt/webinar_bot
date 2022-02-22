from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.default.main import main_markup


@dp.message_handler(commands=["menu"], state="*")
async def main_menu(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text="Главное меню",
        reply_markup=main_markup
    )

