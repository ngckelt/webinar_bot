from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


def webinar_link_markup(payment_link: str):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton(
            text="Ссылка на вебинар",
            url=payment_link
        )
    )
    return markup

