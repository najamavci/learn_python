
# 1. Function that prints "<name> är en fena på programmering"
def praise(name):
    print(f"{name} är en fena på programmering")


# 2a & 2b. Function "eko" with optional count parameter
def eko(text, count=2):
    print(text * count)


# 3. Multiply by 2 loop that stops after 5 iterations
def multiply_loop():
    y = 1
    for x in range(1, 100):
        y *= 2
        if x == 5:  # stop after 5 loops
            break
    print(y)


# 4. Function that returns the last element of a list
def last(lst):
    if lst:  # check if list is not empty
        return lst[-1]
    else:
        return None  # return None if the list is empty


# 5. Function that removes first and last element from a list
def cut_edges(lst):
    if len(lst) >= 2:
        return lst[1:-1]
    else:
        return []  # return empty list if too short


# 6. Fixed increase function
def increase(x):
    x += 1
    return x


# 7. Function that calculates the average of two numbers
def average(x, y):
    return (x + y) / 2


# 8. Pretty print a list
def pretty_print(lst):
    if not lst:
        print("Listan är tom.")
        return
    print(f"Listan har {len(lst)} element:")
    for i, item in enumerate(lst, start=1):
        print(f"{i}. {item}")