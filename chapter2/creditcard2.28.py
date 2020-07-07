class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.

        The initial balance is zero.

        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        try:
            float(price)
            if price + self._balance > self._limit:  # if charge would exceed limit,
                return False  # cannot accept charge
            else:
                self._balance += price
                return True
        except ValueError:
            print('charge function need a numerical input')

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        try:
           # float(amount)
            if amount < 0.:
                raise ValueError('amount must be a positive number')
            self._balance -= amount
        except TypeError:
            print('make_payment need a numerical input')

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit,apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr=apr
        self._time=0

    def charge(self):
        self._time+=1
        success=super().charge()
        if not success:
            self._balance+=5
        return success

    def process_month(self):
        fee=max(0,self._time-10)
        if self._balance>0:
            monthly_factor=pow(1+self._apr,1/12)
            self._balance=(self._balance+fee)*monthly_factor
        self.time=0    

if __name__ == '__main__':

