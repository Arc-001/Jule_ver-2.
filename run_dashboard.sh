#!/bin/bash

echo "Starting Jule Bot Admin Dashboard..."
echo "Access the dashboard at http://localhost:5000"
export FLASK_APP=dashboard.py
python3 -m flask run --host=0.0.0.0 --port=5000
