#sorting lists
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()

print(cars) #result ['audi', 'bmw', 'general motors', 'mercedes benz', 'tesla', 'volvo']
cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
cars.sort()
print(cars) #result ['Bmw', 'audi', 'gm', 'mercedes benz', 'tesla', 'volvo']
#obratno
cars.sort(reverse=True)
print(cars) #['volvo', 'tesla', 'mercedes benz', 'gm', 'audi', 'Bmw']
guest = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() return guest:", sorted(guest))
print("The original list remained unchanged:", guest)
#resut sorted() return guest: ['Avazbek', 'Farruh', 'Hamid', 'Odil', 'Shamsiddin', 'Temur']
#The original list remained unchanged: ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']

#reverse sorting
print(sorted(guest, reverse=True))
ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))
# result  [11, 12, 34, 34, 65, 76, 98]
#[98, 76, 65, 34, 34, 12, 11]

#Rotate the list
fruits = ['pear','banana','apple','watermelon','lemon']
fruits.reverse()
print(fruits)#['lemon', 'watermelon', 'apple', 'banana', 'pear']


#List length,
fruits = ['pear','banana','apple','watermelon','lemon']
print("Elements len:",len(fruits)) # len(fruits)  lists

#range function

sonlar = list(range(0,10)) #result [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sonlar)

#Even numbers
juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
print("Even numbers: ", juft_sonlar)
print("odd numbers: ", toq_sonlar)

narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("The cheapest price ", arzon, ". The most valuable ", qimmat, ". Jami: ", jami)



cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
print(my_cars)#result ['bmw']


numbers = [1, 2, 3, 4, 5] # numbers list created
numbers2 = numbers[:] # [:] numbers list full copy
numbers2.append(6) # numbers2 in 6 number addd
numbers2.append(7) # numbers2 in 7 number addd
print("This numbers list :", numbers)
print("This numbers2 list:", numbers2)# result This numbers list : [1, 2, 3, 4, 5]
#This numbers2 list: [1, 2, 3, 4, 5, 6, 7]

#Tuple list
number = (20, 30, 55.2)
print(number)

toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])

#toys[3] = 'dragon' result: TypeError: 'tuple' object does not support item assignment
toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) #We will make changes to the list(List) reverse
#We will make changes to the list
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Re-list the list (Tuple) reverse
print(toys)

capital  = ['Tadjikiestan','Uzbek', 'Germany', 'Usa', 'Arab']

print(sorted(capital))
print(sorted(capital,reverse=True))
print(capital)
print(capital.reverse())
#sort the list
capital.sort()
print(capital)


num=list(range(120,1200,2))
print(num[:20])
print(num[-20:])
print(num[530:550])
print(num)
print(sum(num))
print(min(num)-max(num))


#create a list of dishes and include any 5 dishes you want
dishes = ['osh','somsa','norin','shashlik','boiler']
breakfast= dishes[:]
breakfast.remove('norin')
breakfast.remove('shashlik')
breakfast.remove('boiler')
breakfast.append('non va qaymoq')
breakfast.append('bred')


breakfast = tuple(breakfast)




