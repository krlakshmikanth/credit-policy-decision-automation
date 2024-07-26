class CreditApplication:
    def __init__(self, name, age, income, employment_duration, credit_score, payment_history, existing_debt, recent_credit_checks):
        self.name = name
        self.age = age
        self.income = income
        self.employment_duration = employment_duration
        self.credit_score = credit_score
        self.payment_history = payment_history
        self.existing_debt = existing_debt
        self.recent_credit_checks = recent_credit_checks

    def evaluate_application(self):
        # Pre-selection criteria
        if self.age < 18:
            return f"Application rejected: {self.name} is under 18."

        if self.income < 25000:
            return f"Application rejected: {self.name}'s income is below the minimum requirement."

        if self.employment_duration < 6:
            return f"Application rejected: {self.name}'s employment duration is less than 6 months."

        # Debt-to-Income Ratio Calculation
        dti_ratio = self.existing_debt / self.income
        if dti_ratio > 0.4:
            return f"Application rejected: {self.name}'s debt-to-income ratio ({dti_ratio:.2%}) is too high."

        # Creditworthiness assessment
        if self.credit_score < 670:
            return f"Application rejected: {self.name}'s credit score is below the threshold."

        if self.payment_history > 3:  # Allow up to 3 missed payments for approval
            return f"Application rejected: {self.name} has too many missed payments."

        if self.recent_credit_checks > 3:
            return f"Application rejected: {self.name} has too many recent credit checks."

        # Determine interest rate
        interest_rate = 5.0  # Base interest rate
        if self.credit_score > 740:
            interest_rate -= 0.5
        if self.payment_history > 0:  # Increase interest rate for any missed payments
            interest_rate += 1.0
        if self.existing_debt > 5000:
            interest_rate += 1.0

        # Monthly interest rate (2% monthly)
        monthly_interest_rate = 2 / 100

        # Determine maximum monthly repayment based on income
        max_monthly_repayment = self.income * 0.4 / 12

        # Calculate maximum credit limit based on monthly repayment and interest rate
        n = 12  # Assuming a 1-year term for simplicity
        max_credit_limit = (max_monthly_repayment * ((1 + monthly_interest_rate)**n - 1)) / (monthly_interest_rate * (1 + monthly_interest_rate)**n)

        # Approval decision
        if max_credit_limit > 0:
            return f"Application approved for {self.name} with a credit limit of ${max_credit_limit:.2f} and an interest rate of {interest_rate:.2f}%. Debt-to-Income Ratio: {dti_ratio:.2%}."
        else:
            return f"Application rejected: {self.name} cannot be granted any credit limit based on current criteria."

# Create instances for each scenario

# Scenario 1: Approved Application
applicant_approved = CreditApplication(
    name="John Doe",
    age=30,
    income=60000,
    employment_duration=12,
    credit_score=750,
    payment_history=0,
    existing_debt=1000,
    recent_credit_checks=1
)

# Scenario 2: Approved Application with Increased Interest Rate
applicant_approved_high_interest = CreditApplication(
    name="Jane Smith",
    age=28,
    income=70000,
    employment_duration=24,
    credit_score=700,
    payment_history=2,  # Two missed payments, leading to a higher interest rate
    existing_debt=20000,  # More debt but still within acceptable DTI
    recent_credit_checks=1
)

# Scenario 3: Application Rejected due to High Debt-to-Income Ratio
applicant_rejected_debt_ratio = CreditApplication(
    name="Mark Johnson",
    age=35,
    income=50000,
    employment_duration=8,
    credit_score=680,
    payment_history=1,
    existing_debt=25000,  # High debt compared to income
    recent_credit_checks=2
)

# Run evaluations
print(applicant_approved.evaluate_application())
print(applicant_approved_high_interest.evaluate_application())
print(applicant_rejected_debt_ratio.evaluate_application())