cars=['audi','bmw','volvo','gm','hyundai']




son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")





mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

for avto in cars:
        if(avto!='gm'):
            print(avto.upper())
        else:
            print(avto.title())

            names =  input("zapolnite:" )
            if names=='admin':  #
                print(f"Hi,  .  {names} Adminstrator.")

            else:
                print("Hello!",names)

                x = float(input("one number input: "))
                y = float(input("two number input:"))
                if x == y: print(f"number rowen: {x}={y}")

                kun = input("inpu day?")
                harorat = float(input("weather?"))
                if kun.lower() == 'weekend' and harorat >= 30:
                    print("yes")
                elif kun.lower() == 'weekend' and harorat < 30:
                    print("Stay Home!")
