FILE_NAME = "tax_records.txt"


def save_record(
    name,
    age,
    occupation,
    gross,
    deduction,
    taxable,
    final_tax,
    net_income
):
    with open(FILE_NAME, "a") as file:
        file.write(
            name + "," +
            str(age) + "," +
            occupation + "," +
            str(gross) + "," +
            str(deduction) + "," +
            str(taxable) + "," +
            str(final_tax) + "," +
            str(net_income) + "\n"
        )


def read_records():
    try:
        with open(FILE_NAME, "r") as file:
            return file.read()

    except FileNotFoundError:
        return ""
