from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.default.main import main_markup


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer(
        text="Привет! Я чат-бот АСИЗ, Академии №1 в России по обучению специалистов в области "
             "управления здоровьем и благополучием. 🌿 ",
        reply_markup=main_markup
    )

    await message.answer(
        text="Давайте я расскажу вам о наших курсах и бесплатных активностях? Подскажите, что вас интересует:\n"
             "Информация об обучении\n"
             "Бесплатные вебинары\n"
             "Связь с менеджером\n"
    )


