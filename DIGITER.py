# creating the algorithm
# getting the input from the User
num = int(input("Enter a number: ")) #input

# initializing variable for storing the number of digits
digits = 0

#initializing a temp variable
temp = num

# creating the loop
while (temp > 0):
    digit = temp % 10
    digits = digits + 1 
    temp = temp // 10

print("The number of digits in",num,"is",digits)