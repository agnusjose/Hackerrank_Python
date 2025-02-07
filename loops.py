if __name__ == '__main__':
    n = int(input("Enter the number to obtain its multiplication table:").strip())
    for i in range(1,11):
       print(str(n)+" x "+str(i)+" = "+str(n*i))
