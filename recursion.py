def factorial(n):
    if n>0:
        fact=n*factorial(n-1)
    else :
        return 1
    return fact

if __name__ == '__main__':

    n = int(input("Enter the number to calculate its factorial:").strip())
    result = factorial(n)
    print(result)

    
