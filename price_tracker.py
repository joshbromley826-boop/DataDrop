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
import subprocess
import os

def push_updates_to_github():
    try:
        # Navigate to the project directory if necessary
        os.chdir(r"C:\Users\joshb\.codex")
        
        # Stage the updated CSV report
        subprocess.run(["git", "add", "market_price_report.csv"], check=True)
        
        # Commit changes (check=False avoids throwing an error if prices haven't changed)
        subprocess.run(["git", "commit", "-m", "Auto-update market price report"], check=False)
        
        # Push to main branch on GitHub
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Successfully pushed live price updates to GitHub Pages!")
        
    except Exception as e:
        print(f"Failed to push updates to GitHub: {e}")

# Call the function after your CSV is generated/updated
if __name__ == "__main__":
    # ... your price extraction logic here ...
    push_updates_to_github()