import os
import asyncio
import logging
from mistralai import Mistral
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not MISTRAL_API_KEY or not TELEGRAM_TOKEN:
    raise ValueError("Отсутствуют переменные окружения: MISTRAL_API_KEY или TELEGRAM_TOKEN")

model = "mistral-large-latest"
client = Mistral(api_key=MISTRAL_API_KEY)

chat_history = {}

logging.basicConfig(level=logging.INFO)
bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        'Привет! Я — IUBIPER. Меня разработал студент группы К4И2 Мамедов Эльмир в рамках дипломной работы. Спрашивай что угодно — помогу и с рецептом блинов, и с написанием сложного кода!'
    )

@dp.message(F.text)
async def filter_messages(message: types.Message):
    chat_id = message.chat.id
    if chat_id not in chat_history:
        chat_history[chat_id] = [
            {"role": "system", "content": "Ты полезный ассистент, отвечай кратко и по делу."}
        ]
    chat_history[chat_id].append({"role": "user", "content": message.text})
    chat_response = client.chat.complete(model=model, messages=chat_history[chat_id])
    response_text = chat_response.choices[0].message.content
    chat_history[chat_id].append({"role": "assistant", "content": response_text})
    if len(chat_history[chat_id]) > 10:
        chat_history[chat_id] = [chat_history[chat_id][0]] + chat_history[chat_id][-9:]
    await message.answer(response_text, parse_mode="Markdown")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
