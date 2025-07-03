# Rental Management System 

This is a university project built using Object-Oriented Programming (OOP) principles in Python. It simulates the workflow of a property rental company by managing residents, properties, contracts, payments, and more.

## 📌 Main Features

- Manage residents and lease contracts
- Handle monthly payments and apply late fees
- Track complaints and maintenance requests
- Log events and simulate notifications
- Admin and Property Manager roles
- Generate reports (occupancy, revenue, etc.)
- Tested with PyTest for correctness

##  Technologies Used

- Python 3.x
- OOP principles
- PyTest (unit testing)
- UML (class diagram included)

## Project Structure
![image](https://github.com/user-attachments/assets/438e1bce-e47e-46b5-8ad8-5bf38834fae9)


🛠 Task 1: Basic Class Structure
Define the Class Structure based on the UML diagram (The given UML class diagram must be entirely implemented, additional classes are permitted)

Implement all the classes, with the correct relationships between them.
Implement the basic functionality, demonstrating lease management, including creating, renewing, and terminating leases.
Deliverables: Python files with class definitions and inheritance properly structured.

🛠 Task 2: Payment System
Implement Payment class to track rent payments, including amount, date, and status.
Create LatePayment (inherits from Payment) to handle overdue payments with penalties.
Implement a TransactionHistory class to store all payment transactions.
Write a method to check unpaid rent and notify residents.
Deliverables: A script that processes rent payments, identifies late payments, calculates total revenue.

🛠 Task 3: Property Maintenance & Renovations
Create a MaintenanceRequest class to handle repair requests.
Implement a Renovation class to track renovation history and costs.
Allow a property manager to approve or reject maintenance requests.
Deliverables: A maintenance management script that handles submitting and resolving requests.

🛠 Task 4: Analytics & Reports
Write methods to analyze data and generate reports:
Calculate the percentage of vacant properties (RentalAnalytics.vacancy_rate()).
Calculate total rental income per month (RentalAnalytics.average_rent()).
Identify the number of rental turnovers per month (RentalAnalytics.tenant_turnover_rate()).
Calculate the financial loss from vacant properties (RentalAnalytics.loss_due_to_vacancy()).
Generate a monthly report (MonthlyReport.generate_report()).
Deliverables: A script that prints analytics reports for a given month/year.

🛠 Task 5: Searching & Navigation
Implement PropertySearch with methods: search_by_location(), search_by_price(), search_by_availability().
Implement Navigation to help find the nearest available property.
Deliverables: A search function where users can find available properties based on criteria.

🛠 Task 6: Event Logging & Notifications
Implement an EventLog to record system events (e.g., lease signed, rent paid).
Implement Notification to send messages for lease expirations, late payments, etc.
Deliverables: A script that sends notifications to renters about late payments.

🛠 Task 7: Reviews & Complaints System
Create a Review class to allow residents to rate properties.
Implement a Complaint system where renters can file complaints.
Deliverables: A review and complaint submission system.

