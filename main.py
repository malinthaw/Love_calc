# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!\nDeveloped by MalinthaW 🚨")
name1 = input("What is your usual calling name and last name? \n")
name2 = input("What is her/his first calling name and last name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t+r+u+e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l+o+v+e

tl = str(true)+str(love)
#print(f"Your love score is {tl}")

if int(tl)<10 or int(tl)>90:
  print(f"Your score is {tl}, you go together like coke and mentos.")
elif int(tl) >= 40 and int(tl)<=50:
  print(f"Your score is {tl}, you are alright together.")
elif int(tl) == 73:
  print(f"Your score is {tl}, you are suppose to stay together no matter what. never giveup...")
else:
  print(f"Your love score is {tl}.")