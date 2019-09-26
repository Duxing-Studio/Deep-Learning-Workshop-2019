i = 11

if i % 2 == 0:
    print("偶数")
else:
    print("奇数")

today = "monday"

if today == "monday":
    print("this is monday")
elif today == "tuesday":
    print("this is tuesday")
elif today == "wednesday":
    print("this is wednesday")
elif today == "thursday":
    print("this is thursday")
elif today == "friday":
    print("this is friday")
elif today == "saturday":
    print("this is saturday")
elif today == "sunday":
    print("this is sunday")
else:
    print("something else")

today = "holiday"
bank_balance = 25000
if today == "holiday":
    if bank_balance > 20000:
        print("Go for shopping")
    else:
        print("Watch TV")
else:
    print("normal working day")
