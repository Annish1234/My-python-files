def generate_amortization_schedule(principal, annual_interest_rate, loan_term_years):
    # Calculate the total number of payments (years to months)
    loan_term_months = loan_term_years * 12

    # Monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12

    # Calculate the monthly EMI
    emi = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**loan_term_months) / ((1 + monthly_interest_rate)**loan_term_months - 1)

    # Initialize variables
    opening_balance = principal
    amortization_table = []

    for year in range(1, loan_term_years + 1):
        annual_interest_payment = 0
        annual_principal_payment = 0

        for month in range(1, 13):
            interest_payment = opening_balance * monthly_interest_rate
            principal_payment = emi - interest_payment
            closing_balance = opening_balance - principal_payment

            annual_interest_payment += interest_payment
            annual_principal_payment += principal_payment

            # Update opening balance for the next month
            opening_balance = closing_balance

        # Append yearly data to the table
        amortization_table.append([year, principal, emi * 12, annual_interest_payment, annual_principal_payment, closing_balance])

    return amortization_table

# Loan details
principal = 100000  # Principal amount
annual_interest_rate = 0.06  # Annual interest rate (6.5%)
loan_term_years = 3  # Loan term in years

# Generate the amortization table
amortization_table = generate_amortization_schedule(principal, annual_interest_rate, loan_term_years)

# Display the table
print("Year  Opening Balance  Yearly EMI  Yearly Interest  Yearly Principal  Closing Balance")
for row in amortization_table:
    year, opening_balance, yearly_emi, yearly_interest, yearly_principal, closing_balance = row
    print("{:<4}  {:>11,.2f}  {:>12,.2f}  {:>12,.2f}  {:>12,.2f}  {:>12,.2f}".format(year, opening_balance, yearly_emi, yearly_interest, yearly_principal, closing_balance))
