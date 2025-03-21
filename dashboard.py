from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_httpauth import HTTPBasicAuth
import os
import json
from dotenv import load_dotenv, set_key
from functools import wraps

app = Flask(__name__)
app.secret_key = os.urandom(24)
auth = HTTPBasicAuth()

# Default admin credentials - consider changing these or moving to environment variables
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "juleadmin"

# Path to the .env file
ENV_FILE = os.path.join(os.path.dirname(__file__), '.env')

@auth.verify_password
def verify_password(username, password):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return username

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            flash('You were successfully logged in')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def dashboard():
    # Load environment variables
    load_dotenv(ENV_FILE)
    
    # Group environment variables by category
    env_vars = {
        'Discord Bot Configuration': {
            'DISCORD_TOKEN': os.getenv('DISCORD_TOKEN', ''),
            'BOT_PREFIX': os.getenv('BOT_PREFIX', '!'),
            'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY', ''),
            'GEMINI_MODEL': os.getenv('GEMINI_MODEL', 'gemini-2.0-flash-exp')
        },
        'Server Configuration': {
            'SERVER_DIRECTORY': os.getenv('SERVER_DIRECTORY', '/home/mcserver/minecraft_bedrock'),
            'SERVER_PROPERTIES': os.getenv('SERVER_PROPERTIES', '/home/mcserver/minecraft_bedrock/server.properties'),
            'SERVER_SERVICE': os.getenv('SERVER_SERVICE', 'minecraft-bedrock.service')
        },
        'Channel IDs': {
            'INTRO_CHANNEL_ID': os.getenv('INTRO_CHANNEL_ID', ''),
            'ADMIN_CHANNEL_ID': os.getenv('ADMIN_CHANNEL_ID', ''),
            'GREETING_CHANNEL_ID': os.getenv('GREETING_CHANNEL_ID', '')
        },
        'Role IDs': {
            'ADMIN_ROLE_ID': os.getenv('ADMIN_ROLE_ID', ''),
            'DEFAULT_ROLE_ID': os.getenv('DEFAULT_ROLE_ID', '')
        },
        'Welcome Message Configuration': {
            'WELCOME_TITLE': os.getenv('WELCOME_TITLE', '🌟 Welcome to Our Community! 🌟'),
            'WELCOME_MESSAGE': os.getenv('WELCOME_MESSAGE', 'Explore the channels, make new connections, and enjoy your stay!'),
            'WELCOME_FOOTER': os.getenv('WELCOME_FOOTER', 'Feel free to ask questions or introduce yourself!')
        }
    }
    
    # Handle role mappings separately since it's JSON
    role_mappings = os.getenv('ROLE_MAPPINGS', '{}')
    try:
        role_mappings = json.loads(role_mappings)
    except json.JSONDecodeError:
        role_mappings = {}
    
    return render_template('dashboard.html', env_vars=env_vars, role_mappings=role_mappings)

@app.route('/update_env', methods=['POST'])
@login_required
def update_env():
    # Check if .env file exists, create it if not
    if not os.path.exists(ENV_FILE):
        open(ENV_FILE, 'a').close()
        print(f"Created new .env file at {ENV_FILE}")
    
    # Check if .env file is writable
    if not os.access(ENV_FILE, os.W_OK):
        flash('Error: .env file is not writable. Please check permissions.')
        print(f"Error: .env file at {ENV_FILE} is not writable")
        return redirect(url_for('dashboard'))

    # Load current environment variables
    load_dotenv(ENV_FILE)
    
    # Update environment variables from form
    success = True
    for key, value in request.form.items():
        if key != 'role_mappings':  # Handle role mappings separately
            try:
                set_key(ENV_FILE, key, value)
                print(f"Updated {key}={value} in .env file")
            except Exception as e:
                success = False
                print(f"Error setting {key}: {str(e)}")
                flash(f'Error updating {key}: {str(e)}')
    
    # Handle role mappings (from JSON)
    if 'role_mappings' in request.form:
        try:
            role_mappings = json.loads(request.form['role_mappings'])
            set_key(ENV_FILE, 'ROLE_MAPPINGS', json.dumps(role_mappings))
            print(f"Updated ROLE_MAPPINGS in .env file")
        except json.JSONDecodeError:
            success = False
            flash('Invalid JSON format for role mappings')
        except Exception as e:
            success = False
            print(f"Error setting ROLE_MAPPINGS: {str(e)}")
            flash(f'Error updating ROLE_MAPPINGS: {str(e)}')
    
    if success:
        flash('Environment variables have been updated')
    else:
        flash('Some environment variables could not be updated. Check the server logs for details.')
    
    return redirect(url_for('dashboard'))

@app.route('/restart_bot')
@login_required
def restart_bot():
    # Implement bot restart functionality here
    # This could be via systemctl, pm2, or another process manager
    # For example: os.system('systemctl restart jule-bot.service')
    flash('Bot restart requested')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
