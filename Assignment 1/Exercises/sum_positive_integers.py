length = int(input("Enter the Number till which you want to sum: "))
sum = 0

for n in range(length + 1):
    sum += n

print("The sum of Required Numbers is: ", sum)