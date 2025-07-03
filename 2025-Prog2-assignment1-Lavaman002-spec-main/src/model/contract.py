from .property import Property
from datetime import date
from .owner import Owner

class Contract ():
    def __init__(self, contract_id :int , start_date : date, end_date : date ,commission_rate: float , property: Property , owner: Owner):
        self.contract_id = contract_id
        self.start_date = start_date
        self.end_date = end_date
        self.commission_rate = commission_rate
        self.property = property
        self.owner = owner
    def is_active(self) -> bool:
        today = date.today()
        if self.start_date <= today <= self.end_date:
            return True
        else:
            return False
    def calculate_commission(self) -> float:
        return self.commission_rate * self.property.price
