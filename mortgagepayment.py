def mortgage_payments(principal, rate, amortization):
    """
    Calculate different mortgage payment options.
    :param principal: Loan amount (float)
    :param rate: Annual quoted interest rate as a percentage (float)
    :param amortization: Amortization period in years (int)
    :return: Tuple containing monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly, and rapid weekly payments
    """
    # Annual quoted interest rate in decimals
    rq = rate / 100
    
    # Total number of payments for monthly, semi-monthly, bi-weekly, and weekly
    n_monthly = amortization * 12
    n_semi_monthly = amortization * 24
    n_bi_weekly = amortization * 26
    n_weekly = amortization * 52
    
    # Periodic interest rates
    r_monthly = (1 + rq / 2) ** (2/12) - 1
    r_semi_monthly = (1 + rq / 2) ** (2/24) - 1
    r_bi_weekly = (1 + rq / 2) ** (2/26) - 1
    r_weekly = (1 + rq / 2) ** (2/52) - 1
    
    # Payments using PV (present value) of annuity formula
    def annuity_payment(principal, r, n):
        return principal * (r / (1 - (1 + r) ** -n)) if r > 0 else principal / n
    
    monthly_payment = annuity_payment(principal, r_monthly, n_monthly)
    semi_monthly_payment = annuity_payment(principal, r_semi_monthly, n_semi_monthly)
    bi_weekly_payment = annuity_payment(principal, r_bi_weekly, n_bi_weekly)
    weekly_payment = annuity_payment(principal, r_weekly, n_weekly)
    
    # Rapid payments
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4
    
    return (round(monthly_payment, 2), round(semi_monthly_payment, 2), round(bi_weekly_payment, 2), 
            round(weekly_payment, 2), round(rapid_bi_weekly_payment, 2), round(rapid_weekly_payment, 2))

# Calculate using the data
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the quoted interest rate (e.g., 5.5 for 5.5%): "))
amortization = int(input("Enter the amortization period in years: "))

# Payments Calculation
payments = mortgage_payments(principal, rate, amortization)

# Display results
print(f"Monthly Payment: ${payments[0]:,.2f}")
print(f"Semi-monthly Payment: ${payments[1]:,.2f}")
print(f"Bi-weekly Payment: ${payments[2]:,.2f}")
print(f"Weekly Payment: ${payments[3]:,.2f}")
print(f"Rapid Bi-weekly Payment: ${payments[4]:,.2f}")
print(f"Rapid Weekly Payment: ${payments[5]:,.2f}")
