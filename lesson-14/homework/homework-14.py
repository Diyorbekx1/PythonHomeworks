# 1
import json

with open ('students.json', 'r') as file:
    students_data = json.load(file)


for student in students_data:
    print("Student Details:")
    for key, value in student.items():
        print(f"{key}: {value}")
    print(" " * 20) 

# 2
import requests

API_KEY = 'your_api_key_here'
city = 'Tashkent'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}appid={API_KEY}&units=metric'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"Weather in {city}")
    print("Temperature:", data["main"]["temp"], "C")
    print("Humidity:", data["main"]["humidity"], "%")
else:
    print("Error:", data.get("message", " wrong"))

# 3

[
    {"title": "48 LOWS OF POWER", "author": "ROBERT GREEN"},
    {"title": "The Alchemist", "author": "Paulo Coelho"}]

import json

def load_books():
    with open('books.json', 'r') as file:
        return json.load(file)

def save_books(books):
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

def add_book(title, author):
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)

def update_book(old_title, new_title, new_author):
    books = load_books()
    for book in books:
        if book['title'] == old_title:
            book['title'] = new_title
            book['author'] = new_author
    save_books(books)

def delete_book(title):
    books = load_books()
    books = [book for book in books if book['title'] != title]
    save_books(books)

# 4
import requests
import random

API_KEY = 'your_api_key_here'
genre_movies = {
    "action": ["SPIDERMAN", "John Wick"],
    "comedy": ["RUSH HOUR", "The Mask"],
    "drama": ["INTERSTELER",  "The Godfather"]
}

genre = input("Enter a movie genre (action/comedy/drama): ").lower()
if genre in genre_movies:
    movie_title = random.choice(genre_movies[genre])
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    
    if data['Response'] == 'True':
        print(f"\n {data['Title']} ({data['Year']})")
        print("Genre:", data['Genre'])
        print("IMDb Rating:", data['imdbRating'])
        print("Plot:", data['Plot'])
    else:
        print("Movie not found.")
else:
    print("Genre not found.")


