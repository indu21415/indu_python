#Write a Python program to find the second smallest number in a list.
# Sample Input
#list1 = [1, 2, -8, -2, 0]
# Expected Output
#-2

list1 = [1,2,-8,-2,0]
list1.sort()
print(list1)
print(list1[1])