# ----------------------------------------------------------
#             TAX CALCULATION MANAGEMENT SYSTEM
# ----------------------------------------------------------

def tax(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return (income - 250000) * 0.05
    elif income <= 1000000:
        return 12500 + (income - 500000) * 0.20
    else:
        return 112500 + (income - 1000000) * 0.30

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

    file = open("tax_records.txt", "a")

    file.write(
        name + "," +
        str(age) + "," +
        occupation + "," +
        str(gross) + "," +
        str(deduction) + "," +
        str(taxable) + "," +
        str(final_tax) + "," +
        str(net_income) + "\n")

    file.close()

    print("Record saved successfully!")


def view_records():
    print("\n----- SAVED RECORDS -----")

    try:
        file = open("tax_records.txt", "r")
        data = file.read()
        file.close()

        if data:
            print("Name, Age, Occupation, Gross, Deduction, Taxable, Tax, Net")
            print("-" * 70)
            print(data)
        else:
            print("No records found.")

    except FileNotFoundError:
        print("No records found.")


def search_record():
    print("\n----- SEARCH RECORD -----")
    search = input("Enter Name: ").lower()
    found = False
    try:
        file = open("tax_records.txt", "r")
        for line in file:
            if search in line.lower():
                print("\nRecord Found:")
                print(line)
                found = True
        file.close()
        if not found:
            print("Record not found.")
    except FileNotFoundError:
        print("No records found.")


# MAIN MENU 

while True:

    print("\n==========================================")
    print("       TAX CALCULATION MANAGEMENT SYSTEM")
    print("==========================================")
    print("1. New Tax Calculation")
    print("2. View All Records")
    print("3. Search Record")
    print("4. Exit")
    print("==========================================")

    choice = input("Enter choice: ")

    if choice == "1":
        calculate()

    elif choice == "2":
        view_records()

    elif choice == "3":
        search_record()

    elif choice == "4":
        print("\nThank you for using the system!")
        break

    else:
        print("Invalid choice!")
