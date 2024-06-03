class Account:
    def __init__ (self, number, pin,owner_details,min_balance=10,recipient=None):
        self.number = number
        self.__pin = pin
        self.__balance = 0
        self.owner_details = owner_details
        self.transaction_history = [] 
        self.annual_interest_rate = 0.02 
        self.is_frozen = False
        self.min_balance = min_balance
        self.recipient = recipient 
        
    def show_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Wrong pin"
        
    #  Q1 Method to be able to deposit
        
    def deposit(self, amount, pin):
        if pin == self.__pin:
            self.__balance += amount
            return f"Deposit successful. New balance: {self.__balance}"
        else:
            return "Wrong pin"

    #  Method to withdraw money from the account
    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if self.__balance >= amount:
                self.__balance -= amount
                return f"Withdrawal successful. New balance: {self.__balance}"
            else:
                return "Insufficient funds"
        else:
            return "Wrong pin"
        
#   q2 Method to display the account owner's details and current balance.
    def display_account_info(self, pin):
        if pin == self.__pin:
            return f"Account Number: {self.number}\nOwner Details: {self.owner_details}\nCurrent Balance: {self.__balance}"
        else:
            return "Wrong pin"
        
    
     # q3# Method to update the account owner's information
    def update_owner_details(self, new_owner_details, pin):
        if pin == self.__pin:
            self.owner_details = new_owner_details
            return "Owner details updated successfully."
        else:
            return "Wrong pin"
        
    # Q4 Method to generate a statement of recent transactions
    def generate_transaction_statement(self, pin):
        if pin == self.__pin:
            statement = "Transaction Statement:\n"
            for transaction in reversed(self.transaction_history):
                statement += f"{transaction[0]} of {transaction[1]} on {transaction[2].strftime('%Y-%m-%d %H:%M')}\n"
            return statement
        else:
            return "Wrong pin"
    # Q5: Method to set an overdraft limit for the account.
        
    def set_overdraft_limit(self, new_limit, pin):
        if pin == self.__pin:
            self.overdraft_limit = new_limit
            return "Overdraft limit updated successfully."
        else:
            return "Wrong pin"
    # q6 Method to calculate and apply interest to the balance.
    def apply_interest(self, pin):
        if pin == self.__pin:
            # Calculate interest for one year
            interest_amount = self.__balance * self.annual_interest_rate
            # Apply interest to the balance
            self.__balance += interest_amount
            return f"Interest applied. New balance: {self.__balance}"
        else:
            return "Wrong pin"
    # q7 Methods to freeze and unfreeze the account for security reasons.
    def freeze_account(self, pin):
        if pin == self.__pin:
            self.is_frozen = True
            return "Account has been frozen."
        else:
            return "Wrong pin"

    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.is_frozen = False
            return "Account has been unfrozen."
        else:
            return "Wrong pin"

    def is_active(self, pin):
        if pin == self.__pin:
            return not self.is_frozen
        else:
            return False
        
    # q8 Method to retrieve the history of all transactions made on the account.
    def get_transaction_history(self, pin):
        if self.is_active(pin):
            return self.transaction_history
        else:
            return "Account is frozen."
    # q9 Method to enforce a minimum balance requirement
    def check_minimum_balance_requirement(self, pin):
        if self.is_active(pin):
            if self.__balance >= self.min_balance:
                return "Your account meets the minimum balance requirement."
            else:
                return "Your account does not meet the minimum balance requirement."
        else:
            return "Account is frozen."
    
    # q10   Method to transfer funds from one account to another.


def transfer_funds(self, amount, recipient_number):
        if self.__pin == self.__pin:  # Corrected typo here; compare with itself
            if self.is_active() and self.__balance >= amount:
                if self.__balance - amount < self.min_balance:
                    return "Transfer would cause insufficient funds."
                else:
                    self.__balance -= amount
                    self.transaction_history.append(("Transfer Outgoing", -amount))
                    # Validate and handle the recipient account appropriately
                    if self.validate_recipient(recipient_number):
                        self.recipient.deposit(amount, self.__pin)
                        self.recipient.transaction_history.append(("Transfer Incoming", amount))
                        return f"Transfer successful. New balance: {self.__balance}. Recipient's new balance: {self.recipient.show_balance(self.__pin)}."
                    else:
                        return "Invalid recipient account number."
            else:
                return "Insufficient funds or account is frozen."
        else:
            return "Wrong pin"

def validate_recipient(self, recipient_number):
        return self.number == recipient_number

# q11 Method to close the account and perform necessary cleanup.
def close_account(self, pin):
        if pin == self.__pin:
            if self.is_active():  #  to check if the account is active before closing
                self.__balance = 0  # to Clear any remaining balance
                self.transaction_history.clear()  #to Clear transaction history
                self.owner_details = None  #  toOptionally clear sensitive details
                self.is_frozen = True  #to  Mark the account as frozen/closed
                return "Account closed successfully."
            else:
                return "Account is already closed or frozen."
        else:
            return "Wrong pin"

