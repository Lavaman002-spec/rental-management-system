from .property import Property
from.contract import Contract
class RentalCompany():

    # Your code goes here.
    company_name: str = "Nordis"
    properties_list: list = []
    contracts: list = []

    def __init__(self):
        pass

    def add_property(self, property: Property):
        if property not in RentalCompany.properties_list:
            RentalCompany.properties_list.append(property)
            print(f"Property {property.property_id} added to {RentalCompany.company_name}.")
        else:
            print("Property already in the company.")
    def remove_property(self, property: Property):
        if property in RentalCompany.properties_list:
            RentalCompany.properties_list.remove(property)
        else:
            print("Property not in the company.")
    def get_income(self) -> float:
        total_income = 0.0
        for contract in self.contracts:
            if contract.is_active():
                total_income += contract.calculate_commission()
        return total_income

    def analyze_occupancy(self) -> float:
        total_properties = len(self.properties_list)
        if total_properties == 0:
            return 0.0
        occupied_properties = 0
        for property in self.properties_list:
            if property.is_occupied:
                occupied_properties += 1

        occupancy_rate = (occupied_properties / total_properties) * 100

        return occupancy_rate
