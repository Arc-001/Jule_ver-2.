# Jule Discord Bot

A Discord bot that uses Google's Gemini AI to provide helpful responses and manage Minecraft server settings.

## How to Add the Bot to Your Server

### Step 1: Create a Discord Application
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and name your bot
3. Go to the "Bot" tab and click "Add Bot"
4. Under the bot's username, there's a "Token" section. Click "Copy" to copy your bot token
   (You'll need this for the `.env` file)

### Step 2: Configure Bot Permissions
1. In the "Bot" tab, scroll down to "Privileged Gateway Intents"
2. Enable:
   - Presence Intent
   - Server Members Intent 
   - Message Content Intent

### Step 3: Generate an Invite Link
1. Go to the "OAuth2" tab, then "URL Generator"
2. Select the following scopes:
   - `bot`
   - `applications.commands`
3. In the "Bot Permissions" section, select:
   - Read Messages/View Channels
   - Send Messages
   - Manage Messages
   - Embed Links
   - Attach Files
   - Read Message History
   - Manage Roles (if your bot needs to assign roles)
4. Copy the generated URL at the bottom of the page

### Step 4: Invite the Bot to Your Server
1. Paste the URL you copied into your web browser
2. Select the server you want to add the bot to
3. Click "Authorize"
4. Complete the CAPTCHA if prompted

### Step 5: Configure the Bot
1. Copy the `.env.example` file to create your own `.env` file:
   ```bash
   cp .env.example .env
   ```
2. Edit the `.env` file and add your Discord token, Gemini API key, and other configuration values:
   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   GEMINI_API_KEY=your_gemini_api_key_here
   # Fill in other values as needed
   ```

### Step 6: Install Dependencies and Run the Bot
1. Install required packages:
   ```
   pip install discord.py google-generativeai python-dotenv
   ```
2. Run the bot:
   ```
   python bot.py
   ```

## Features
- AI-powered conversations with Google's Gemini
- Role assignment for new users
- Minecraft Bedrock server management

## Setup

### Prerequisites

- Python 3.8+
- `discord.py` library
- `google.generativeai` library
- A Discord bot token
- Gemini API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Arc-001/Jule.git
   cd Jule
   ```

## Environment Variables

The bot uses the following environment variables that can be set in the `.env` file:

| Variable | Description | Example |
|----------|-------------|---------|
| DISCORD_TOKEN | Your Discord bot token | `abcd1234...` |
| GEMINI_API_KEY | Your Google Gemini API key | `AIza...` |
| BOT_PREFIX | Command prefix for the bot | `!` |
| GEMINI_MODEL | The Gemini model to use | `gemini-2.0-flash-exp` |
| SERVER_DIRECTORY | Path to Minecraft server directory | `/path/to/server` |
| SERVER_PROPERTIES | Path to server.properties file | `/path/to/server.properties` |
| SERVER_SERVICE | Name of the systemd service for the server | `minecraft-bedrock.service` |
| INTRO_CHANNEL_ID | ID of the channel for introductions | `1234567890123456789` |
| ADMIN_CHANNEL_ID | ID of the admin channel | `1234567890123456789` |
| GREETING_CHANNEL_ID | ID of the greeting channel | `1234567890123456789` |
| ADMIN_ROLE_ID | ID of the admin role | `1234567890123456789` |
| DEFAULT_ROLE_ID | ID of the default role | `1234567890123456789` |
| WELCOME_TITLE | Title for welcome embeds | `🌟 Welcome to Our Community! 🌟` |
| WELCOME_MESSAGE | Message body for welcome embeds | `Explore the channels...` |
| WELCOME_FOOTER | Footer text for welcome embeds | `Feel free to ask questions...` |
| ROLE_MAPPINGS | JSON mapping of role names to IDs | `{"role-name": 1234567890123456789}` |
