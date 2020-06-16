deposit=int(input())
rate=float(7.1/100)
t=0
while deposit<700000:
    deposit = (deposit * 1.071)
    t+=1
print(t)