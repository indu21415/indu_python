#Write a program to sort the following employ data (list of tuples) as per their salaries (each tuple represents employ ID, name, age and salary)?
#data = [(1234, 'Abishek' , 32, 35000), (4532, 'Barathi', 27, 29000), (3455, 'Charan', 31, 37000), (9863, 'Devi', 42, 52000), (4852, 'Eswar', 37, 56000), (6481, 'Fathima', 40, 65000), (2793, 'Ganesh', 28,45000)]


data = [(1234, 'Abishek' , 32, 35000), 
        (4532, 'Barathi', 27, 29000), 
        (3455, 'Charan', 31, 37000), 
        (9863, 'Devi', 42, 52000), 
        (4852, 'Eswar', 37, 56000), 
        (6481, 'Fathima', 40, 65000), 
        (2793, 'Ganesh', 28, 45000)]
sort = sorted(data,key = lambda x : x[3])
for i in sort:
    print(i)