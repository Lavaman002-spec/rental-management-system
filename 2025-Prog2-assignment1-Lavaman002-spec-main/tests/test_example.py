# from src.model.rentalcompany import RentalCompany
#
# def test_rental_company():
#     company = RentalCompany("Test Company")
#     assert company.name == "Test Company"
#     assert isinstance(company, RentalCompany)
#
#     assert False, "This was just an example. Add more tests here"
# -------------------------------------------------
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))# Hey, also look in src/ when searching for modules.
from datetime import date
from model.owner import Owner
from model.contract import Contract
from model.property import Property
from model.rentalcompany import RentalCompany
from model.payment import LatePayment


def test_contract_methods():
    print("Test started")
    owner1 = Owner(owner_id=1, name="Manu Carbasanu", contact_info="john@example.com")
    print("✅ Owner created")
    property1 = Property(1, "Main St", 100.0, 1500.0 , owner1)
    print("✅ Property created")
    contract = Contract(
        contract_id=101,
        property=property1,
        start_date=date(2024, 1, 1),
        end_date=date(2025, 12, 31),
        commission_rate=0.1,
        owner = owner1
    )

    # Test is_active() should be True
    assert contract.is_active() is True
    print("Is contract active:", contract.is_active())
    # Test calculate_commission() should return 150.0
    assert contract.calculate_commission()

    print("Calculated commission:", contract.calculate_commission())

    assert property1 in owner1.get_properties()
    print(f"Owner:{owner1.name} owns property: {property1.address}✅  ")

    # ---------------------------Testing rental company -----------------------------
def test_rental_company_methods():
    print(" Testing RentalCompany methods...")

    owner = Owner(2, "Ana Smith", "ana@example.com")
    company = RentalCompany()

    prop1 = Property(101, "1st Avenue", 80.0, 1000.0, owner)
    prop2 = Property(102, "2nd Street", 120.0, 2000.0, owner)
    prop3 = Property(103, "3rd Blvd", 60.0, 800.0, owner)

    # Make 2 out of 3 occupied
    prop1.is_occupied = True
    prop2.is_occupied = False
    prop3.is_occupied = True

    # Add to company
    company.add_property(prop1)
    company.add_property(prop2)
    company.add_property(prop3)

    # Add some contracts
    contract1 = Contract(
        contract_id=201,
        property=prop1,
        start_date=date(2024, 1, 1),
        end_date=date(2024, 12, 31),
        commission_rate=0.1,
        owner=owner
    )
    contract2 = Contract(
        contract_id=202,
        property=prop1,
        start_date=date(2024, 1, 1),
        end_date=date(2024, 12, 31),
        commission_rate=0.1,
        owner=owner
    )

    company.contracts.append(contract1)
    company.contracts.append(contract2)
    print(f"Contract {contract1.contract_id} added: {contract1.property.address}, Commission: {contract1.calculate_commission()}")
    print("Company contracts:")
    for contract in company.contracts:
        print(f"- Contract {contract.contract_id} with property {contract.property.address} (Owner: {contract.owner.name})")
    # Test occupancy analysis
    occupancy = company.analyze_occupancy()
    print(f"📊 Occupancy rate is: {occupancy}%")

def test_owner_method():
    owner = Owner(owner_id=1, name="Manu Carbasanu", contact_info="secic@gmail.com")

    prop1 = Property(101, "Main St", 100.0, 1500.0, owner)
    prop2 = Property(102, "Elm St", 80.0, 1200.0, owner)

    properties = owner.get_properties()
    print("Test passed. Properties owned:", properties)

#------------------------- late payment -----------------------t`

def create_mock_contract(end_date: date) -> Contract:
    owner = Owner(1, "Test Owner", "owner@example.com")
    prop = Property(1, "Test St", 100.0, 1500.0, owner)
    return Contract(
        contract_id=999,
        start_date=date(2025, 1, 1),
        end_date=end_date,
        commission_rate=0.1,
        property=prop,
        owner=owner
    )



#have a finatical to use module in __init__ file
#calculate total revenue in lease agreement to make it eaiser
