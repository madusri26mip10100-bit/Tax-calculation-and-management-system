from app.tax import tax
from app.file_handler import save_record


def calculate():
    print("\n----- TAX CALCULATION -----")

    name = input("Name: ")
    age = int(input("Age: "))
    occupation = input("Occupation: ")

    salary = float(input("Annual Salary: ₹"))
    other = float(input("Other Income: ₹"))
    deduction = float(input("Deduction: ₹"))

    gross = salary + other
    taxable = max(0, gross - deduction)

    basic_tax = tax(taxable)

    rebate = basic_tax if taxable <= 500000 else 0
    tax_after_rebate = basic_tax - rebate

    cess = tax_after_rebate * 0.04
    final_tax = tax_after_rebate + cess

    monthly_tax = final_tax / 12
    net_income = gross - final_tax
    percentage = (final_tax / gross) * 100 if gross > 0 else 0

    print("\n========== TAX REPORT ==========")
    print("Name           :", name)
    print("Age            :", age)
    print("Occupation     :", occupation)
    print("--------------------------------")
    print("Salary         : ₹", round(salary, 2))
    print("Other Income   : ₹", round(other, 2))
    print("Gross Income   : ₹", round(gross, 2))
    print("Deduction      : ₹", round(deduction, 2))
    print("Taxable Income : ₹", round(taxable, 2))
    print("--------------------------------")
    print("Basic Tax      : ₹", round(basic_tax, 2))
    print("Rebate         : ₹", round(rebate, 2))
    print("Cess (4%)      : ₹", round(cess, 2))
    print("Final Tax      : ₹", round(final_tax, 2))
    print("--------------------------------")
    print("Monthly Tax    : ₹", round(monthly_tax, 2))
    print("Net Income     : ₹", round(net_income, 2))
    print("Tax Rate       :", round(percentage, 2), "%")
    print("================================")

    save_record(
        name,
        age,
        occupation,
        gross,
        deduction,
        taxable,
        final_tax,
        net_income
    )

    print("Record saved successfully!")
