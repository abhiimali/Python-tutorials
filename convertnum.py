phone=input('phone:')
digits={"1":"one","2":"Two"}
op=''
for ch in  phone:
    op += digits.get(ch,"!")
print(op)
