#To calculate compound interest
principal=float(input("Enter the principal amount:"))
rate_of_interest=float(input("Enter the rate of interest:"))
time=float(input("Enter the time in years :"))
compound_interest=principal*(pow((1+rate_of_interest/100),time))
print("The compound interest is:",compound_interest)