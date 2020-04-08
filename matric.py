matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][1])

for row in matrix:
    for i in row :
        print(i)
#codewithmosh.com

#list methods
num=[5,2,1,7,4]
num.append(20)
print(num)
num.insert(0,10)
print(num)
num.remove(5)
print(num)
num.pop(2)
print(num)
print(num.index(7))
print(30 in num)
print(num.count(2))
num.sort()
print(num)
