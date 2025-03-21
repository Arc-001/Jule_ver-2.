import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Discord settings
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GREET_CHANNEL_ID = int(os.getenv("GREET_CHANNEL_ID"))
INTRO_CHANNEL_ID = int(os.getenv("INTRO_CHANNEL_ID"))
SERVER_ADMIN_CHANNEL_ID = int(os.getenv("SERVER_ADMIN_CHANNEL_ID"))
DEFAULT_ROLE_ID = int(os.getenv("DEFAULT_ROLE_ID"))
ADMIN_ROLE_ID = int(os.getenv("ADMIN_ROLE_ID"))

# Gemini settings
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

# Minecraft server settings
SERVER_DIRECTORY = os.getenv("SERVER_DIRECTORY", "/home/mcserver/minecraft_bedrock")
SERVER_PROPERTIES = f"{SERVER_DIRECTORY}/server.properties"
SERVER_SERVICE_NAME = os.getenv("SERVER_SERVICE_NAME", "minecraft-bedrock.service")

# Role mappings
ROLE_MAPPINGS = {
    "18-20": 1316707496974618644,
    "21-25": 1316707726780534795,
    "25-30": 1316707851363684354,
    "30-35": 1316707965990080522,
    ">35": 1316708075603759114,
    "he/him": 1316708175860338708,
    "she/her": 1316708329208156191,
    "they/them": 234567890123456789,
    "work": 1316708586344284211,
    "college": 1316708465602990100
}

# Check for required environment variables
def validate_env():
    missing_vars = []
    if not DISCORD_TOKEN:
        missing_vars.append("DISCORD_TOKEN")
    if not GEMINI_API_KEY:
        missing_vars.append("GEMINI_API_KEY")
    
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
