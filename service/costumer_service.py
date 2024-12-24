class CostumerService:
    def __init__(self):
        # Initialize an empty list to store customers
        self.customers = []
        
    def add_customer(self, customer):
        """
        Add a new customer to the customers list.
        
        Args:
            customer: An instance of Customer.
        """
        self.customers.append(customer)
        print(f"Customer {customer.firstname} {customer.lastname} added successfully!")

    def list_customers(self):
        """
        List all customers in the service.
        """
        if not self.customers:
            print("No customers found.")
        else:
            for idx, customer in enumerate(self.customers, start=1):
                print(f"{idx}. {customer}")