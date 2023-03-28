#Write a program for addition of tuples.
# Input
#tuple1 = (10, 4, 5)
#tuple2 = (2, 5, 18)
# Expected Output
#new_tuple = (12, 9, 23)

tuple1 = (10, 4, 5)
tuple2 = (2, 5, 18)
a = list(tuple1)
b = list(tuple2)
c = (a[0]+b[0],a[1]+b[1],a[2]+b[2])
print(tuple(c))