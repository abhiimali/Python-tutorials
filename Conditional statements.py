#conditional statements
is_hot = False
is_cold=True
if is_hot:
    print("Its a hot day")
    print("Drink plenty of water")
elif is_cold:
     print("Its a cool day")
     print("Wear warm cloths")
else :
    print("Its a lovelyday")
price=1000000
has_good_credit=True

if has_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f"Down payment:${down_payment}")



