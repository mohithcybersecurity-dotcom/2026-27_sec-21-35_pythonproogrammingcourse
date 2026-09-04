#python identity operators exercise
a = [1, 2, 3]
b = a
result=b is a#is identity operator
print("result of ",b,"is",a,"is:",result)

a=[1,2,3]
b=[1,2,3]
result=a is not b #is not identity operator
print("result of ",a,"is not",b,"is:",result)

a=[1,2,3]
b=[1,2,3]
result=a is b #is identity operator
print("result of ",a,"is",b,"is:",result)

a=[1,2,3,]
b=a
result=a is not b #is not identity operator
print("result of",a,"is not",b,"is:",result)