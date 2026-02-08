'''
i En uppgift i tre delar:
Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
Rätta felen, så funktionen gör det den ska.

def find_min(numbers):
    counter = 0
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])

'''
def find_min(numbers):
    if not numbers:  # Handle empty list
        print("The list is empty.")
        return None

    counter = numbers[0]  # Start with the first number
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])

#The fixes:
#1. Handling the empty list
#2. Initialize the counter correctly
#3. looping through the numbers remins the same