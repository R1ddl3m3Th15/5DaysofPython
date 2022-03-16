# a program to calculate 1+2+3+...+100 which Gauss did as a kid with a neat trick

sum = 0
for i in range(101):
    sum = sum + i
print(sum)

# now, a while equivalent of the above for loop

i = 0
sum = 0
while i<=100:
    sum = sum + i
    i = i + 1
print(sum)
