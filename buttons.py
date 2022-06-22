from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_button = KeyboardButton('Взял КБ 💼', callback_data='kb')
mail_button = KeyboardButton('Взял почту 📨', callback_data='mail')
sut_button = KeyboardButton('Взял девочку 👧', callback_data='sut')
ugon_button = KeyboardButton('Взял угон 🚗', callback_data='ugon')


def make_keyboard():
    return ReplyKeyboardMarkup().row(
        kb_button, mail_button
    ).add(sut_button).add(ugon_button)
