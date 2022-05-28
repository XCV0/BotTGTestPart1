from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='')
dp = Dispatcher(bot)


@dp.message_handler(content_types=['text'])
async def main(message: types.Message):
    if message.text == '/start':
        await bot.send_message(message.from_user.id, 'Приветики ))')


if __name__ == '__main__':
    executor.start_polling(dp)