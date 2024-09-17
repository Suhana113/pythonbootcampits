# wap to create a funcion of N factorial of a given number N..
def factorial(N):
    if N==0:
        return 1
    else:
        return N* factorial(N-1)
num=int(input("Enter a number:"))
print("factorial of",num,"is:",factorial(num))