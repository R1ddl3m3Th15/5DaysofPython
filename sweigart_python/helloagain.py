# WAP that says hello and asks for your name and age, calculate length of name and their age in a year

print("Hello there")
print("What's your name?")
name = input()
print("Hello " + name + "!," + " what's your age?")
age = input()
print("Length of your name is " + str(len(name)))
print("You will be " + str(int(age) + 1) + " in a year.")
