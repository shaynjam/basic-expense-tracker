# Basic Python Expense Tracker

## What This Is
This is a simple command-line Python script I built while learning the fundamentals of the language. It allows a user to type in daily expenses, categorizes them, and then calculates the total amount spent in each category.

## How It Works
* Uses a `while` loop to continuously ask the user for inputs until they choose to stop.
* Stores the inputs using a list of dictionaries.
* Uses nested loops to match categories together and add up the final costs.

## What I Learned Building This
This was a practice project to help me get comfortable with basic data structures and logic. The main hurdles I worked through were:

* **Using Classes:** This was my first time wrapping functions inside a "class" and using `self` to pass variables (like the main expense list) between different parts of the code.
* **Avoiding Data Overwrites:** I initially tried to use a standard dictionary, but realized multiple entries for the same category (like buying "Food" twice) would overwrite each other. I switched to a list of dictionaries to keep every entry separate.
* **The Loop Double-Counting Bug:** When adding up the totals, I accidentally created a bug where the loop would count the same items twice. I fixed this by creating a separate "tracker" list that records the index of an item once it has been counted, so the loop knows to skip it next time. 

## How to Run
1. Clone this repository.
2. Run `python expense_tracker.py` in your terminal.
3. Follow the text prompts to log your data!
