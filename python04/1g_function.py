'''
1g Funktionen "isinstance" kan kontrollera en variabels datatyp. Vad gör funktionen is_number? Går det att förbättra koden?

def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(5.5))
print(is_number(42))
'''


#Answer:
#The function is checking whether the x is a float or an integer
#The function returns True if it is a float or a number
#The function will return True in both cases

#How can it be improved: I suggest to make it shorter like this:
def is_number(x):
    return isinstance(x, (int, float))
print(is_number(5.5)) #True
print(is_number(42))#True

#Second solution by using lambda
is_number02= lambda x: isinstance(x,(int,float))
print(is_number02(23.4))#True
print(is_number02(3))#True

#Third solution: by using map
values= [5.5, 42, "hello", None]
is_number03=list(map(lambda x:isinstance(x,(int,float)),values));
print(is_number03)
#[True, True, False, False]
