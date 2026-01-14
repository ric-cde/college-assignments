speed = int(input("How fast are you going?"))
points = 0

if (speed < 70):
    print("OK")
elif (speed > 70):
    over = speed - 70
    points = (over // 5)
    print("Points: ", points)
    if (points > 12):
        print("Licence suspended")

sp = int(input("Please enter your speed: "))
pts = 0
ex = 0
if sp <= 70:
    print("No points, drive safe")
elif sp > 70:
#    for i in range(70, sp+1):
#        ex = i - 70
        pts = (sp+1 - 70) / 5
if pts >= 12:
    print("Your licence is revoked")
print(int(pts))