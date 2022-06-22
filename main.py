import asyncio

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from datetime import datetime

from buttons import make_keyboard

bot = Bot(token='5330702714:AAEijBWtU3DVFW0WQEenrfHCgU1mQwUYSxY')
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message: types.Message):
    keyboard = make_keyboard()
    print(message.text.split())
    text = ''
    timer = 0

    if len(message.text.split()) >= 2:
        command = message.text.split()[1]
        if command == 'КБ':
            timer = 60 * 4
            text = 'КБ 💼'
        elif command == 'почту':
            timer = 60 * 10
            text = 'Почта 📨'
        elif command == 'девочку':
            timer = 60 * 90
            text = 'Девочка 👧'
        elif command == 'угон':
            timer = 60 * 90
            text = 'Угон 🚗'

        msg = await bot.send_message(text=f'{text}: {timer} секунд', chat_id=message.chat.id,
                                     reply_markup=types.InlineKeyboardMarkup())

        start_time = datetime.now()

        while (datetime.now() - start_time).seconds < timer:
            await asyncio.sleep(5)
            if (datetime.now() - start_time).seconds >= timer:
                await msg.edit_text(f'{text}: 0 секунд',
                                    reply_markup=types.InlineKeyboardMarkup())
            else:
                await msg.edit_text(f'{text}: {timer - (datetime.now() - start_time).seconds} секунд',
                                    reply_markup=types.InlineKeyboardMarkup())

        if text == 'Девочка 👧':
            await bot.send_message(text=f'{text} откатилась', chat_id=message.chat.id,
                                   reply_markup=types.InlineKeyboardMarkup())
        else:
            await bot.send_message(text=f'{text} откатилось', chat_id=message.chat.id,
                                   reply_markup=types.InlineKeyboardMarkup())
    else:
        await bot.send_message(text='Вот твоя клавиатура', chat_id=message.chat.id, reply_markup=keyboard)


executor.start_polling(dp, skip_updates=True)
