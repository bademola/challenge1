

# the loans
loan_costs = [500, 600, 200, 1000, 450]

#number of loans
print(f" The number of loans are {len(loan_costs)}.")

#the sum of the loans
print(f" The sum of all the loans is {sum(loan_costs)}.")

#calc average using sum and len
avg_loan =sum(loan_costs)/ len(loan_costs)
print(f" The average loan amount is {avg_loan}.")


##Part 2 Analyze Loan Data
##Detailed loan information

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#print(loan)
#Getting the futre value variable
future_value = loan.get("future_value")
print(future_value)
print(f"The future value is {future_value}.")

#Getting the remaining months
remaining_months = loan.get("remaining_months")
print(remaining_months)
print(f"Time remaining on this loan is {remaining_months}.")

present_value = future_value / (1 + .2/12)**remaining_months
print(present_value)

##Determine if the present value is equal to loan fair value
if present_value > loan.get("loan_price"):
    print("The loan is worth buying at current levels")
elif present_value < loan.get("loan_price"):
    print("The loan is not worth buying at current levels")    

#Part 3 Perform financial calculations

#calc present value function
def calculate_present_value(fut_value, rem_months, ann_discount_rate):
    print (fut_value / (1 + ann_discount_rate/12)**rem_months )

calculate_present_value(1000,9,.20)

#new loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#Using present value function

calculate_present_value(new_loan.get("loan_price"), new_loan.get("remaining_months"),.2)

