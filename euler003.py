whole = int(600851475143)
tally = whole
primes = [1]
x = int(2)

while tally != 1:
    while (whole%x)!= 0:
        x += 1
    primes.append(x)
    tally = (whole/x)
    whole = tally
    x = 2
    
print(max(primes))

