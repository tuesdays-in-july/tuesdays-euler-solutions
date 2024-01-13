#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6,  and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

mult_three = 0
mult_five = 0
net_sum = 0
#for ch in range(0,10):
for ch in range(0,1000):
    mult_three = (ch/3)                                                #just does 3s
    mult_five = (ch/5)                                                    #now have 5s
    if (mult_three == int(mult_three)) or (mult_five == int(mult_five)):    #fingers crossed
      #  print(ch)
        net_sum = net_sum + ch
    else:
        net_sum = net_sum
        mult_three = 0
        mult_five = 0
print("The sum of all multiples of 3 or 5 below 1000 is...")
print(int(net_sum))

#YIPPEE
#going through to clean up final results, fixing range, renaming variables, and getting a cleaner final statement...
#and we've got a programmed solution for Project Euler's first problem :3