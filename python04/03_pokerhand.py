def pretty_print_card(card):
    value_names = {
        11: "knekt",
        12: "dam",
        13: "kung",
        14: "ess"
    }
    value = value_names.get(card[1], str(card[1]))  # use name if 11-14, else number
    return f"{card[0]} {value}"

# Test
print(pretty_print_card(["hjärter", 5]))  # hjärter 5
print(pretty_print_card(["spader", 12]))  # spader dam