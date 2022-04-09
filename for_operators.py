guests = ['Ali','Vali','Hasan', 'Husan','Olim']
for guest in guests:
    print(guest)


    for gues in guests:
        print(f"Dear {gues}, we invite you to lunch on December 20th")

    print("Sincerely, Palonchiyev family")
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning squares {son**2} ")

    sonlar = list(range(11))  # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
    sonlar_kvadrati = []  # bo'sh ro'yxat yaratamiz
    for son in sonlar:  # sonlar dagi har bir son uchun
        sonlar_kvadrati.append(son ** 2)  # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz

    print(sonlar)
    print(sonlar_kvadrati)

friends = []  # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):  # n bu yerda 0 dan 4 gacha qiymatlar oladi
    friends.append(input(f"{n + 1}-enter your friend's name: "))
print(friends)

friend = ["Hasan","Husanjan","Ali","Nemat","Hilol"]
for frien in friend:

    print(f"SAlom {frien}")

print(f"Kod  return {len(friend)}   : ")


for num in range(10,100,1):
    print(num**2)

    # Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
    # va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar = []
print("5 ta sevimli kinoingiz qaysilar?")
for k in range(5):
    kinolar.append(input(f"{k + 1}-kino:"))
print(kinolar)

# With how many people from the user today
# Ask if you met (talked),
# and write on the list asking for the name of each person you talked to one by one. Upload the list to the console.
n_people = int(input("How many people did you talk to??>>>"))
names = []
for n in range(n_people):
    names.append(input(f"{n + 1}-Who was the person you talked to:: "))
print(names)







