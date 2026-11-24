# 🏦 PREM BANK – Python Banking Management System

A simple and interactive **Banking Management System** developed using Python and Streamlit. This application allows users to create bank accounts, securely log in using a 4-digit PIN, check account balances, deposit money, withdraw money, and view transaction history.

The application uses an Excel file to store account details and transaction records.

## ✨ Features

- **Create Account:** Create a new bank account with a unique account number and 4-digit PIN.
- **Customer Login:** Login using an account number and PIN.
- **Dashboard:** View account information and current balance.
- **Check Balance:** Check the available account balance.
- **Deposit Money:** Add money to your bank account.
- **Withdraw Money:** Withdraw money with insufficient balance validation.
- **Transaction History:** View all account transactions with date and time.
- **Download History:** Download transaction records in CSV format.
- **Session Management:** Maintain login sessions and provide logout functionality.
- **Custom UI:** Clean and user-friendly interface designed using Streamlit and custom CSS.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| OpenPyXL | Excel file handling |
| Pandas | Transaction data management |
| UUID | Unique transaction ID generation |
| Datetime | Transaction date and time |

## 📂 Project Structure

```text
PREM-BANK/
│
├── app.py                 # Main Streamlit application
├── banking_app.py         # Banking functions and account management
├── bank_records.xlsx      # Excel database (auto-created)
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

*Note: The Excel database is created automatically when the application runs, depending on the implementation of `banking_app.py`.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PREM-BANK.git
```

### 2. Navigate to the Project Folder

```bash
cd PREM-BANK
```

### 3. Install Required Libraries

```bash
pip install streamlit openpyxl pandas
```

### 4. Run the Application

```bash
streamlit run app.py
```

### 5. Open in Browser

After running the command, Streamlit will provide a local URL:

```text
http://localhost:8501
```

Open this URL in your browser to access PREM BANK.

## 📋 Application Modules

### 1. Home
Displays the welcome page and provides options to create an account or log in.

### 2. Create Account
Users can register by entering:
- Customer Name
- Account Number
- 4-digit PIN
- Opening Balance

The application validates the inputs and prevents duplicate account numbers.

### 3. Login
Customers can access their accounts using their registered account number and PIN.

### 4. Customer Dashboard
Displays:
- Customer Name
- Account Number
- Current Account Balance

### 5. Banking Services

| Service | Description |
|---|---|
| Check Balance | Displays the available balance |
| Deposit Money | Adds money to the account |
| Withdraw Money | Deducts money from the account |
| Transaction History | Displays previous transactions |

### 6. Transaction History
Every transaction contains:
- Transaction ID
- Transaction Type
- Transaction Amount
- Previous Balance
- Current Balance
- Date and Time

Users can also download their transaction history as a CSV file.

## 💾 Data Storage

PREM BANK uses an Excel workbook (`bank_records.xlsx`) as its database.

Account and transaction information is stored in rows containing account details, transaction information, balance records, and timestamps.

The Excel file is managed using the OpenPyXL library.

## 🔐 Validations

The application includes the following validations:

- Name cannot be empty.
- Account number must contain digits only.
- Duplicate account numbers are not allowed.
- PIN must contain exactly 4 digits.
- Deposit amount must be greater than zero.
- Withdrawal amount must be greater than zero.
- Withdrawal cannot exceed the available balance.
- Invalid login credentials are rejected.

## 🚀 Future Improvements

- Password/PIN hashing and stronger authentication.
- SQLite or MySQL database integration.
- Admin dashboard and customer management.
- Money transfer between bank accounts.
- PDF transaction statement generation.
- Improved security and input validation.
- Deployment as an online banking demo.

## ⚠️ Disclaimer

This project is developed for **educational purposes and Python programming practice**. It is not a real banking application and should not be used to store actual financial or sensitive customer information.

The current Excel-based implementation stores PINs in plain text and is not suitable for production banking.

## 👨‍💻 Developer

**Project Name:** PREM BANK  
**Project Type:** Banking Management System  
**Language:** Python  
**Framework:** Streamlit  
**Storage:** Microsoft Excel

---

⭐ If you find this project useful, consider giving it a star on GitHub!
