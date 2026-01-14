dog_age = int(input("How old is your dog? "))

if dog_age > 2:
    dog_years = 2 * 10.5
    dog_years = dog_years + ((dog_age - 2) * 4)
    print("Your dog is", int(dog_years), "in dog years.")
else:
    dog_years = dog_age * 10.5
    print("Your dog is", int(dog_years), "in dog years.")

