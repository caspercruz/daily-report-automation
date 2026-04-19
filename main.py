import os
import logging

from src.data_loader import load_data
from src.report_generator import generate_report
from src.email_sender import send_email
from config import LOG_PATH

# Ensure folders exist
os.makedirs(LOG_PATH, exist_ok=True)

# Logging setup
logging.basicConfig(
    filename=os.path.join(LOG_PATH, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run():
    try:
        logging.info("Automation started")

        df = load_data()
        logging.info("Data loaded successfully")

        report_path = generate_report(df)
        logging.info(f"Report generated: {report_path}")

        send_email(report_path)
        logging.info("Email sent successfully")

        logging.info("Automation completed")

    except Exception as e:
        logging.error(f"Automation failed: {str(e)}")
        print("Error:", e)

if __name__ == "__main__":
    run()