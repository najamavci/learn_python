"""
3a Write a program that tells today’s date.
Resource: Handling dates in Python

3b (harder) Modify the program so that it can tell what the date will be in 7 days.
"""
from datetime import date
from datetime import timedelta

today = date.today()
print(f"Today's date: {today}")
seventh_day=today + timedelta(7)
print(f"Week number: {seventh_day}")