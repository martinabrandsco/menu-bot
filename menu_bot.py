import os
import datetime
import pytz
import csv
import asyncio
from telegram import Bot
from dotenv import load_dotenv
import sys

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, '.env')

print(f"Looking for .env file at: {env_path}")
print(f"File exists: {os.path.exists(env_path)}")

# Load environment variables
load_dotenv(env_path)

# Telegram setup
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def get_current_week_and_day():
    madrid_tz = pytz.timezone('Europe/Madrid')
    now = datetime.datetime.now(madrid_tz)
    
    # Get the first day of the current month
    first_day = now.replace(day=1)
    
    # Calculate which week of the month we're in
    week_number = (now.day - 1) // 7 + 1
    print(f"Week number: {week_number}")
    
    # Get the day of the week (0 = Monday, 6 = Sunday)
    day_of_week = now.weekday()
    
    # Map weekday number to Spanish day name
    days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    day_name = days[day_of_week]
    
    return week_number, day_name

def get_todays_menu():
    # Get the current week and day
    current_week, current_day = get_current_week_and_day()
    
    # Read the CSV file
    csv_path = os.path.join(current_dir, 'menu-meri-gon.csv')
    todays_meals = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row['Week of the month']) == current_week and row['Day'] == current_day:
                    todays_meals.append(f"🕒 {row['Time']} - {row['Meal Type']}:\n{row['Description']}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return "Error reading menu file."
    
    if not todays_meals:
        return "No menu found for today."
    
    # Format the message
    message = f"🍽️ *Today's Menu - Semana {current_week} - {current_day}* 🍽️\n\n"
    message += "\n\n".join(todays_meals)
    return message

async def send_telegram_message():
    try:
        if not TELEGRAM_BOT_TOKEN:
            raise ValueError("TELEGRAM_BOT_TOKEN is not set in environment variables")
        
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        message = get_todays_menu()
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode='Markdown')
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")

async def main():
    print("\nSending today's menu...")
    await send_telegram_message()

if __name__ == "__main__":
    asyncio.run(main()) 