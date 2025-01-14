from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Чтение токена из файла
with open('token.txt', 'r') as file:
    TOKEN = file.read().strip()

# Ссылка для отправки
LINK = 'https://t.me/fedresurs_online'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправка ссылки по команде /start"""
    await update.message.reply_text(
        f'Привет! Вот ваша ссылка: {LINK}'
    )

def main():
    """Основной цикл работы бота"""
    if not TOKEN:
        raise ValueError("Токен отсутствует. Проверьте файл token.txt")

    app = ApplicationBuilder().token(TOKEN).build()

    # Обработка команды /start
    app.add_handler(CommandHandler("start", start))

    # Запуск бота
    app.run_polling()

if __name__ == '__main__':
    main()
