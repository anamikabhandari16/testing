import math

principal = float(input( "Enter the principal amount:" ))
Rate = float (input(" Enter annual rate of interest:"))
time = int (input(" enter the time (in years): " ))

print ( "1. Calculate simple interest")
print( " 2. Calculate compound interest")
choice = int ( input (" Enter  your choice(1 or 2):"))

if choice == 1:
    interest = (principal* Rate* time)/100
    amount = principal+ interest
    print (" Simple interest :{0:16.2f} ".format(interest))
    print (" Amount after interest :{0:12.2f}".format(amount))
else:
    n = int (input (" number of times interest is compounded in year:"))
    Rate = Rate/100
    periods = time * n
    amount = principal * pow((1+ Rate/n), periods)
    interest = amount - principal

    print (" Compound interet :{0:16.2f}".format(interest))
    print (" Amount after interest :{0:12.2f} ".format(amount))
