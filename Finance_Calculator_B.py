"""
Personal Finance Calculator - Part B
Includes:
- Indian number formatting
- Two employee comparison
- Financial health score
"""


def format_indian_currency(amount: float) -> str:
    """Format number in Indian system (lakhs/crores)."""
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
    """Validate user inputs."""

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
    """Calculate financial health score (0–100)."""

    score = 0

    if rent_ratio < 30:
        score += 30
    elif rent_ratio < 40:
        score += 20
    else:
        score += 10

    score += min(savings_percent, 40)

    disposable_ratio = (disposable / net_salary) * 100
    score += min(disposable_ratio, 30)

    return round(score, 2)


def calculate_financials(name: str) -> dict:
    """Collect input and calculate financial metrics."""

    print(f"\nEnter details for {name}")
    salary = float(input("Annual Salary: "))
    tax_percent = float(input("Tax % (0-50): "))
    rent = float(input("Monthly Rent: "))
    savings_percent = float(input("Savings % (0-100): "))

    if not validate_inputs(salary, tax_percent, rent, savings_percent):
        raise ValueError("Invalid input provided.")

    monthly_salary = salary / 12
    monthly_tax = monthly_salary * (tax_percent / 100)
    net_salary = monthly_salary - monthly_tax
    rent_ratio = (rent / net_salary) * 100
    savings = net_salary * (savings_percent / 100)
    disposable = net_salary - rent - savings

    health_score = calculate_health_score(
        rent_ratio, savings_percent, disposable, net_salary
    )

    return {
        "name": name,
        "net_salary": net_salary,
        "rent_ratio": rent_ratio,
        "savings_percent": savings_percent,
        "disposable": disposable,
        "health_score": health_score
    }


def print_comparison(emp1: dict, emp2: dict) -> None:
    """Print side-by-side comparison."""

    print("\n" + "=" * 70)
    print("EMPLOYEE FINANCIAL COMPARISON")
    print("=" * 70)

    print(
        f"{'Metric':<20}"
        f"{emp1['name']:<25}"
        f"{emp2['name']:<25}"
    )
    print("-" * 70)

    print(
        f"{'Net Salary':<20}"
        f"{format_indian_currency(emp1['net_salary']):<25}"
        f"{format_indian_currency(emp2['net_salary']):<25}"
    )

    print(
        f"{'Rent Ratio %':<20}"
        f"{emp1['rent_ratio']:<25.1f}"
        f"{emp2['rent_ratio']:<25.1f}"
    )

    print(
        f"{'Savings %':<20}"
        f"{emp1['savings_percent']:<25}"
        f"{emp2['savings_percent']:<25}"
    )

    print(
        f"{'Disposable':<20}"
        f"{format_indian_currency(emp1['disposable']):<25}"
        f"{format_indian_currency(emp2['disposable']):<25}"
    )

    print(
        f"{'Health Score':<20}"
        f"{emp1['health_score']:<25}"
        f"{emp2['health_score']:<25}"
    )

    print("=" * 70)


def main():
    """Main execution."""

    print("=" * 44)
    print("TWO EMPLOYEE FINANCE COMPARISON TOOL")
    print("=" * 44)

    name1 = input("Employee 1 Name: ")
    emp1 = calculate_financials(name1)

    name2 = input("\nEmployee 2 Name: ")
    emp2 = calculate_financials(name2)

    print_comparison(emp1, emp2)


if __name__ == "__main__":
    main()
