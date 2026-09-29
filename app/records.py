from app.file_handler import read_records


def view_records():
    print("\n----- SAVED RECORDS -----")

    data = read_records()

    if data:
        print("Name, Age, Occupation, Gross, Deduction, Taxable, Tax, Net")
        print("-" * 70)
        print(data)
    else:
        print("No records found.")


def search_record():
    print("\n----- SEARCH RECORD -----")

    search = input("Enter Name: ").lower()
    found = False

    data = read_records()

    if data:
        for line in data.splitlines():
            if search in line.lower():
                print("\nRecord Found:")
                print(line)
                found = True

    if not found:
        print("Record not found.")
