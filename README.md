# Pizza Game Bot

A simple Telegram bot game where players click to eat pizza and earn coins.

## Setup

1. Clone the repository.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Telegram bot token in `main.py`:
   ```python
   TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
   ```
4. Initialize the database:
   ```bash
   python main.py
   ```
5. Start the bot:
   ```bash
   python main.py
   ```

## Commands

- `/start` - Start the game and receive a welcome bonus.
- `/eat_pizza` - Click to eat pizza and earn coins.
- `/balance` - Check your current coin balance.
- `/shop` - View available power-ups in the shop.
- `/buy [item number]` - Purchase a power-up from the shop.
- `/use_power_up` - Use a purchased power-up.
- `/leaderboard` - View the top players.
- `/achievements` - View your achievements.
