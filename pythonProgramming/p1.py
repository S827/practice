# give a certain discount to customers if they spend over $100. You will 
# also provide an extra discount if that customer is part of a loyalty 
# program. If the customer is not part of the loyalty program and did not 
# spend over a $100, a service charge of 5% is applied.

# limit = 100
# loyalty = bool(int(input("Are you a part of loyalty program?: True or False")))
# print(loyalty)
# print(bool("0"))
# discount = 12
# spend = int(input("How much did you spend?"))
# charge = 0.05
# dloyal = 20
# if spend > limit and loyalty:
#     total_bill = spend - dloyal
# elif spend > limit:
#     total_bill = spend - discount
# else:
#     total_bill = spend + spend * charge
# print("Please pay ${}".format(total_bill))

loyalty = False
total_bill = 100

if loyalty and total_bill > 100:
    #give 20 % discount
    total_bill = total_bill - (float(total_bill)/100) * 20
elif total_bill > 100:
    total_bill = total_bill - (float(total_bill)/100) * 10
else:
    total_bill = total_bill + total_bill * 0.05
print(total_bill)