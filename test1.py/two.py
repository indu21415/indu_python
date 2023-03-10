a = []
for i in range(7):
    n = int(input())
    a.append(n)
print(a)
even = 0
for i in range(len(a)):
    if i%2 ==0:
        even+=a[i]

print(sum(a))
