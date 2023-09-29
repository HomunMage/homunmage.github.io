import os
import datetime

def generate_file(directory, category, hour):
    """Generate markdown file in the specified directory with given category."""
    os.makedirs(directory, exist_ok=True)
    
    file_path = os.path.join(directory, f'{today_date}.md')
    with open(file_path, 'w') as file:
        file.write(f"""---
layout: default
categories: [{category}]
title:  "{category}"
date:   {today_date} {hour}:00:00 +0800
---
""")
    print(f"{category} file created at {file_path}!")

if __name__ == "__main__":
    # Get today's date
    today_date = datetime.date.today().strftime('%Y-%m-%d')
    
    # Define directories and corresponding categories
    directories_and_categories = {
        './Pitch/': 'Pitch',
        './Novel/': 'Novel',
        './Copywriting/': 'Copywriting',
        './GameDesign/': 'GameDesign'
    }

    start_hour = 8
    for dir_path, category in directories_and_categories.items():
        generate_file(dir_path, category, str(start_hour).zfill(2))
        start_hour += 1
