n=int(input("Enter the number of entries:"))
phone={}
for i in range(n):
    inp=input("Enter name and phone number with space between them:").split()
    name=inp[0]
    num=inp[1]
    phone[name]=num
try:
    while True:
        query = input("Enter the name to search:").strip()
        if query in phone:
            print(f"{query}={phone[query]}")
        else:
            print("Not found")
except EOFError:
    pass 
