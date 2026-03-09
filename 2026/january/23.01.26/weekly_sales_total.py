def weekly_sales_total(sales):
    total = 0
    for sale in sales:
        total = total + sale
    if total < 1000:
        total = total * 0.9
    return total

sales = [0]
print(weekly_sales_total(sales))
