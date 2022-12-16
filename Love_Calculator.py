# Take Input from user
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Code Logic

combineString = name1 + name2
lower_Combine = combineString.lower()

t = lower_Combine.count("t") 
r = lower_Combine.count("r") 
u = lower_Combine.count("u") 
e = lower_Combine.count("e") 

true = t + r + u + e

l = lower_Combine.count("l") 
o = lower_Combine.count("o") 
v = lower_Combine.count("v") 
e = lower_Combine.count("e") 

love = l + o + v + e

trueLOVE =  str(true) + str(love)
intTrue_Love = int(trueLOVE)


if (intTrue_Love<10) or (intTrue_Love>90):
    print(f"Your score is {intTrue_Love}, you go together like coke and mentos.")
elif (intTrue_Love<=40) or (intTrue_Love<=50):
    print(f"Your score is {intTrue_Love}, you are alright together.")
else:
    print(f"Your score is {intTrue_Love}.")