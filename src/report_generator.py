import os
import matplotlib.pyplot as plt
from config import REPORT_PATH

def generate_report(df):
    try:
        os.makedirs(REPORT_PATH, exist_ok=True)

        file_path = os.path.join(REPORT_PATH, "report.png")

        plt.figure()
        plt.bar(df["name"], df["value"])
        plt.title("Daily Report")
        plt.savefig(file_path)
        plt.close()

        return file_path

    except Exception as e:
        print("Report generation failed:", e)
        raise