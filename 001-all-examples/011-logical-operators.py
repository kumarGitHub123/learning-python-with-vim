has_high_income = True
has_good_credit = False
has_criminal_records = False

if has_high_income and has_good_credit and not has_criminal_records:
    print("Eligible for loan")
elif has_high_income or has_good_credit:
    print("Just Eligible for loan")

