#list1 = [1, 2, 3, 4]
#list2 = [1, 2]
#if list1!=list2
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
a=(list1[1::2])
b=(list2[0::2])
a.extend(b)
print(a)
