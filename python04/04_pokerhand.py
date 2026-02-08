def poker_hand(cards):
    # check if there is a pair
    values = [card[1] for card in cards]  # get all card values
    for value in values:
        if values.count(value) == 2:
            print(f"Du fick ett par med valören: {value}")
            return
    print("Inget par i handen")

# Test
hand = [
    ["hjärter", 5],
    ["spader", 5],
    ["ruter", 9],
    ["klöver", 11],
    ["hjärter", 2]
]
poker_hand(hand)  # Output: Du fick ett par med valören: 5