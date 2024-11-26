import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = '7661962661:AAH8zaO2qq0QZWwcEcNxyyydbMBfGOMLxNg'
bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("это команда старт!")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


    
async def main():
    await dp.start_polling(bot)

asyncio.run(main())