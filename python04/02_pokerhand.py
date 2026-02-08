def same_value(card1, card2):
    return card1[1] == card2[1]

# Test
print(same_value(["hjärter", 5], ["spader", 5]))  # True
print(same_value(["hjärter", 5], ["spader", 7]))  # False