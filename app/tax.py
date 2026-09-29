def tax(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return (income - 250000) * 0.05
    elif income <= 1000000:
        return 12500 + (income - 500000) * 0.20
    else:
        return 112500 + (income - 1000000) * 0.30
