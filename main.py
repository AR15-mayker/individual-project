import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("это команда старт!")


@dp.message(lambda message: message.text.lower() == "привет")
async def greet(message: types.Message):
    await message.answer("Привет! Как я могу помочь?")


@dp.message(lambda message: message.text.lower() == "как дела?")
async def how_are_you(message: types.Message):
    await message.answer("У меня всё хорошо, спасибо! А у тебя?")


@dp.message(lambda message: message.text.lower() == "пока")
async def goodbye(message: types.Message):
    await message.answer("До свидания! Возвращайся, если понадоблюсь!")


@dp.message(lambda message: message.text.lower() == "Разработчик")
async def greet(message: types.Message):
    await message.answer("разрабочик этого бота являеться : @AR_15_RUS ")


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
