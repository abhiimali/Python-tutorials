num=[2,2,3,3,4,5,6,6]
uniq=[]

for n in  num:
    if n  not in uniq:
        uniq.append(n)
print(uniq)
