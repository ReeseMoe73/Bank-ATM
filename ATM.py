class ATM:
    def __init__(self):
        # Sample data of cards with PINs and balances
        self.cards = {
            "1234567890": {"pin": "1234", "balance": 700.0},  # Valid card
            "0981964321": {"pin": "5678", "balance": 0.0}  # Zero balance card
        }
        self.current_card = None

    def validate_card(self, card_number):
        # Check if the card exists
        if card_number in self.cards:
            self.current_card = card_number
            return True
        else:
            print("Invalid card. Ejecting card.")
            return False

    def validate_pin(self, pin):
        # Allow up to 3 attempts to enter the correct PIN
        attempts = 3
        while attempts > 0:
            if pin == self.cards[self.current_card]["pin"]:
                return True
            else:
                attempts -= 1
                if attempts > 0:
                    pin = input(f"Incorrect PIN. You have {attempts} attempt(s) left. Please try again: ")
                else:
                    print("Incorrect PIN entered 3 times. Ejecting card.")
                    return False

    def select_transaction(self):
        # Prompt the user to select a transaction
        transaction = input("Select transaction: 1 - Withdraw Money: ")
        if transaction == "1":
            return True
        else:
            print("Invalid transaction. Ejecting card.")
            return False

    def withdraw_money(self):
        # Check if the account has a balance
        balance = self.cards[self.current_card]["balance"]
        if balance <= 0:
            print("Insufficient balance. Ejecting card.")
            return False

        # Get withdrawal amount
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid amount entered. Ejecting card.")
            return False

        if amount > balance:
            print("Insufficient balance for this amount. Ejecting card.")
            return False
        else:
            self.cards[self.current_card]["balance"] -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.cards[self.current_card]['balance']}")
            return True

    def print_receipt(self):
        # Print transaction receipt
        print("Transaction complete. Printing receipt...")

    def eject_card(self):
        # Eject card
        print("Ejecting card.")
        self.current_card = None

    def run(self):
        # Start the ATM operation
        card_number = input("Please insert your card (enter card number): ")

        if not self.validate_card(card_number):
            self.eject_card()
            return

        pin = input("Enter your PIN: ")

        if not self.validate_pin(pin):
            self.eject_card()
            return

        if not self.select_transaction():
            self.eject_card()
            return

        if not self.withdraw_money():
            self.eject_card()
            return

        self.print_receipt()
        self.eject_card()


# Create an instance of ATM and run it
atm = ATM()
atm.run()
