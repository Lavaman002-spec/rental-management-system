from datetime import date

class Payment:
    def __init__(self, payment_id: int, amount: float, payment_date: date, contract, status: str):
        self.payment_id = payment_id
        self.amount = amount
        self.payment_date = payment_date
        self.contract = contract
        self.status = status

    def is_late(self) -> bool:
        return self.payment_date > self.contract.end_date


class LatePayment(Payment):
    def __init__(self, payment_id: int, amount: float, payment_date: date, contract, status: str, penalty_fee: float):
        super().__init__(payment_id, amount, payment_date, contract, status)
        self.penalty_fee = penalty_fee

    def calculate_penalty(self) -> float:
        if self.is_late():
            days_late = (self.payment_date - self.contract.end_date).days
            return self.penalty_fee * days_late
        return 0.0

