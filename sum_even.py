num = int(input("Enter an even number: "))
sum = 0
if num%2 == 0:
    print("Its an valid number") 
    for i in range(1, num+1):
        if i%2 == 0:
            sum = sum+i
    print("Sum of even number:", sum)
else:
    print("Its an invalid number")


