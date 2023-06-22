import os
from datetime import date

# Get today's date
today = date.today()

# Format the date as YYYY-MM-DD
date_str = today.strftime("%Y-%m-%d")

# Create the folder
folder_name = f"Folder_{date_str}"
os.makedirs(folder_name)

print(f"Folder '{folder_name}' created successfully.")
