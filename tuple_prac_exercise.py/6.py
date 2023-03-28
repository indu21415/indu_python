#Write a program to remove duplicates from tuple.
        #with using set#-------
t = (2,33,55,33,44,55,44,7,8,9,8,1)
a = set(t)
print(tuple(a))
 
          #without using set#--------------

t = (2,33,55,33,44,55,44,7,8,9,8,1)
a = []
for i in t:
    if i not in a:
        a.append(i)
print(tuple(a))