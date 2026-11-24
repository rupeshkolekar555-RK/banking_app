# 🏦 PREM BANK – Banking Management System

PREM BANK is one of my first-year Python projects, developed as part of my journey in Computer Science Engineering (Artificial Intelligence & Machine Learning).

I created this project to improve my Python programming skills and understand how basic banking operations can be implemented through code.

The application allows users to create an account, log in using their account number and PIN, check their balance, deposit and withdraw money, and view their transaction history.

To make the project more interesting, I developed it with two different interfaces: a **Command-Line Interface (CLI)** and a **web-based interface using Streamlit**.

## ✨ Features

- **Create Account:** Create a new bank account with a name, account number, 4-digit PIN and opening balance.
- **Customer Login:** Log in using an account number and PIN.
- **Check Balance:** View the current account balance.
- **Deposit Money:** Add money to the account.
- **Withdraw Money:** Withdraw money with balance validation.
- **Transaction History:** View previous transactions with their details.
- **Download History:** Download transaction records in CSV format through the web application.
- **Logout:** Exit the customer account.

## 🖥️ Application Interfaces

This project has two interfaces:

### 1. Command-Line Interface (CLI)

The CLI version runs in the terminal and provides an interactive banking experience.

It uses libraries like Rich, Colorama and PyFiglet to make the terminal interface more attractive and easier to use.

### 2. Web Application (Streamlit)

The web version provides a simple and clean graphical interface that can be accessed through a browser.

It includes:
- Home page
- Account creation
- Customer login
- Banking dashboard
- Balance checking
- Deposit and withdrawal
- Transaction history
- CSV download option

## 🛠️ Technologies & Libraries Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Building the web interface |
| OpenPyXL | Managing Excel records |
| Pandas | Handling transaction data |
| Rich | Formatting terminal output |
| Colorama | Adding terminal colors |
| PyFiglet | Creating ASCII text |
| Pwinput | Masking PIN input |
| UUID | Generating transaction IDs |
| Datetime | Recording date and time |

## 📂 Project Structure

```text
banking_app/
│
├── app.py
│   └── Web application
│
├── banking_app.py
│   └── Banking functions and CLI application
│
├── bank_records.xlsx
│   └── Excel database
│
└── README.md
```

The Excel database is created automatically when the application runs, if it does not already exist.

## ⚙️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/rupeshkolekar555-RK/banking_app.git
```

### Step 2: Open the Project Folder

```bash
cd banking_app
```

### Step 3: Install Required Libraries

```bash
pip install streamlit openpyxl pandas rich colorama pyfiglet pwinput
```

### Step 4: Run the Application

**For the Web Application:**

```bash
streamlit run app.py
```

**For the CLI Application:**

```bash
python banking_app.py
```

For the web version, open `http://localhost:8501` in your browser.

## 💾 Data Storage

I used an Excel file named `bank_records.xlsx` to store account details and transaction records.

The file maintains information such as:

- Account number
- Customer name
- PIN
- Transaction ID
- Transaction type
- Transaction amount
- Previous balance
- Current balance
- Transaction date and time

Whenever a customer deposits or withdraws money, a new transaction record is added to the Excel file.

## 📚 What I Learned

As a first-year student, working on this project helped me gain practical experience with several Python concepts.

- Understanding Python functions and modules.
- Working with external Python libraries.
- Reading and writing Excel files.
- Handling user input and validating data.
- Using loops and conditional statements.
- Generating unique transaction IDs.
- Creating a web application using Streamlit.
- Displaying data using Pandas.
- Understanding basic banking operations and transaction management.

## 🚀 Future Improvements

I would like to improve this project by adding more features as I learn new technologies.

- Integrate SQLite or MySQL.
- Improve account security using PIN hashing.
- Add money transfers between accounts.
- Create an admin dashboard.
- Generate PDF transaction statements.
- Improve the overall user interface.
- Deploy the application online.

## ⚠️ Disclaimer

This project is created for educational purposes as part of my learning journey in Python programming.

It is a basic banking simulation, not a real banking system. It currently stores PINs in plain text and uses Excel for data storage. It should not be used for actual financial transactions or sensitive information.

## 👨‍💻 About Me

**Rupesh Kolekar**  
First-Year B.Tech Student  
Computer Science & Engineering (Artificial Intelligence & Machine Learning)

I'm currently exploring Python programming, software development and the practical applications of technology through small projects like PREM BANK.

**GitHub:** [@rupeshkolekar555-RK](https://github.com/rupeshkolekar555-RK)

**Project Repository:** [PREM BANK](https://github.com/rupeshkolekar555-RK/banking_app)

---

⭐ Thanks for visiting my project! Suggestions and feedback are always welcome.