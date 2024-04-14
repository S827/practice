import random

def select_random_item(my_list):
    if len(my_list) > 0:
        random_item = random.choice(my_list)
        return random_item
    else:
        return 'List is Empty'

beginner_projects = [
    "To-Do List Application",
    "Simple Calculator",
    "Weather App",
    "Random Quote Generator",
    "BMI Calculator",
    "Countdown Timer",
    "Basic Form Validator",
    "Simple Quiz Game",
    "Currency Converter",
    "Basic Blogging Platform",
    "Number Guessing Game",
    "Text-Based Adventure Game",
    "Unit Converter",
    "Hangman Game",
    "Tic-Tac-Toe Game",
    "Basic Image Viewer",
    "File Renaming Tool",
    "Password Generator",
    "Contact Book",
    "Simple Drawing App",
    "URL Shortener",
    "Word Counter",
    "Alarm Clock",
    "Simple Music Player",
    "Email Slicer"
]



random_item = select_random_item(beginner_projects)

print("Randomly Selected Project is: ", random_item)
