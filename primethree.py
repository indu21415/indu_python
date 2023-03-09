n = int(input("enter num:"))
i = 2
sqroot = int(n**0.5)
while i<=sqroot:
    if n%i == 0:
        print('not prime')
        break
    i+=1
else:
    print('prime')