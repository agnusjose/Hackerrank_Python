def solve(meal_cost, tip_percent, tax_percent):
    tip=(meal_cost*tip_percent)/100
    tax=(meal_cost*tax_percent)/100
    total=tip+tax+meal_cost
    print(int(round(total)))

if __name__ == '__main__':
    meal_cost = float(input("Enter meal cost:").strip())

    tip_percent = int(input("Enter tip percentage:").strip())

    tax_percent = int(input("Enter tax percentage:").strip())

    solve(meal_cost, tip_percent, tax_percent)
    
