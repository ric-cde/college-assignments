parking_length = float(input("How long are you parking for? (hours) "))

if parking_length <= 2:
    print("It's free!")
else:
    price = int(parking_length - 2) * 2
    print("Parking is €", price)