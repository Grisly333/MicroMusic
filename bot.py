from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
from config import TOKEN
#TOKEN = "8963655932:AAFx0Rrq7i7VtzvRq-M0lZO4_CTD92hL594"
bot = Bot(token=TOKEN)
dp = Dispatcher()
# Когда пользователь пишет /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Здравствуй мой госпадин")
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Я могу находить и включать тебе музыку.")
@dp.message(Command("about"))
async def cmd_about(message: types.Message):
    await message.answer("Наш проект называется MicroMusic ")
    await message.answer("Создан командой Alex team")
# Когда пользователь пишет любой текст
@dp.message()
async def get_name(message: types.Message):
    name = message.text
    await message.answer(f"благо, {name}! Рад тебя видеть.")
# Запуск бота
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
