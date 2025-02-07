if __name__ == '__main__':

    arr = []
    lis=[]

    for i in range(6):
             arr.append(list(map(int, input("Enter numbers for matrix:").rstrip().split())))
    for i in range(4):
        for j in range (4):
                sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                lis.append(sum)
    print(max(lis))
   
