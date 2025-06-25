"""Calculation of a repayment plan for a loan."""

# --- Initial loan parameters ---
principal = 350_000        # Initial debt in euros
interest_rate = 1.9        # Annual interest rate in percent
monthly_payment = 1_800    # Monthly payment in euros

# --- Initialize tracking variables ---
month = 0
total_interest = 0
total_payments = 0
remaining_debt = principal

# --- Repayment loop: continue until the loan is fully repaid ---
while remaining_debt > 0:
    month += 1

    # Calculate monthly interest (1/12 of annual rate), rounded to cents
    interest = round(remaining_debt * interest_rate / 100 / 12, 2)
    remaining_debt += interest

    # Determine payment for this month (cannot pay more than remaining debt)
    payment = min(monthly_payment, remaining_debt)

    # Reduce the remaining debt by the payment
    remaining_debt -= payment

    # Accumulate totals for summary
    total_payments += payment
    total_interest += interest

    # Output the details for this month
    principal_repaid = payment - interest
    print(f'{month:3d}. Month: Interest {interest:8.2f} €, '
          f'Repayment {principal_repaid:8.2f} €, '
          f'Remaining debt {remaining_debt:10.2f} €')

# --- Summary of the repayment plan ---
total_principal_repaid = total_payments - total_interest
years = month // 12
months = month % 12

print("\nLoan fully repaid after "
      f"{years} year(s) and {months} month(s).\n")
print(f'Total paid        : {total_payments:10.2f} €')
print(f'   of which interest   : {total_interest:10.2f} €')
print(f'   of which principal  : {total_principal_repaid:10.2f} €')