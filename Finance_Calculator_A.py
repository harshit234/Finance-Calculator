"""
Personal Finance Calculator
Day 7 PM Take-Home Assignment
Author: Harshit Gautam
Description: Calculates financial breakdown with validation
and Indian number formatting.
"""


def format_indian_currency(amount: float) -> str:
    """
    Format number in Indian system (lakhs/crores).
    Example: 1200000 -> Rs. 12,00,000.00
    """
    amount_str = f"{amount:.2f}"
    integer_part, decimal_part = amount_str.split(".")

    if len(integer_part) <= 3:
        return f"Rs. {integer_part}.{decimal_part}"

    last_three = integer_part[-3:]
    remaining = integer_part[:-3]

    parts = []
    while len(remaining) > 2:
        parts.insert(0, remaining[-2:])
        remaining = remaining[:-2]

    if remaining:
        parts.insert(0, remaining)

    formatted_integer = ",".join(parts) + "," + last_three
    return f"Rs. {formatted_integer}.{decimal_part}"


def validate_inputs(
    salary: float,
    tax_percent: float,
    rent: float,
    savings_percent: float
) -> bool:
    """Validate all user inputs."""

    if salary <= 0:
        print("Salary must be greater than 0.")
        return False

    if not 0 <= tax_percent <= 50:
        print("Tax must be between 0 and 50.")
        return False

    if rent <= 0:
        print("Rent must be greater than 0.")
        return False

    if not 0 <= savings_percent <= 100:
        print("Savings percent must be between 0 and 100.")
        return False

    return True


def calculate_health_score(
    rent_ratio: float,
    savings_percent: float,
    disposable: float,
    net_salary: float
) -> float:
    """
    Calculate financial health score (0–100).
    """

    score = 0

    # Rent weight: 30 points
    if rent_ratio < 30:
        score += 30
    elif rent_ratio < 40:
        score += 20
    else:
        score += 10

    # Savings weight: 40 points
    score += min(savings_percent, 40)

    # Disposable weight: 30 points
    disposable_ratio = (disposable / net_salary) * 100
    score += min(disposable_ratio, 30)

    return round(score, 2)


def main():
    """Main execution function."""

    print("=" * 44)
    print("EMPLOYEE FINANCIAL SUMMARY GENERATOR")
    print("=" * 44)

    name = input("Employee Name: ")
    salary = float(input("Annual Salary: "))
    tax_percent = float(input("Tax % (0-50): "))
    rent = float(input("Monthly Rent: "))
    savings_percent = float(input("Savings % (0-100): "))

    if not validate_inputs(salary, tax_percent, rent, savings_percent):
        return

    monthly_salary = salary / 12
    monthly_tax = monthly_salary * (tax_percent / 100)
    net_salary = monthly_salary - monthly_tax
    rent_ratio = (rent / net_salary) * 100
    savings = net_salary * (savings_percent / 100)
    disposable = net_salary - rent - savings

    annual_tax = monthly_tax * 12
    annual_savings = savings * 12
    annual_rent = rent * 12

    health_score = calculate_health_score(
        rent_ratio, savings_percent, disposable, net_salary
    )

    print("\n" + "=" * 44)
    print("EMPLOYEE FINANCIAL SUMMARY")
    print("=" * 44)

    print(f"Employee : {name}")
    print(f"Annual Salary : {format_indian_currency(salary)}")
    print("-" * 44)

    print("Monthly Breakdown:")
    print(f"Gross Salary : {format_indian_currency(monthly_salary)}")
    print(f"Tax ({tax_percent}%) : {format_indian_currency(monthly_tax)}")
    print(f"Net Salary : {format_indian_currency(net_salary)}")
    print(
        f"Rent : {format_indian_currency(rent)} "
        f"({rent_ratio:.1f}% of net)"
    )
    print(f"Savings ({savings_percent}%) : {format_indian_currency(savings)}")
    print(f"Disposable : {format_indian_currency(disposable)}")

    print("-" * 44)
    print("Annual Projection:")
    print(f"Total Tax : {format_indian_currency(annual_tax)}")
    print(f"Total Savings : {format_indian_currency(annual_savings)}")
    print(f"Total Rent : {format_indian_currency(annual_rent)}")
    print("-" * 44)
    print(f"Financial Health Score: {health_score} / 100")
    print("=" * 44)


if __name__ == "__main__":
    main()
