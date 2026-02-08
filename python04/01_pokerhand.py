''''
4 Pokerhand
När man spelar poker har man en hand med 5 kort, som man hoppas ska bli bättre än motståndarnas. Du ska bygga en funktion som kan utvärdera en pokerhand och tala om hur bra den är. Exempel på körning:
poker_hand(cards)
"Du fick ett par med valören: 5"

1 Bygg en funktion som slumpar ett spelkort. Den ska returnera en lista med två element: färg och valör. Färg kan vara: ruter, hjärter, spader eller klöver. Valör kan vara tvåa till ess, för enkelhets skull använder vi talen 2 till 14.
Exempel på ett kort: ["hjärter", 12]

2 Bygg en funktion som jämför två spelkort och kan tala om ifall de har samma valör.

3 Bygg första versionen av poker_hand(cards). Med hjälp av de andra funktionerna ska den ta reda på om man har ett par, dvs det finns två kort med samma valör.

Fortsätt att lägga till fler kontroller till funktionen.
Tips! Du kan göra en funktion som skriver ut kortvärdet snyggare:
pretty_print_card(["hjärter", 5]) → "hjärter fem"

Lista med pokerhänder.
Ett par (två lika kort)
Två par
Tretal (tre lika)
Straight (5 kort i följd, t.ex. 7-8-9-10-11)
Flush / färg (alla kort har samma färg)
Hus (par och tretal med olika valörer)
Fyrtal
Straight flush (5 kort i följd, med samma färg)
Femtal
'''
import random

def random_card():
    suits = ["ruter", "hjärter", "spader", "klöver"]  # colors
    values = list(range(2, 15))  # 2-14, where 14 = Ace
    suit = random.choice(suits)
    value = random.choice(values)
    return [suit, value]

# Test
print(random_card())  # Example output: ['spader', 11]