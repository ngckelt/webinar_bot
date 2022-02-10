from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.default.main import main_markup


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer(
        text="Приветсвеное меню. Выберите, что Вас интересует",
        reply_markup=main_markup
    )


