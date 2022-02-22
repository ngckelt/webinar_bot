from aiogram import types
from loader import dp
from keyboards.default.main import main_markup


@dp.message_handler(commands=["menu"])
async def main_menu(message: types.Message):
    await message.answer(
        text="Главное меню",
        reply_markup=main_markup
    )

