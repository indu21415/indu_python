#Two lists are given below. Write a program to create a third list by picking an odd-index element from the first list and even index elements from second.
# Sample Input
#list1 = [3, 6, 9, 12, 15, 18, 21]
#list2 = [4, 8, 12, 16, 20, 24, 28]
# Expected Output
#list3 = [6, 12, 18, 4, 12, 20, 28]


list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
even = list1[1::2]
odd = list2[0::2]
even.extend(odd)

print(even)