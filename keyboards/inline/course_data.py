from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

course_data_callback = CallbackData("course_data", "course_index", "option")


def course_data_markup(course_index: int, payment_link: str):
    markup = InlineKeyboardMarkup(row_width=2)
    if payment_link.startswith("http"):
        payment_link_button = InlineKeyboardButton(
            text="Ссылка на оплату",
            url=payment_link
        )
    else:
        payment_link_button = InlineKeyboardButton(
            text="Оплата через менеджера",
            callback_data=course_data_callback.new(course_index, "payment_link"),
        )
    markup.add(
        InlineKeyboardButton(
            text="Цена",
            callback_data=course_data_callback.new(course_index, "price"),
        ),
        InlineKeyboardButton(
            text="Формат",
            callback_data=course_data_callback.new(course_index, "format"),
        ),
        payment_link_button,
        InlineKeyboardButton(
            text="Связаться с менеджером",
            callback_data=course_data_callback.new(course_index, "connect_with_manager"),
        ),
    )
    return markup


def get_back_markup(course_index):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(
            text="Назад",
            callback_data=course_data_callback.new(course_index, "get_back"),
        )
    )
    return markup
