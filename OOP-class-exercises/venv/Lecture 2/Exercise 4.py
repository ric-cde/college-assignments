location = input("Where do you want to send your letter? ")

if location.lower() == "ireland":
    print("Postage is €1")
elif location.lower() == "europe":
    print("Postage is €1.70")
else:
    if input("Are you posting somewhere not in Ireland or Europe? (y/n) ") == "y":
        print("Postage is €2.00")