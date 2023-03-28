
# 2 .Write a program to count the number of even and odd numbers from a tuple of numbers.
# Input
#tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output:
#Number of even numbers: 5
#Number of odd numbers: 4

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count = 0
count1 = 0
for i in tuple1:
    if i%2 == 0:
        count+=1
    elif i%2 != 0:
        count1+=1
print("Number of even numbers",count)
print("number of odd",count1)
        
