total_numbers = int(input("Enter the total Length of numbers: "))
total_sum = 0 

for n in range(total_numbers):
    temp = float(input("Enter the " + (str(n + 1)) + " Number: "))
    total_sum += temp

avg = total_sum / total_numbers

print("The average of Provided Number is: ",avg)