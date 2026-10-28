# ---- Reading input ----
# Use these EXACT prompt strings so your program matches the required format.
# How many times you read, and in what order, is up to you.
#
#   the day:   int(input("Enter day (1-8): "))
#   each age:  int(input("Enter age (-1 to stop): "))
#
# Reading stops when the age entered is -1 (the -1 is not counted as a visitor).


# ---- Your program ----
# Read the input and work everything out here. How you structure and order
# the steps is up to you.
daytype = int(input("Enter day (1-8): "))
if 1 <= daytype <= 5:
    daytype = "weekday"
elif 6 <= daytype <= 7:
    daytype = "weekend"
else:
    daytype = "holiday"


children = 0
adult = 0
senior = 0
age = int(input("Enter age (-1 to stop): "))
while age != -1:
    if 0 <= age <= 12:
        children += 1
    elif 13 <= age <= 59:
        adult += 1
    else:
        senior += 1
    age = int(input("Enter age (-1 to stop): "))

totapeople = children + adult + senior 
group = adult // 5
adultleft = adult % 5



if daytype == "weekday":
    adultprice = group * 35 * 5 + adultleft * 60
    totalprice = children * 30 +  adultprice + senior * 40
    discount = 0
    if 3 <= totapeople <= 6:
        servicefee = 5 * totapeople
    elif totapeople > 6:
        servicefee = 30
    else:
        servicefee = 0

elif daytype == "weekend":
    adultprice = group * 65 * 5 + adultleft * 80
    totalprice = children * 40 +  adultprice + senior * 50
    if group >= 1:
        discount = 0.1 * totalprice         
    else:
        discount = 0
    if totapeople <= 6:
        servicefee = 5 * totapeople
    else:
        servicefee = 30 
   
else:
    adultprice = group * 75 * 5 + adultleft * 100
    totalprice = children * 50 +  adultprice + senior * 60
    if group >= 1:
        discount = 0.1 * totalprice
    else:
        discount = 0
    if totapeople <= 6:
        servicefee = 5 * totapeople
    else:
        servicefee = 30 

totalprice = totalprice + servicefee - discount  

# ---- Output ----
# Replace each ??? with the value you computed. Keep every label, space, and
# the "{:.2f}" formatting exactly as shown — your output is compared exactly.

print("Day type:", daytype)
print("Children:", children)
print("Adults:", adult)
print("Seniors:", senior)
print("Total people:", totapeople)
print("Groups formed:", group)
print("Discount:", "{:.2f}".format(discount))
print("Service fee:", "{:.2f}".format(servicefee))
print("Total cost:", "{:.2f}".format(totalprice))
