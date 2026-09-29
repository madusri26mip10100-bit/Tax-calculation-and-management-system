from app.calculator import calculate
from app.records import view_records, search_record


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
