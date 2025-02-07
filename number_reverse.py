if __name__ == '__main__':
    arr = list(map(int, input("Enter numbers with space between:").rstrip().split()))
    n=len(arr)
    for i in range (n-1,-1,-1):
        print(arr[i],end=" ")
        
