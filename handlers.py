from telegram import Update
from telegram.ext import CallbackContext
from database import get_user_data, update_user_data, get_power_up, award_achievement

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if not get_user_data(user_id):
        update_user_data(user_id, 10)
    update.message.reply_text("Welcome to Pizza Game! You received 10 coins as a welcome bonus. Type /eat_pizza to start earning more coins!")

def eat_pizza(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user = get_user_data(user_id)
    
    coins_earned = 1  # Coins per click
    user['coins'] += coins_earned
    update_user_data(user_id, user['coins'])

    # Check for achievements
    if user['coins'] >= 100:
        award_achievement(user_id, '100 Coins')
    
    update.message.reply_text(f"You ate a slice of pizza! +{coins_earned} coin. Total coins: {user['coins']}")

def balance(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user = get_user_data(user_id)
    update.message.reply_text(f"Your current balance is {user['coins']} coins.")

def shop(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Shop: 1. Double Coins (10 minutes) - 50 coins. 2. Auto-Clicker (5 minutes) - 100 coins. Type /buy [item number] to purchase.")

def buy(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user = get_user_data(user_id)
    item = context.args[0]

    if item == "1" and user['coins'] >= 50:
        user['coins'] -= 50
        conn = sqlite3.connect('pizza_game.db')
        c = conn.cursor()
        c.execute('INSERT OR REPLACE INTO power_ups (user_id, power_up, duration) VALUES (?, ?, ?)', (user_id, 'double_coins', 10))
        conn.commit()
        conn.close()
        update_user_data(user_id, user['coins'])
        update.message.reply_text("You bought Double Coins! Use /use_power_up to activate it.")
    elif item == "2" and user['coins'] >= 100:
        user['coins'] -= 100
        conn = sqlite3.connect('pizza_game.db')
        c = conn.cursor()
        c.execute('INSERT OR REPLACE INTO power_ups (user_id, power_up, duration) VALUES (?, ?, ?)', (user_id, 'auto_clicker', 5))
        conn.commit()
        conn.close()
        update_user_data(user_id, user['coins'])
        update.message.reply_text("You bought Auto-Clicker! Use /use_power_up to activate it.")
    else:
        update.message.reply_text("You don't have enough coins for that item.")

def use_power_up(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    power_up = get_power_up(user_id)
    if power_up:
        power_up_name, duration = power_up
        if power_up_name == "double_coins":
            coins_earned = 2  # Double the coins
        else:
            coins_earned = 1
    else:
        coins_earned = 1  # Normal coin earning rate

    user = get_user_data(user_id)
    user['coins'] += coins_earned
    update_user_data(user_id, user['coins'])
    update.message.reply_text(f"You used a {power_up_name} power-up! +{coins_earned} coins per click. Total coins: {user['coins']}")

def leaderboard(update: Update, context: CallbackContext) -> None:
    conn = sqlite3.connect('pizza_game.db')
    c = conn.cursor()
    c.execute('SELECT user_id, coins FROM users ORDER BY coins DESC LIMIT 10')
    top_users = c.fetchall()
    conn.close()
    
    leaderboard_message = "Top Players:\n"
    for i, (user_id, coins) in enumerate(top_users, start=1):
        leaderboard_message += f"{i}. User {user_id} - {coins} coins\n"
    
    update.message.reply_text(leaderboard_message)

def achievements(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    conn = sqlite3.connect('pizza_game.db')
    c = conn.cursor()
    c.execute('SELECT achievement FROM achievements WHERE user_id = ?', (user_id,))
    user_achievements = c.fetchall()
    conn.close()
    
    if user_achievements:
        achievements_message = "Your Achievements:\n"
        for (achievement,) in user_achievements:
            achievements_message += f"- {achievement}\n"
    else:
        achievements_message = "You have no achievements yet."
    
    update.message.reply_text(achievements_message)
