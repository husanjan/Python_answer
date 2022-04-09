
fruits = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
price = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
number = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
name = [] # bo'sh ro'yxat

print("Birinchi Fruits: ", fruits[0])
print("Ikkinchi Fruits: ", fruits[1])
print("Birinchi meva: ", fruits[0].title())
print("Ikkinchi meva: ", fruits[1].upper())
print(price[2] + price[3])

fruits.append("tarvuz") # mevalar ga tarvuz qo'shamiz
print(fruits)


del fruits[1] # 2-element (anjir) ni o'chirib tashlaymiz
print(fruits)

fruits.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
print(fruits)
#Car lists
car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
print(car_models[-1])

cars = [] # bo'sh ro'yxat yaratamiz
cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
print(cars)

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)


names=["Shohruh","Huseyn","Naim"]
print(f"Salom {names[0]} , bugun choyxona bormi \n  Salom {names[1]} , bugun choyxona bormi \n  Salom {names[2]} , bugun choyxona bormi  ")

numbers=[10,20,-23,-33,90]
print(numbers)
numbers[0]=20
numbers[1]=10
print(numbers)
print(numbers[1]+numbers[0])

t_shaxslarva =["Sariq dev","Muhammad Ali","Yusuf","Bill Gates","Ilon Mask"]

z_shaxslar=["Imom Buxoriy","Paygambarimiz Muhammad S.A.V"]

print(f"Men tarixiy Shaxslardan {z_shaxslar[1]} {z_shaxslar[0]} \n Zamonaviy shaxslardan esa {t_shaxslarva[0]} suhbat qilishni istar edim")
friends=[]
friends.append("Hsueyn")
friends.append("Ali")
friends.append("Oybek")

friends.append("Shohruh")
print(friends)
friends.append('Hasan')
friends.insert(0, 'Husan')
friends.insert(2, 'Ivan')
print(friends)
