#functions
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.
#example:
def function():
    print("welcome to python")
function()

#add two numbers using functions
def add(x,y):
    return x+y
print(add(3,4))
#return statement :
#A return statement is used to end the execution of the function call and “returns” the result.
# The statements after the return statements are not executed.
 
 
#Write a Python program to create a dictionary from a string.  
# Note: Track the count of the letters from the string.
#Sample string : 'skywavessoftwares' using functions
def char_count(d):
    l=len(d)
    count={}
    for i in d:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count
d='skywavessoftwares'
print(char_count(d))

#Write a Python script to print a dictionary where the keys are numbers between
#  1 and 15 (both included) and the values are the square of the keys. using functions
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49,
 #8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
def square(squares):
    d1={}
    for i in range(1,16):
        d1[i] = i ** 2
    return d1
squares=15
print(square(squares))


#  Write a python program to  add a key to a dictionary ? using functions
def add_key_value(d, key, value):
    d[key] = value
    return d
d1 = {"name": "gopichand", "age": 24, "company_name": "skywaves"}
key = "salary"
value = 23000
result = add_key_value(d1, key, value)
print(result)

 


