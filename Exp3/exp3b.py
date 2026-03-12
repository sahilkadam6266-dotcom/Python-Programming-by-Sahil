def simple_interest(principal, rate, time):
    si=(principal*rate*time)/100
    return si
p=float(input("Enter principal value:"))
r=float(input("Enter rate:"))
t=float(input("Enter time (in years):"))
interest=simple_interest(p,r,t)
print("Simple interest=",interest)