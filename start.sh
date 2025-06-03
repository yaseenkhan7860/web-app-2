#!/bin/bash

# Print Python version
echo "Python version:"
python --version

# Print installed packages
echo "Installed packages:"
pip list

# Start the application
echo "Starting application..."
gunicorn app:app 