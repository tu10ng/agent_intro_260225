"""
Plan Mode Demo - User Service Module
This file is used to demonstrate Claude Code's /plan mode.

The file intentionally has some issues that can be improved:
1. Long function with repeated logic
2. No logging
3. Mixed responsibilities

Task for demo: Use /plan to add logging functionality
"""

import json
from datetime import datetime
from typing import Optional


# Simulated user database
_users_db = {
    "user_001": {"name": "Alice", "email": "alice@example.com", "status": "active"},
    "user_002": {"name": "Bob", "email": "bob@example.com", "status": "active"},
    "user_003": {"name": "Charlie", "email": "charlie@example.com", "status": "inactive"},
}


def get_user(user_id: str) -> Optional[dict]:
    """Get user by ID."""
    if user_id in _users_db:
        return _users_db[user_id].copy()
    return None


def create_user(user_id: str, name: str, email: str) -> dict:
    """Create a new user."""
    if user_id in _users_db:
        raise ValueError(f"User {user_id} already exists")

    user_data = {
        "name": name,
        "email": email,
        "status": "active",
        "created_at": datetime.now().isoformat()
    }
    _users_db[user_id] = user_data
    return user_data


def update_user(user_id: str, **kwargs) -> Optional[dict]:
    """Update user information."""
    if user_id not in _users_db:
        return None

    for key, value in kwargs.items():
        if key in _users_db[user_id]:
            _users_db[user_id][key] = value

    return _users_db[user_id].copy()


def delete_user(user_id: str) -> bool:
    """Delete a user."""
    if user_id in _users_db:
        del _users_db[user_id]
        return True
    return False


def list_active_users() -> list:
    """List all active users."""
    return [
        {"id": uid, **data}
        for uid, data in _users_db.items()
        if data.get("status") == "active"
    ]


def main():
    """Demo the user service."""
    print("User Service Demo")
    print("=" * 40)

    # List users
    print("\nActive users:")
    for user in list_active_users():
        print(f"  - {user['id']}: {user['name']} ({user['email']})")

    # Get a user
    print("\nGet user_001:")
    user = get_user("user_001")
    print(f"  {json.dumps(user, indent=2)}")

    # Create a new user
    print("\nCreate new user:")
    try:
        new_user = create_user("user_004", "David", "david@example.com")
        print(f"  Created: {json.dumps(new_user, indent=2)}")
    except ValueError as e:
        print(f"  Error: {e}")

    # Update a user
    print("\nUpdate user_002:")
    updated = update_user("user_002", name="Bobby")
    print(f"  Updated: {json.dumps(updated, indent=2)}")


if __name__ == "__main__":
    main()
