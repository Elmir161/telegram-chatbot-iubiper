# 🤖 IUBIPER — образовательный Telegram-бот

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![aiogram](https://img.shields.io/badge/aiogram-3.x-green)
![Mistral AI](https://img.shields.io/badge/Mistral%20AI-API-orange)

> Дипломный проект студента группы К4И2 Мамедова Эльмира

## 📌 О проекте

**Актуальность**: спрос на интеллектуальных помощников в образовании растёт на 15–20% в год.  
**Цель**: разработать чат-бота в Telegram для помощи учащимся в выполнении учебных заданий.  
**Стек**: Python, aiogram, Mistral AI, Telegram Bot API.

## 🧩 Функции

- Приём текстовых сообщений и анализ запросов.
- Генерация ответов через Mistral AI.
- Сохранение контекста диалога.
- Обработка команд `/start` и `/help`.
- Корректная реакция на некорректный ввод и пустые сообщения.

## 🏗️ Архитектура

Пользователь → Telegram → aiogram-бот → Mistral AI → ответ.

## 🚀 Быстрый старт

```bash
git clone https://github.com/ВАШ_ЛОГИН/IUBIPER-bot.git
cd IUBIPER-bot
python -m venv venv
source venv/bin/activate   # или venv\Scripts\activate на Windows
pip install -r requirements.txt
