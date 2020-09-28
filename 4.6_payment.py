def computepay(h, r):
    # Try to cast to float if not input is not a number
    try:
        h = float(h)
        r = float(r)
    except:
        return("Invalid value")
        quit()

    # calculate the payment
    pay = h * r

    # if the worker works more than 40 hours we need to pay 1.5 times the value of an hour
    # per extra hour
    if h <= 40.0:
        return (pay)
    else:
        extra_h = h - 40
        extra_pay = extra_h * (1.5 * r)
        pay = extra_pay + (40 * r)
        return (pay)


#Input and prints
hrs = input("Enter Hours:")
vle = input("Enter Value:")
p = computepay(hrs, vle)
print("Pay", p)
