class AccountService:
    def __init__(self):
        # Initialize an empty list to store accounts
        self.accounts = []

    def add_account(self, account):
        """
        Add a new account to the accounts list.
        
        Args:
            account: An instance of Account or its subclasses.
        """
        self.accounts.append(account)

    def get_all_accounts(self):
        """
        Retrieve all accounts stored in the service.
        
        Returns:
            list: A list of account instances.
        """
        return self.accounts

    def find_account_by_owner(self, owner_name):
        """
        Find accounts by the owner's name.
        
        Args:
            owner_name (str): The name of the account owner to search for.
        
        Returns:
            list: A list of accounts belonging to the owner.
        """
        return [account for account in self.accounts if account.owner.name.lower() == owner_name.lower()]

    def delete_account(self, account):
        """
        Delete an account from the accounts list.
        
        Args:
            account: The account instance to remove.
        """
        if account in self.accounts:
            self.accounts.remove(account)

    def update_account_balance(self, account, new_balance):
        """
        Update the balance of an existing account.
        
        Args:
            account: The account instance whose balance needs to be updated.
            new_balance (float): The new balance to set.
        """
        if account in self.accounts:
            account.balance = new_balance
