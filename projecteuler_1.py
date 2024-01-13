#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6,  and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

mult_three = 0
mult_five = 0
net_sum = 0
for ch in range(0,1000):
    mult_three = (ch/3) 
    mult_five = (ch/5)
    if (mult_three == int(mult_three)) or (mult_five == int(mult_five)):
        net_sum = net_sum + ch
    else:
        net_sum = net_sum
        mult_three = 0
        mult_five = 0
print(int(net_sum))
