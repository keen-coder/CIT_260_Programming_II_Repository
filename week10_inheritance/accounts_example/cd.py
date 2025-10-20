from savings_account import SavingsAccount
# The CD account represents a certificate of
# deposit (CD) account. It is a subclass of
# the SavingsAccount class.

class CD(SavingsAccount):

    # The init method accepts arguments for the
    # account number, interest rate, balance, and
    # maturity date.
    
    def __init__(self, account_num, int_rate, bal, mat_date):
        # Call the superclass __init__ method.
        super().__init__(self, account_num, int_rate, bal)

        # Initialize the __maturity_date attribute.
        self.__maturity_date = mat_date

    # The set_maturity_date is a mutator for the
    # __maturity_date attribute.

    def set_maturity_date(self, mat_date):
        self.__maturity_date = mat_date

    # The get_maturity_date method is an accessor
    # for the __maturity_date attribute.

    def get_maturity_date(self):
        return self.__maturity_date
