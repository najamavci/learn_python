'''
3 Spelet 21
Om man lägger ihop talen 1 + 2 + 3 + 4 + …  så kommer talens summa att bli större och större. Förr eller senare kommer man förbi 21. Skriv en funktion som skriver ut det första talet i talserien som är större än 21.

Version 2: i stället för att använda talserien, slumpa tal mellan 1 och 13. (talen i en vanlig kortlek)
Tips: importera modulen random och använd funktionen randint för att slumpa tal.
Exempel: card = random.randint(1, 13)

Möjlig vidareutveckling: bygg ett spel som frågar användaren om man vill ta ett nytt kort eller stanna. (slumpa ett tal) Gör så att datorn kan simulera en motståndare. Målet är att vinna över datorn.

'''

# Step 1 - adding numbers 1, 2, 3 ...
def first_over_21():
    total = 0  # this will store the sum
    number = 0  # this is the current number we add

    while total <= 21:  # keep going until total is bigger than 21
        number += 1  # go to the next number
        total += number  # add it to total
    print("The first number that makes the sum bigger than 21 is:", number)

# Test it
first_over_21()