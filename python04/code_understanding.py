'''
Läsa och förstå kod - diskutera i grupp
Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den.
Fick du samma resultat som du trodde? Om inte, varför?
'''
#1a
def foo(t):
    print("test")

foo("hej") #we assignsed a value here temporarily
#Explanation: The function requires one parameter, in this case the 't'. in that case we print 't' as test
#1b
def fun1(x, y):
    return x * y

print(3, 5)
#The function called fun1 has two parameters x and y.
# It returns the sum of x and y. We print the numbers 3,5 but not the actual sum of x and y
# we need something like: print(fun1(2,3) then it will print the sum of 2 and 3

#1c
def fun1(x, y):
    return x * y

print(fun1(3, 5))
#This function, also called fun1, has two parameters x and y.
#It will return the multiplication of x and y
#we want to print the function and assign the values to it

#1d
def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)
'''
The fun2 function has one parameter i
It returns i multiplied by 5
we then initialize two variables, a and y
then, we assign the return of the fun2 to a variable a (which can be replaced by a lambda instead)
The print will give as the fun2 with summary of fun2(5*2) + (5*3) = fun2(25)
a = fun2(25) = 5 * 25 = 125
'''

#1e
a = 5
def fun3(a):
    a += 1

a += 2
print(a)
'''
variable has a value 5
function 3 is taking the variable a and increase it by 1
then we call a and increase it by 2 
we print a at the end which will give the result: 7

'''
#1f
def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);
print(a)

'''
the function foo has a parameter i
it returns the value of i multiplied by 2 and its own value 

then there is a second function goo that takes two parameters
it returns x with y 

a = x(y)(2*i*i, 3)


'''