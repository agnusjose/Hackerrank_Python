def is_leap(year):
    leap = False
    if (year%4)==0 and ((year%100)!=0 or (year%400)==0):
        leap = True
    return leap

year = int(input("Enter year to check whether its leap year or not:"))
print(is_leap(year))
