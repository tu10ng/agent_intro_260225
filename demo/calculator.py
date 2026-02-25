"""
Simple Calculator - Demo for AI Agent presentation
This calculator only has add and subtract functions.
"""


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def main():
    """Interactive calculator demo."""
    print("Simple Calculator")
    print("=" * 30)
    print("Available operations: add, subtract")
    print()

    # Demo calculations
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"100 + 25 = {add(100, 25)}")
    print(f"50 - 18 = {subtract(50, 18)}")


if __name__ == "__main__":
    main()
