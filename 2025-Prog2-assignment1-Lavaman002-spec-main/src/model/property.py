from .owner import Owner
class Property():
    def __init__(self, property_id: int, address: str, size: float, price: float , owner: Owner ):
        self.property_id = property_id
        self.address = address
        self.size = size
        self.facilities = []
        self.price = price
        self.history = []  #not impl in __init__ cuz a new prop will not have a history or be occupied yet when created
        self.is_occupied = False
        self.owner = owner
        owner.properties_owned.append(self)
        # self.facilities = []
        # self.hystory = []

    def get_status(self):
        def get_status(self) -> str:
            return "Occupied" if self.is_occupied else "Vacant"

    def calculate_cost(self) -> float:    # TODO: Add facilities and maintenance cost later
        price_per_sqm = 14  # 14€/sqm
        cost = self.size * price_per_sqm
        return cost
    # def add_facility(self, facility) -> list:    #TODO EVENTS WILL WORK WITH THIS LAST DEFS
    #     self.facilities.append(facility)

    # def add_hystory(self, hystory) -> list:
    #     self.hystory.append(hystory)
    #
    # def get_facilities(self) -> list:
    #     return self.facilities                    #Todo impl them when I finish event
    #
    # def get_history(self) -> list:
    #     return self.history





