


def dectobin(n):
    if n==0:
        return '0'
    else:
        return dectobin(n//2)+str(n%2)
    

if __name__ == '__main__':
    n = int(input("Enter the decimal number to find its binary equivalent:").strip())
    bin=dectobin(n)
    print(bin)
    lis=[]
    count=0
    for i in range(len(bin)):
        if bin[i]=='1':
            count=count+1
        else:
            if count>0:
                lis.append(count)
            count=0
            continue
print("Number of 1s in it:",max(lis))
