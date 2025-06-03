import os

BOT_TOKEN = os.getenv("7983775414:AAGLRF4MqvTJmxcfro0BCuVgiGv5kYSQH5E")

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

main_menu_keyboard = ReplyKeyboardMarkup(
    [
        ['💵 Валюти', '🧱 Матеріали'],
        ['📚 Джерело', '🔗 Посилання']
    ],
    resize_keyboard=True
)

back_keyboard = ReplyKeyboardMarkup(
    [['🔙 Назад']],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    await update.message.reply_text(
        f"👋 Привіт, {user_first_name}!\n"
        f"Вітаю, я бот-помічник:\n"
        f"Технології 3D друку!\n"
        "Оберіть розділ із меню нижче:",
        reply_markup=main_menu_keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == '💵 Валюти':
        await update.message.reply_text(
            "📈 Ціни на 3D друк:\n"
            "🇺🇸 Долар: $5–$20\n"
            "🇪🇺 Євро: 5€–25€\n"
            "🇺🇦 Гривня: 150–800 грн",
            reply_markup=back_keyboard
        )

    elif text == '🧱 Матеріали':
        await update.message.reply_text(
            "🧱 Популярні матеріали для 3D друку:\n\n"
            "🔹 PLA – легкий у використанні, біорозкладний\n"
            "🔹 ABS – міцний, жаростійкий\n"
            "🔹 PETG – гнучкий, прозорий\n"
            "🔹 TPU – еластичний, як гума\n"
            "🔹 Nylon – міцний та зносостійкий",
            reply_markup=back_keyboard
        )

    elif text == '📚 Джерело':
        await update.message.reply_text(
            "📚 Основна інформація взята з освітніх матеріалів курсів Coursera, "
            "YouTube-каналів про 3D-друк та статей на 3dnatives.com.",
            reply_markup=back_keyboard
        )

    elif text == '🔗 Посилання':
        await update.message.reply_text(
            "🔗 Корисні ресурси:\n"
            "🔸 https://3dnatives.com\n"
            "🔸 https://all3dp.com\n"
            "🔸 https://www.youtube.com/c/ThomasSanladerer\n"
            "🔸 https://reprap.org/wiki/Main_Page",
            reply_markup=back_keyboard
        )

    elif text == '🔙 Назад':
        await update.message.reply_text(
            "🔙 Ви повернулись до головного меню. Оберіть розділ:",
            reply_markup=main_menu_keyboard
        )

    else:
        await update.message.reply_text(
            "❓ Команду не розпізнано. Будь ласка, скористайтесь меню.",
            reply_markup=main_menu_keyboard
        )

def main():
    app = Application.builder().token("7983775414:AAGLRF4MqvTJmxcfro0BCuVgiGv5kYSQH5E").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("✅ Бот запущено...")
    app.run_polling()

if __name__ == '__main__':
    main()
