# def apply_discount(price: int, discount: float = 0.0) -> int:
#     """Apply Discount Percent and Calculate Final Price"""
#     final_price = int(price * (1 - discount))
#     assert 0 < final_price <= price, """“Why this AssertionError never Raised!”)"""
#     return final_price

# print(apply_discount(100000,2))

# this is an exercise to undrestant that assert is not the way to show errors in production.


def apply_discount(price: int, discount: float = 0.0) -> int:
    """Apply Discount Percent and Calculate Final Price"""
    if price <= 0:
        raise ValueError("Price must be positive")
    if not 0 <= discount < 1:
        raise ValueError("Discount must be between 0.0 and 0.99")
    
    final_price = int(price * (1 - discount))
    
    return final_price


print(apply_discount(100000,2))