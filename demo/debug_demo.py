"""
Debug Demo - Order Processing Module
This file is used to demonstrate debugging with Claude Code.

The file intentionally contains bugs that can be found through logging:
1. Division by zero in calculate_discount
2. KeyError when accessing missing fields
3. Type error with None values

Task for demo: Add logging and fix the bugs
"""

from datetime import datetime
from typing import Optional


class Order:
    """Represents a customer order."""

    def __init__(self, order_id: str, customer_id: str, items: list):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items  # List of {"name": str, "price": float, "quantity": int}
        self.created_at = datetime.now()
        self.discount_percent = 0
        self.status = "pending"

    def calculate_total(self) -> float:
        """Calculate total before discount."""
        total = 0
        for item in self.items:
            # Bug: Will fail if price or quantity is missing
            total += item["price"] * item["quantity"]
        return total

    def calculate_discount(self, member_points: int) -> float:
        """Calculate discount based on member points."""
        # Bug: Division by zero if member_points is 0
        discount_rate = 100 / member_points
        return min(discount_rate, 20)  # Max 20% discount

    def apply_discount(self, discount_percent: float) -> None:
        """Apply discount to the order."""
        self.discount_percent = discount_percent

    def get_final_price(self) -> float:
        """Get final price after discount."""
        total = self.calculate_total()
        # Bug: Will fail if discount_percent is None
        discount = total * (self.discount_percent / 100)
        return total - discount


def process_order(order_data: dict) -> Optional[Order]:
    """Process an incoming order."""
    # Bug: No validation of order_data structure
    order = Order(
        order_id=order_data["order_id"],
        customer_id=order_data["customer_id"],
        items=order_data["items"]
    )

    # Get member points (might be None or missing)
    member_points = order_data.get("member_points")

    if member_points:
        # Bug: This can fail if member_points is 0 (falsy but valid)
        discount = order.calculate_discount(member_points)
        order.apply_discount(discount)

    order.status = "processed"
    return order


def main():
    """Demo the order processing - will encounter bugs."""
    print("Order Processing Demo")
    print("=" * 40)

    # Test case 1: Normal order
    print("\n[Test 1] Normal order:")
    order1_data = {
        "order_id": "ORD001",
        "customer_id": "CUST001",
        "items": [
            {"name": "Laptop", "price": 999.99, "quantity": 1},
            {"name": "Mouse", "price": 29.99, "quantity": 2}
        ],
        "member_points": 500
    }
    try:
        order1 = process_order(order1_data)
        print(f"  Total: ${order1.get_final_price():.2f}")
        print(f"  Discount: {order1.discount_percent:.1f}%")
    except Exception as e:
        print(f"  Error: {e}")

    # Test case 2: Order with missing price (will fail)
    print("\n[Test 2] Order with missing price:")
    order2_data = {
        "order_id": "ORD002",
        "customer_id": "CUST002",
        "items": [
            {"name": "Keyboard", "quantity": 1}  # Missing price!
        ],
        "member_points": 100
    }
    try:
        order2 = process_order(order2_data)
        print(f"  Total: ${order2.get_final_price():.2f}")
    except Exception as e:
        print(f"  Error: {type(e).__name__}: {e}")

    # Test case 3: Order with zero member points (will fail)
    print("\n[Test 3] Order with zero member points:")
    order3_data = {
        "order_id": "ORD003",
        "customer_id": "CUST003",
        "items": [
            {"name": "USB Cable", "price": 9.99, "quantity": 3}
        ],
        "member_points": 0  # Zero points - division by zero!
    }
    try:
        order3 = process_order(order3_data)
        print(f"  Total: ${order3.get_final_price():.2f}")
    except Exception as e:
        print(f"  Error: {type(e).__name__}: {e}")

    # Test case 4: Order without member points
    print("\n[Test 4] Order without member points:")
    order4_data = {
        "order_id": "ORD004",
        "customer_id": "CUST004",
        "items": [
            {"name": "Headphones", "price": 79.99, "quantity": 1}
        ]
        # No member_points key
    }
    try:
        order4 = process_order(order4_data)
        print(f"  Total: ${order4.get_final_price():.2f}")
        print(f"  No discount applied")
    except Exception as e:
        print(f"  Error: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
