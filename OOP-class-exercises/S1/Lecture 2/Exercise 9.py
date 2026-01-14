month = input("Enter a month to find out how many days are in it: ")

thirty_one_days = ("january", "april", "may", "july", "august", "october", "december")
thirty_days = ("march", "june", "november")
twenty_eight_days = ("february")

if month.lower() in thirty_one_days:
    print(month.capitalize(), "has 31 days")
if month.lower() in twenty_eight_days:
    print(month.capitalize(), "has 28 or 29 days")
if month.lower() in thirty_days:
    print(month.capitalize(), "has 30 days")