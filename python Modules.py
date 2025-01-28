'''
import os
import os.path

# 1. List contents of Downloads folder
downloads_path = os.path.expanduser("~/Downloads") 

try:
    for item in os.listdir(downloads_path):
        item_path = os.path.join(downloads_path, item)
        if os.path.isfile(item_path):
            print(f"{item} - File")
        elif os.path.isdir(item_path):
            print(f"{item} - Folder")
        else:
            print(f"{item} - Unknown")
except FileNotFoundError:
    print("Downloads folder not found.")
'''

# 2. Print all ASCII letters
import string

print("ASCII Letters:", string.ascii_letters)

# 3. Randomly sample five letters
from random import sample

five_letters = ''.join(sample(string.ascii_letters, 5))
print("Five Random Letters:", five_letters)

from datetime import datetime, timedelta
import random
import calendar
'''
# 4. Date Manipulation

def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        day_of_week = calendar.day_name[date_obj.weekday()]
        formatted_date = f"{day_of_week} {date_obj.day} {date_obj.strftime('%B')} {date_obj.year}"
        return formatted_date, day_of_week
    except ValueError:
        return "Invalid date format. Please use dd/mm/yyyy."

def add_time_to_date(date_str, days, hours):
    try:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        new_date = date_obj + timedelta(days=days, hours=hours)
        return new_date.strftime("%d/%m/%Y")
    except ValueError:
        return "Invalid date format. Please use dd/mm/yyyy."

def get_date_after_months(months):
    today = datetime.today()
    new_date = today + relativedelta(months=months)
    return new_date.strftime("%d/%m/%Y")
'''

# 5. Rock Paper Scissors

def play_rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    while True:
        user = input("Enter your choice (rock, paper, scissors): ").lower()
        if user not in options:
            print("Invalid choice. Please choose from rock, paper, or scissors.")
            continue

        computer = random.choice(options)
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a draw!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("You win!")
            break
        else:
            print("Computer wins!")
            break



play_rock_paper_scissors()
