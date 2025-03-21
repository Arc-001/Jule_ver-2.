#!/bin/bash

echo "Installing Jule Discord Bot dependencies..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
else
    echo "Python 3 is already installed."
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing required packages..."
pip install discord.py google-generativeai python-dotenv
echo "Installing dependencies for Jule Discord Bot..."
pip install discord.py python-dotenv langchain-google-genai google-generativeai langchain
# Create .env file from template if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please edit the .env file to configure your bot settings."
else
    echo ".env file already exists."
fi

echo "Installation complete! Please configure your .env file before running the bot."
echo "You can run the bot using: ./run.sh"
