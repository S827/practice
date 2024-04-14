def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate)/100, 2)
print("total tax: ", calculate_tax(125, 10))
print("total tax: ", calculate_tax(225, 15))