from my_functions import (
    praise, eko, multiply_loop, last, cut_edges,
    increase, average, pretty_print
)

# 1.
praise("David")

# 2.
eko("hej")       # default 2 times
eko("hej", 3)    # 3 times

# 3.
multiply_loop()  # prints 32

# 4.
print(last([1, 2, 3]))  # 3

# 5.
print(cut_edges([1, 2, 3, 4]))  # [2, 3]

# 6.
print(increase(1))  # 2

# 7.
print(average(4, 8))  # 6

# 8.
pretty_print(["a", "b", 3.14])
pretty_print([])  # empty list example