for item in range(1,21,2):
    print(item)

#cost of items

prices=[10,20,30]
total=0
for price in prices:
    total=total+price
print(f"{total}")

#nested loop

for x in range(4):
    for y in range(2):
        print(f'({x},{y})')

#example print F

numbers=[5,2,5,2,2]
for i in numbers:
        print('x'*i)
#pattern
num=[1,2,3,4,5,4,3,2,1]
space=[1,2,3,4,0,4,3,2,1]
for i in num:
    for j in space:
      print( 'x'*i)
      print( ' '*j)



