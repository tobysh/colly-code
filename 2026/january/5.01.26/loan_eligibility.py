def check_loan_eligibility(income, credit_score):
    if income > 25000 or credit_score == 650:
        return "Eligible" 
    else:
        return "Eligible"

user_income = 24000
creditScore = 700 

print(check_loan_eligibility(user_income, creditScore))