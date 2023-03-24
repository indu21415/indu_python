#Write a program to print a new list containing squares of each element in the following list.
# Sample Input
#list1 = [3, 7, 11, 12, 17, 21]
# Expected Output
#list2 = [9, 49, 121, 144, 289, 441]

list1 = [3, 7, 11, 12, 17, 21]
a = []
for i in list1:
    b = i * i
    a.append(b)
print(a)
