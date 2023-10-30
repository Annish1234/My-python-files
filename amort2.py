def get_I_P(ob, emi, mir):
    annual_interest_payment = 0
    annual_principal_payment = 0
    for month in range(1, 13):
        interest_payment = ob * mir 
        principal_payment = emi - interest_payment
        cl = ob - principal_payment
        annual_interest_payment += interest_payment
        annual_principal_payment = annual_principal_payment+ principal_payment
    return annual_interest_payment, annual_principal_payment,ob,cl
    

def Annual():
    # Loan details
    principal = 100000  # Principal amount
    annual_interest_rate = 0.06  # Annual interest rate (6%)
    loan_term_years = 3  # Loan term in years

    # Calculate the total number of payments (years to months)
    loan_term_months = loan_term_years * 12

    # Monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12

    # Calculate the monthly EMI
    emi = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**loan_term_months) / ((1 + monthly_interest_rate)**loan_term_months - 1)
    
    # Initialize variables
    opening_balance = principal
    amortization_table = []

    # Generate the year-wise amortization table
    for year in range(1, loan_term_years + 1):
        annual_interest_payment, annual_principal_payment,opening_balance,closing_balance = get_I_P(opening_balance, emi, monthly_interest_rate)
        # closing_balance = opening_balance - annual_principal_payment
        amortization_table.append([year, opening_balance, emi * 12, annual_interest_payment, annual_principal_payment, closing_balance])
        opening_balance = closing_balance

    # Display the year-wise table
    print("Year  Opening Balance  Yearly EMI  Yearly Interest  Yearly Principal  Closing Balance")
    for row in amortization_table:
        print("{:<4}  {:<15.2f}  {:<12.2f}  {:<15.2f}  {:<15.2f}  {:<15.2f}".format(*row))

Annual()

