#!/bin/bash

echo "=== Jule Discord Bot Configuration ==="
echo "This script will help you set up your bot's configuration."
echo "Please provide the following information:"
echo ""

# Prompt for Discord bot token
read -p "Discord Bot Token: " DISCORD_TOKEN

# Prompt for Google Gemini API key
read -p "Google Gemini API Key: " GEMINI_API_KEY

# Prompt for bot prefix with default
read -p "Bot Command Prefix (default: !): " BOT_PREFIX
BOT_PREFIX=${BOT_PREFIX:-!}

# Create the .env file
cat > .env.new << EOL
# Discord Bot Configuration
DISCORD_TOKEN=${DISCORD_TOKEN}
BOT_PREFIX=${BOT_PREFIX}

# Google Gemini API Configuration
GEMINI_API_KEY=${GEMINI_API_KEY}
EOL

# Check if .env already exists and create backup if needed
if [ -f ".env" ]; then
    echo "Backing up existing .env file to .env.backup"
    cp .env .env.backup
fi

# Move the new config file to .env
mv .env.new .env

echo ""
echo "Configuration complete! Your .env file has been created."
echo "You can edit this file manually anytime at: $(pwd)/.env"
echo ""
echo "You can now run the bot using: ./run.sh"
