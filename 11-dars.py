son = int(input("Istalgan butun son kiriting: "))

for n in range(2,1111):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
