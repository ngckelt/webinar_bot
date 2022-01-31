from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


# Команда старт с кодом приглашения
@dp.message_handler(CommandStart(deep_link='invite_code'))
# @dp.message_handler(CommandStart(re.compile(r'regex'))))
async def bot_start_with_param(message: types.Message):
    args = message.get_args()
    # args - это invite_code

    invite_link = f'https://t.me{message.bot.me}?start={message.from_user.id}'

    await message.answer(f"Приветствую, {message.from_user.full_name}!"
                         f"Вы успешно добавлены в базу."
                         f"Используйте команду /help для получения справки")


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Бот недоступен."
                         f"Используйте реферальную ссылку или код приглашения")

