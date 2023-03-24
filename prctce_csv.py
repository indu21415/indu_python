# f = open("data.csv","r")
# s = f.read()
# f.close()
# print(s)

      #-------male female ratio--------#
import csv

with open('data.csv', newline='\n') as csvfile:
    #  datareader = csv.reader(csvfile, delimiter=';', quotechar='|')
    #data extracted to data reader and retruns a reader object
    
    datareader = csv.reader(csvfile, delimiter=',')
    
    data_iter = iter(datareader)
    col_names = next(data_iter)

    csv_data = []

    for row in data_iter:
        csv_data.append(row)

print(col_names)
print(csv_data)
male = 0
female = 0
for i in csv_data:
   if i[4] == 'Male':
    male+=1
   elif i[4] == 'Female':
      female+=1

print('number of male count',male)
print('number of female count',female)
print('ratio',male/female)



   #-------population of countrys--------#



country_population = {}
for i in csv_data:
   if i[5] not in country_population:
      country_population [i[5]] = 1
   else:
      country_population [i[5]] += 1
print(country_population)

         #--------country with highest population#--------#


country_population = {}
for i in csv_data:
   if i[5] not in country_population:
      country_population [i[5]] = 1
   else:
      country_population [i[5]] += 1
country = max(country_population, key = lambda x : country_population[x])
print(country,country_population[country])