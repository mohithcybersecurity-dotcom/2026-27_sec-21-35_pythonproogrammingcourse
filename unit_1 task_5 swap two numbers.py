#swapping two  numbers without using third variable
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
a,b=b,a
print("After swapping:")
print("first number is :",a)
print("second number is:",b)