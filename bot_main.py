from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import datetime
import os
from buttons import user_kb, user_inline_kb

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Bot has been started', reply_markup=user_kb)
    await message.answer('Check date', reply_markup=user_inline_kb)


@dp.message_handler(Text(equals='пожелание доброго утра', ignore_case=True))
async def good_morning(message: types.Message):
    await message.answer('Доброе утро!')


@dp.message_handler(Text(equals='пожелание доброй ночи', ignore_case=True))
async def good_night(message: types.Message):
    await message.answer('Доброй ночи!')


@dp.callback_query_handler(text='button_date')
async def date(callback_query: types.CallbackQuery):
    date_now = datetime.datetime.now()
    message = date_now.strftime('%d-%m-%Y %H:%M:%S')
    await bot.send_message(callback_query.from_user.id, message)

    await bot.answer_callback_query(callback_query.id, 'Hello')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
