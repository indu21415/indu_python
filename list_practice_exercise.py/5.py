#Write a Python program to get the difference between the two lists.
# Sample Input
#list1 = [1, 2, 3, 4]
#list2 = [1, 2]
# Expected Output
#[3,4]

list1 = [1, 2, 3, 4]
list2 = [1, 2]
a = []
for i in list1:
    if i not in list2:
     a.append(i)
print(a)
