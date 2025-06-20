def factorial(i):
    if i==1 :
        return 1
    else :
        return factorial(i-1) * i

n = int(input("Enter a number : "))

print(f"Factorial of {n} is : {factorial(n)}")