import streamlit as st
import openpyxl
import uuid
from datetime import datetime
import pandas as pd

import banking_app as bank

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="PREM BANK",
    page_icon="🏦",
    layout="wide"
)

bank.create_excel_file()


# -----------------------------------
# SESSION MANAGEMENT
# -----------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "account_no" not in st.session_state:
    st.session_state.account_no = None


# -----------------------------------
# CUSTOM UI DESIGN
# -----------------------------------

st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb;
}

.block-container {
    padding-top: 2rem;
}

.bank-title {
    background: linear-gradient(100deg, #102a43, #176b87);
    color: white;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
}

.bank-title h1 {
    color: white;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #dddddd;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------------
# BANK HEADER
# -----------------------------------

st.markdown("""
<div class="bank-title">
    <h1>🏦 PREM BANK</h1>
    <p>Welcome to Python Banking System</p>
</div>
""", unsafe_allow_html=True)


# -----------------------------------
# DATABASE TRANSACTION FUNCTION
# -----------------------------------

def add_transaction(account_no, transaction_type, amount):

    name, pin = bank.get_user_details(account_no)

    previous_balance = bank.get_balance(account_no)

    if transaction_type == "Deposit":
        current_balance = previous_balance + amount

    else:
        current_balance = previous_balance - amount

    transaction_id = str(uuid.uuid4())[:8]

    date_time = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    workbook = openpyxl.load_workbook(bank.FILE_NAME)
    sheet = workbook.active

    sheet.append([
        account_no,
        name,
        pin,
        transaction_id,
        transaction_type,
        amount,
        previous_balance,
        current_balance,
        date_time
    ])

    workbook.save(bank.FILE_NAME)
    workbook.close()


# -----------------------------------
# LOGIN / CREATE ACCOUNT
# -----------------------------------

if not st.session_state.logged_in:

    option = st.sidebar.radio(
        "MAIN MENU",
        ["Home", "Create Account", "Login"]
    )

    if option == "Home":

        st.subheader("Welcome to PREM BANK")

        st.write(
            "A simple Python-based banking management system."
        )

        col1, col2 = st.columns(2)

        with col1:
            st.info("📝 Create your bank account.")

        with col2:
            st.info("🔐 Login to access banking services.")


    # --------------------------------
    # CREATE ACCOUNT
    # --------------------------------

    elif option == "Create Account":

        st.subheader("📝 Create New Account")

        with st.form("create_form"):

            name = st.text_input("Enter Name")

            account_no = st.text_input(
                "Enter Account Number"
            )

            pin = st.text_input(
                "Create 4-digit PIN",
                type="password",
                max_chars=4
            )

            opening_balance = st.number_input(
                "Opening Balance (₹)",
                min_value=0.0,
                step=100.0
            )

            submit = st.form_submit_button(
                "Create Account",
                use_container_width=True
            )

        if submit:

            if not name.strip():
                st.error("Please enter your name.")

            elif not account_no.isdigit():
                st.error("Account number must contain digits only.")

            elif bank.account_exists(account_no):
                st.error("Account number already exists.")

            elif len(pin) != 4 or not pin.isdigit():
                st.error("PIN must contain exactly 4 digits.")

            else:

                transaction_id = str(uuid.uuid4())[:8]

                date_time = datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )

                workbook = openpyxl.load_workbook(
                    bank.FILE_NAME
                )

                sheet = workbook.active

                sheet.append([
                    account_no,
                    name.strip(),
                    pin,
                    transaction_id,
                    "Opening",
                    opening_balance,
                    0,
                    opening_balance,
                    date_time
                ])

                workbook.save(bank.FILE_NAME)
                workbook.close()

                st.success("Account created successfully!")

                st.info(
                    f"Your Account Number is: {account_no}"
                )


    # --------------------------------
    # LOGIN
    # --------------------------------

    elif option == "Login":

        st.subheader("🔐 Customer Login")

        with st.form("login_form"):

            account_no = st.text_input(
                "Account Number"
            )

            pin = st.text_input(
                "Enter PIN",
                type="password"
            )

            login_button = st.form_submit_button(
                "Login",
                use_container_width=True
            )

        if login_button:

            workbook = openpyxl.load_workbook(
                bank.FILE_NAME,
                data_only=True
            )

            sheet = workbook.active

            valid = False

            for row in sheet.iter_rows(
                min_row=2,
                values_only=True
            ):

                if (
                    str(row[0]) == account_no
                    and str(row[2]) == pin
                ):

                    valid = True
                    break

            workbook.close()

            if valid:

                st.session_state.logged_in = True
                st.session_state.account_no = account_no

                st.success("Login successful!")

                st.rerun()

            else:

                st.error(
                    "Invalid Account Number or PIN."
                )


# -----------------------------------
# CUSTOMER DASHBOARD
# -----------------------------------

else:

    account_no = st.session_state.account_no

    name, pin = bank.get_user_details(account_no)

    balance = bank.get_balance(account_no)

    # SIDEBAR

    st.sidebar.success(f"Welcome, {name}")

    st.sidebar.write(
        f"Account: {account_no}"
    )

    if st.sidebar.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False
        st.session_state.account_no = None

        st.rerun()

    # DASHBOARD

    st.subheader(f"Hello, {name}!")

    col1, col2 = st.columns(2)

    col1.metric(
        "💰 Current Balance",
        f"₹{balance:,.2f}"
    )

    col2.metric(
        "🏦 Account Number",
        account_no
    )

    st.divider()

    # BANKING MENU

    menu = st.radio(
        "Select Banking Service",
        [
            "Check Balance",
            "Deposit Money",
            "Withdraw Money",
            "Transaction History"
        ],
        horizontal=True
    )


    # --------------------------------
    # CHECK BALANCE
    # --------------------------------

    if menu == "Check Balance":

        st.subheader("💰 Account Balance")

        st.metric(
            "Available Balance",
            f"₹{balance:,.2f}"
        )


    # --------------------------------
    # DEPOSIT MONEY
    # --------------------------------

    elif menu == "Deposit Money":

        st.subheader("➕ Deposit Money")

        with st.form("deposit_form"):

            amount = st.number_input(
                "Enter Deposit Amount (₹)",
                min_value=0.0,
                step=100.0
            )

            deposit_button = st.form_submit_button(
                "Deposit Money"
            )

        if deposit_button:

            if amount <= 0:

                st.error("Enter a valid amount.")

            else:

                add_transaction(
                    account_no,
                    "Deposit",
                    amount
                )

                st.success(
                    f"₹{amount:,.2f} deposited successfully!"
                )

                st.rerun()


    # --------------------------------
    # WITHDRAW MONEY
    # --------------------------------

    elif menu == "Withdraw Money":

        st.subheader("➖ Withdraw Money")

        with st.form("withdraw_form"):

            amount = st.number_input(
                "Enter Withdrawal Amount (₹)",
                min_value=0.0,
                step=100.0
            )

            withdraw_button = st.form_submit_button(
                "Withdraw Money"
            )

        if withdraw_button:

            if amount <= 0:

                st.error("Enter a valid amount.")

            elif amount > balance:

                st.error("Insufficient Balance!")

            else:

                add_transaction(
                    account_no,
                    "Withdraw",
                    amount
                )

                st.success(
                    f"₹{amount:,.2f} withdrawn successfully!"
                )

                st.rerun()


    # --------------------------------
    # TRANSACTION HISTORY
    # --------------------------------

    elif menu == "Transaction History":

        st.subheader("📄 Transaction History")

        workbook = openpyxl.load_workbook(
            bank.FILE_NAME,
            data_only=True
        )

        sheet = workbook.active

        records = []

        for row in sheet.iter_rows(
            min_row=2,
            values_only=True
        ):

            if str(row[0]) == str(account_no):

                records.append([
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8]
                ])

        workbook.close()

        if records:

            df = pd.DataFrame(
                records,
                columns=[
                    "Transaction ID",
                    "Type",
                    "Amount",
                    "Previous Balance",
                    "Current Balance",
                    "Date-Time"
                ]
            )

            st.dataframe(
                df.iloc[::-1],
                use_container_width=True,
                hide_index=True
            )

            st.download_button(
                "⬇️ Download History",
                df.to_csv(index=False),
                file_name="transaction_history.csv",
                mime="text/csv"
            )

        else:

            st.info("No transactions found.")


# -----------------------------------
# FOOTER
# -----------------------------------


st.divider()

st.caption(
    "PREM BANK | Python Banking Management System"
)
