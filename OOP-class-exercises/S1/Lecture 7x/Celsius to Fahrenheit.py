def CtoF(input_celsius):
  return input_celsius * 1.8 + 32

def FtoC(input_fahrenheit):
  return (input_fahrenheit - 32) / 1.8

c_or_f = input("What type of number do you want to convert? (Type C or F)")

if c_or_f.lower() == 'c':
  print(int(CtoF(float(input("Enter a temperature in celsius: ")))))
elif c_or_f.lower() == 'f':
  print(round(FtoC(float(input("Enter a temperature in fahrenheit: "))),2))
else:
  print("Did not understand that unit of temperature.")





