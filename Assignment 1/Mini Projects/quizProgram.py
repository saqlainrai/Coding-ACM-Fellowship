print("Welcome to the Quiz")

check = input ("Do you want to Play(y/n): ") 

if (check != "y"):
    quit()

score = 0

print("Let's start Playing ")

print("Choose any one of the Options ")

print("1. CPU stands for ")
print("a. Central Processing Unit     b. Central Power Unit       c. Circuit Processing Unit")
check = input("Your input is: ")

if (check == "a"):
    score = score + 1 



print("2. USB stands for ")
print("a. Universal Subject Bias     b. Unified Serial Bus       c. Universal Serial Bus")
check = input("Your input is: ")

if (check == "c"):
    score = score + 1 

print("3. The Capital of Pakistan is ")
print("a. Lahore     b. Karachi       c. Islamabad")
check = input("Your input is: ")

if (check == "c"):
    score = score + 1 

print("4. Python is a ")
print("a. Compiled language     b. Intrepreted language       c. Both")
check = input("Your input is: ")

if (check == "b"):
    score = score + 1 

print("5. Pillar of Object Oriented Programming is ")
print("a. Inheritance     b. Abstraction       c. Both")
check = input("Your input is: ")

if (check == "c"):
    score = score + 1 


# Announcement of Result

if (int(score) >= 4):
    print("Congratulations!!! Your Scores are:", score)
else:
    print("Your Scores are: ", score)