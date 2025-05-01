1)
from datetime import datetime

birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
today = datetime.today()

years = today.year - birthdate.year
months = today.month - birthdate.month
days = today.day - birthdate.day

if days < 0:
    months -= 1
    days += 30 


print(f"You are {years} years, {months} months, and {days} days old.")

2) from datetime import datetime, timedelta

birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
birth = datetime.strptime(birthdate, "%Y-%m-%d")
today = datetime.today()
next_birthday = datetime(today.year, birth.month, birth.day)

if next_birthday < today:
    next_birthday = datetime(today.year + 1, birth.month, birth.day)

days_left = (next_birthday - today).days
print(f"Days until your next birthday: {days_left}")

3)
from datetime import datetime, timedelta

current = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
hours = int(input("Enter meeting duration in hours: "))
minutes = int(input("Enter meeting duration in minutes: "))

start_time = datetime.strptime(current, "%Y-%m-%d %H:%M")
end_time = start_time + timedelta(hours=hours, minutes=minutes)

print("Meeting will end at:", end_time.strftime("%Y-%m-%d %H:%M"))

4)
from datetime import datetime
import pytz

from_zone = input("Enter your current timezone (e.g., Asia/Tashkent): ")
to_zone = input("Enter the timezone to convert to (e.g., Europe/London): ")
date_input = input("Enter date and time (YYYY-MM-DD HH:MM): ")

local = pytz.timezone(from_zone)
target = pytz.timezone(to_zone)
dt = local.localize(datetime.strptime(date_input, "%Y-%m-%d %H:%M"))
converted = dt.astimezone(target)

print("Converted time:", converted.strftime("%Y-%m-%d %H:%M"))

5)
from datetime import datetime
import time

target = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
future = datetime.strptime(target, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    remaining = future - now
    if remaining.total_seconds() <= 0:
        print("Time is up!")
        break
    print("Time remaining:", remaining, end="\r")
    time.sleep(1)
6)
import re

email = input("Enter your email address: ")

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")

7)

phone = input("Enter a 10-digit phone number: ")

if len(phone) == 10 and phone.isdigit():
    formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print("Formatted:", formatted)
else:
    print("Invalid phone number.")

8)
import re

password = input("Enter your password: ")

length = len(password) >= 8
uppercase = re.search(r'[A-Z]', password)
lowercase = re.search(r'[a-z]', password)
digit = re.search(r'\d', password)

if length and uppercase and lowercase and digit:
    print("Strong password.")
else:
    print("Weak password. Use at least 8 characters, include uppercase, lowercase, and digits.")

9)
text = "Python is powerful. Python is easy to learn. Python is fun!"
word = input("Enter the word to search for: ")

positions = [i for i in range(len(text)) if text[i:i+len(word)] == word]

if positions:
    print(f"Word found at positions: {positions}")
else:
    print("Word not found.")
10)
import re

text = input("Enter text containing dates: ")

pattern = r'\b(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})\b'
dates = re.findall(pattern, text)

if dates:
    print("Found dates:", dates)
else:
    print("No dates found.")
