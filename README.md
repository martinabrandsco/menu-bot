# Menu Bot

A Telegram bot that sends daily menu recommendations based on a CSV file. The bot runs automatically at 7 AM Madrid time.

## Features

- Reads menu from a CSV file
- Sends daily menu recommendations via Telegram
- Automatically determines current week and day
- Runs daily at 7 AM Madrid time using GitHub Actions

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/menu-bot.git
cd menu-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Telegram credentials:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

4. Set up GitHub Secrets:
   - Go to your repository settings
   - Navigate to Secrets and Variables > Actions
   - Add the following secrets:
     - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
     - `TELEGRAM_CHAT_ID`: Your Telegram chat ID

## CSV File Format

The menu CSV file should have the following columns:
- Week of the month
- Day (Lunes, Martes, Miércoles, etc.)
- Time
- Meal Type
- Description

## Running Locally

To run the bot locally:
```bash
python menu_bot.py
```

## GitHub Actions

The bot is configured to run automatically at 7 AM Madrid time using GitHub Actions. The workflow:
- Runs daily at 7 AM Madrid time
- Can be triggered manually using the "Run workflow" button
- Uses repository secrets for Telegram credentials

## License

MIT License 