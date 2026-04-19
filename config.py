# config.py

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Folders
DATA_PATH = os.path.join(BASE_DIR, "data")
REPORT_PATH = os.path.join(BASE_DIR, "reports")
LOG_PATH = os.path.join(BASE_DIR, "logs")

# Email settings
EMAIL_SENDER = "######@gmail.com"
EMAIL_PASSWORD = "####"
EMAIL_RECEIVER = "######@gmail.com"

# SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
