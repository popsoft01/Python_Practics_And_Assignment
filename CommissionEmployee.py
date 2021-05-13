from decimal import Decimal


class CommissionEmployee:

    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate):
        self._firstName = first_name
        self._lastName = last_name
        self._ssn = ssn
        self.gross_sales = gross_sales
        self.commission_rate = commission_rate

    @property
    def first_name(self):
        return self._firstName

    @property
    def last_name(self):
        return self._lastName

    @property
    def ssn(self):
        return self._ssn

    @property
    def gross_sale(self):
        return self.gross_sales

    @gross_sale.setter
    def gross_sale(self, sales):
        if sales < Decimal('0.00'):
            raise ValueError('Gross sales must be >= to 0')

        self.gross_sales = sales

    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, rate):
        if not (Decimal('0.00') < rate < Decimal('1.0')):
            raise ValueError('Interest rate must be greater than 0 and less than 1')

        self._commission_rate = rate

    def earning(self):
        return self.gross_sales * self.commission_rate

    def __repr__(self):
        return 'CommissionEmployee: ' + f'{self.first_name} {self.last_name}\n' + f'social security number: {self.ssn}\n' + f'gross sales: {self.gross_sales:.2f}\n' + f'commission rate: {self.commission_rate:.2f}'


