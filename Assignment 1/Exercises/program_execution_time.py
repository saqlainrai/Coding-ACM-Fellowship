# find the time for summation of N integers
import time

numbers = int(input("Enter the End of Numbers: "))
sum = 0 

start_time = time.time()

for i in range(numbers + 1):
    sum += i

end_time = time.time()

print("The sum of Numbers is ", sum)
print("The time taken by the program is ", end_time - start_time)