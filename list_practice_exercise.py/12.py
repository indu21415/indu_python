#Write a program to print the list of numbers which are greater than the average of numbers in the following list.
# Sample Input
#list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
# Expected Output
#[9, 13, 12, 7]

list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
b = len(list1)
#a = sum(list1)/10
a = sum(list1)/b
print(a)
z=[]
for i in list1:
    if i>=a:
        z.append(i)
print(z)
