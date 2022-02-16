num = ['кабак', 'дом', 'мадам']


for i in num:
    a = i
    a = i[::-1]
    if a == i:
        print(f"Палиндром {a}")
    else:
        print(f"Не палиндром {a}")
    