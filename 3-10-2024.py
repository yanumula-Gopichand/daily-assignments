# s = "learning python is very easy"
 #output = "easy very is python learning"
#output = "ysae yrev si nohtyp gninrael"
s = "learning python is very easy"
print(s[::-1])
s = "learning python is very easy"
print(" ".join(s.split()[::-1]))


#s = "learning python is very easy"
#output = "learningpythonisveryeasy"

s = "learning python is very easy"
print(s.replace(" ", ""))

#s1 = "learning"
#output = l = 1
       # e = 1
        #a = 1
       # r = 1
       # n = 2
       # i = 1
       # g = 1

S = "learning"
count = {}
for char in S:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
for char, count in count.items():
    print(f"{char} = {count}")