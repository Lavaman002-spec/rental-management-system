from datetime import date
from model.contract import Contract
from model.owner import Owner
from model.property import Property
from model.payment import LatePayment



def identify_late_payments(payments: list):
    late_payments = []
    for payment in payments:
        penalty = payment.calculate_penalty()
        if penalty > 0:
            days_late = (payment.payment_date - payment.contract.end_date).days
            print(f"Payment ID {payment.payment_id} is late by {days_late} days. Penalty: {penalty}")
            late_payments.append((payment, days_late, penalty))
    return late_payments


def calculate_total_revenue(payments: list) -> float:
    total = sum(p.amount for p in payments if p.status == "paid")
    print(f"Total revenue: €{total}")
    return total


if __name__ == "__main__":
    # Setup test data
    owner = Owner(1, "Test Owner", "test@email.com")
    prop = Property(1, "Test Street", 100.0, 1200.0, owner)

    contract = Contract(
        contract_id=1,
        start_date=date(2025, 1, 1),
        end_date=date(2025, 3, 1),
        commission_rate=0.1,
        property=prop,
        owner=owner
    )

    payment1 = LatePayment(1, 1000.0, date(2025, 3, 5), contract, "paid", penalty_fee=20)
    payment2 = LatePayment(2, 1000.0, date(2025, 2, 28), contract, "paid", penalty_fee=20)

    identify_late_payments([payment1, payment2])
    calculate_total_revenue([payment1, payment2])
