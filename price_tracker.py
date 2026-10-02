from datetime import datetime

# Get current time
last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
currency = "GBP"

import csv

print("Starting the data engine...")

# This data is built safely inside your own script
local_market_data = [
    {"Item Name": "Python Coding Basics", "Price": "£19.99"},
    {"Item Name": "Automated Web Scrapers", "Price": "£24.99"},
    {"Item Name": "Data Pipelines Made Easy", "Price": "£29.99"},
    {"Item Name": "Low-Stress Micro-SaaS Guide", "Price": "£14.99"}
]

file_name = "market_price_report.csv"
columns = ["Item Name", "Price"]

try:
    # This block forces your laptop to create the spreadsheet file
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(local_market_data)

    print("--------------------------------------------------")
    print(f"🎉 SUCCESS! Your file has been created successfully.")
    print(f"Look inside your folder for: {file_name}")
    print("--------------------------------------------------")

except Exception as e:
    print(f"An error occurred: {e}")
