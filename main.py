from service.account_service import AccountService
from service.costumer_service import CostumerService
from entities.persons.costumer import Customer
from entities.accounts.saving_account import SavingsAccount
from entities.accounts.checking_account import CheckingAccount

def main():
    account_service = AccountService()
    customer_service = CostumerService()

    while True:
        print("\nMain Menu:")
        print("1. Create Savings Account")
        print("2. Create Checking Account")
        print("3. List Accounts")
        print("4. Add a New Customer")
        print("5. List All Customers")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Create Savings Account
            name = input("Enter customer's first name: ").strip()
            lastname = input("Enter customer's last name: ").strip()
            email = input("Enter customer's email: ").strip()
            customer_id = input("Enter customer ID: ").strip()
            balance = float(input("Enter account balance: "))
            interest_rate = float(input("Enter interest rate (%): "))

            customer = Customer(name, lastname, email, customer_id)
            account = SavingsAccount(customer, balance, interest_rate)
            account_service.add_account(account)
            print("Savings account created successfully!")

        elif choice == "2":
            # Create Checking Account
            name = input("Enter customer's first name: ").strip()
            lastname = input("Enter customer's last name: ").strip()
            email = input("Enter customer's email: ").strip()
            customer_id = input("Enter customer ID: ").strip()
            balance = float(input("Enter account balance: "))
            overdraft_limit = float(input("Enter overdraft limit: "))

            customer = Customer(name, lastname, email, customer_id)
            account = CheckingAccount(customer, balance, overdraft_limit)
            account_service.add_account(account)
            print("Checking account created successfully!")

        elif choice == "3":
            # List Accounts
            accounts = account_service.get_all_accounts()
            if accounts:
                print("\nAccounts:")
                for idx, account in enumerate(accounts, start=1):
                    print(f"{idx}. {account}")
            else:
                print("No accounts found.")

        elif choice == "4":
            # Add a New Customer
            name = input("Enter customer's first name: ").strip()
            lastname = input("Enter customer's last name: ").strip()
            email = input("Enter customer's email: ").strip()
            customer_id = input("Enter customer ID: ").strip()

            customer = Customer(name, lastname, email, customer_id)
            customer_service.add_customer(customer)
            print(f"Customer {name} {lastname} added successfully!")

        elif choice == "5":
            # List All Customers
            print("\nCustomers:")
            customer_service.list_customers()

        elif choice == "6":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
