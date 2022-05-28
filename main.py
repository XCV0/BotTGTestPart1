from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = ''
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(content_types=['text'])
async def main(message: types.Message):
    if message.text == '/start':
        await bot.send_message(message.from_user.id, 'Привет')
    if message.text.lower() == 'команды':
        await bot.send_message(message.from_user.id, 'Команды: как дела?')
    if message.text.lower() == 'как дела?':
        await bot.send_message(message.from_user.id, 'Нормально, у Вас?')
    else:
        await bot.send_message(message.from_user.id, 'Не понял Вас')

if __name__ == '__main__':
    executor.start_polling(dp)

