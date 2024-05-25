from telegram.ext import Updater, CommandHandler
from handlers import start, eat_pizza, balance, shop, buy, use_power_up, leaderboard, achievements
from database import initialize_db

# Define your bot token (from BotFather)
TOKEN = '7043389751:AAEYCDhAgGyKrqXZVSTgYqEwJgWqDYQyKME'

def main() -> None:
    # Initialize the database
    initialize_db()

    # Set up the bot
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("eat_pizza", eat_pizza))
    dispatcher.add_handler(CommandHandler("balance", balance))
    dispatcher.add_handler(CommandHandler("shop", shop))
    dispatcher.add_handler(CommandHandler("buy", buy, pass_args=True))
    dispatcher.add_handler(CommandHandler("use_power_up", use_power_up))
    dispatcher.add_handler(CommandHandler("leaderboard", leaderboard))
    dispatcher.add_handler(CommandHandler("achievements", achievements))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
