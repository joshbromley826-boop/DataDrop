import csv
from datetime import datetime
import os

CSV_FILE = "market_price_report.csv"


def save_historical_prices(scraped_items):
    file_exists = os.path.isfile(CSV_FILE)

    # Get current timestamp (e.g. 2026-10-02 12:48)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # Write header if the file doesn't exist yet
        if not file_exists:
            writer.writerow(["Timestamp", "Item", "Price"])

        for item in scraped_items:
            writer.writerow([timestamp, item["name"], item["price"]])

    print("Historical price entry appended to CSV.")