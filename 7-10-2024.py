#combine list of strings into a single string without using join function
a=["learning"," ","python"," ","is"," ","very"," ","easy"]
b=""
for i in range(len(a)):
    b+=a[i]
print(b)

#1.Python Program to count occurrence of a given characters in string. 
S = "learning"
count = {}
for char in S:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
for char, count in count.items():
    print(f"{char} = {count}")


#2.Python Program to check if two Strings are Anagram. 
x=input("enter a string")
y=input("enter a string")
if(sorted(x)==sorted(y)):
    print("strings are anagrams")
else:
    print("strings are not anagrams")

#3.Python program to check a String is palindrome or not. 
s=input("eneter a string") 
if(s==s[::-1]):  
      print("The string  is a palindrome")  
else:  
      print("The string is not a palindrome")  

#4.Python program to replace the string space with a given character. 
s="learning python is very easy"
print(s.replace(" ","#"))

#5.Python program to replace the string space with a given character using replace() method. 
s1="python is very easy"
print(s1.replace(" ",'*'))


#6.Python program to convert lowercase char to uppercase of string. 
s2="learning"
print(s2.upper())

#7.Python program to check given character is digit or not using isdigit() method. 
s3="python123"
print(s3.isdigit())

#8.Python program to separate characters in a given string. 
s4 = "python"
print([*s4])

#9.Python program to remove blank space from string.
m1="   learning python  "
print(m1.replace(" ",""))
print(m1.strip())



#10.Python program to concatenate two strings using join() method.
s1="hi"
s2="hello"
print(' '.join([s1,s2]))

#11.Python program to concatenate two strings without using join() method. 
a="hello"
b="world"
print(a+b)

#12.Python program to remove repeated character from string. 
n="my name is gopichand"
print(set(n))

#13.Python program to count alphabets, digits and special characters. 
a=input("enter a string")
alphabets=digits=special_characters=0
for i in range(len(a)):
    if(a[i].isalpha()):
        alphabets = alphabets + 1
    elif(a[i].isdigit()):
        digits = digits + 1
    else:
        special_characters = special_characters + 1
print("total no.of alphabets",alphabets)
print("total no of digits",digits)
print("total npo.of special_characters",special_characters)

#14.Python program to check given character is digit or not. 
t=input("enter a character")
if(t>='0' and t<='9'):
    print("given character is digit")
else:
    print("given character is not digit")


#15.Python program to print all non repeating character in string. 
# Input string
string=input("enter a string")
for i in string:
    count=0
    for j in string:
        if i==j:
            count=count+1
        if count>1:
            break
    if count==1:
         print(i)

#16.Python program to copy one string to another string.
s1=input("enter a string")
s2=""
for i in range(len(s1)):
    s2=s2+s1[i]
print(s2)



#17.Python program to print the highest frequency character in a String.
string = "hello world"
frequency = {}
for i in string:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
max_char = ''
max_freq = 0
 
for i in frequency:
    if frequency[i] > max_freq:
        max_char = i
        max_freq = frequency[i]
print("The highest frequency character is:", max_char)



#18.Python program to calculate sum of integers in string.
s=input("enter a string")
total=0
for i in s:
    total=total+int(i)
print(total)