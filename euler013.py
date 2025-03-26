## Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
sums = open("thirteen.txt")

numbers = []
for num in sums:
    num = num.rstrip(" \n")
    numbers.append(int(num) / 10000000000)
tot = 0
for item in numbers:
    tot += item
print(tot)