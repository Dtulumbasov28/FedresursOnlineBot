from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Вставь свой токен сюда
TOKEN = '7653125508:AAEfrNgm5g9mEu77n539I3j0GCuF-dFMgcE'

# Ссылка для отправки
LINK = 'https://t.me/fedresurs_online'  # Замените на вашу ссылку

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправка ссылки при запуске команды /start"""
    await update.message.reply_text(f'Привет! Вот ваша ссылка: {LINK}')

def main():
    """Основной цикл работы бота"""
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Обработка команды /start
    app.add_handler(CommandHandler("start", start))
    
    # Запуск бота
    app.run_polling()

if __name__ == '__main__':
    main()
