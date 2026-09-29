# Tax Calculation & Management System

A simple, command-line based Python application to calculate individual tax liabilities based on specific income slabs, apply rebates and cesses, and persistently store the data for future reference.

## 🚀 Features

* **New Tax Calculation:** Computes Gross Income, Taxable Income, Basic Tax, Rebates, Cess, Final Tax, and Net Income.
* **Persistent Storage:** Automatically saves calculated tax reports to a local `tax_records.txt` file.
* **View All Records:** Displays all previously saved tax records in a clean, tabulated format.
* **Search Functionality:** Allows users to search for specific tax records by Name (case-insensitive).
* **Zero Dependencies:** Runs entirely on standard Python built-in libraries.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your local machine:
* **Python (3.x or higher):** The core programming language used.
* **Pip:** Python's package installer (Included for standard best practices and future dependency management).
* **Git:** Version control system to clone the repository.

## 📥 Installation & Setup

**1. Clone the repository using Git**
Open your terminal or command prompt and run the following command to clone the project to your local machine:
```bash
git clone https://github.com/madusri26mip10100-bit/Tax-calculation-and-management-system.git
```

**2. Navigate to the project directory**
```bash
cd Tax-calculation-and-management-system
```

*(Optional)* **Set up a virtual environment using Pip**
While this specific script doesn't require external packages, it's a good Python practice:
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
python -m pip install --upgrade pip
```

## 💻 Usage

Run the main Python script from your terminal:

```bash
python "madusri 26MIP10100.py"
```

Once the application starts, you will be presented with the **Main Menu**:
```text
==========================================
       TAX CALCULATION MANAGEMENT SYSTEM
==========================================
1. New Tax Calculation
2. View All Records
3. Search Record
4. Exit
==========================================
```
Type the number corresponding to your choice and press `Enter` to navigate the system.

## 🗂️ File Structure

* `madusri 26MIP10100_2.py`: The main executable Python script containing the business logic and user interface.
* `tax_records.txt`: A flat text file generated automatically by the script to store saved tax calculations (comma-separated).

## 🤝 Contributing
Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribution.
