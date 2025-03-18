Fitness Tracker

📌 Overview

This project tracks user fitness activity using Google Fit API, storing step count data in MySQL and exporting reports to Google Sheets and Tableau. It also automates data updates every 3 hours.

🔹 Features

Fetches step count from Google Fit

Stores data in MySQL database

Exports data to CSV, Excel, and Google Sheets

Visualizes data using Tableau

Automates updates using cron jobs

📥 Installation

# Clone the repository
git clone https://github.com/yourusername/fitness-tracker.git
cd fitness-tracker

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

🔑 Google API Setup

Create a Google Cloud Project

Enable Google Fit API

Download OAuth credentials.json

Place it in the project root
