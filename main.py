def round_to_decimal(value: float, decimal: float) -> float:
    """
    Rounds the given value to the nearest multiple of the specified decimal.

    Parameters:
        value (float): The number to round.
        decimal (float): The rounding decimal.

    Returns:
        float: The rounded value.
    """
    if decimal == 0:
        raise ValueError("Decimal must be non-zero.")
    
    # Calculate the nearest multiple of the specified decimal
    return round(value / decimal) * decimal

def get_decimal_part(value: float) -> float:
    """
    Extracts the decimal part of a given float.

    Parameters:
        value (float): The number to extract the decimal part from.

    Returns:
        float: The decimal part of the number.
    """
    return abs(value) - abs(int(value))

def test_functions():
    # Example usage
    result = round_to_decimal(5.821, 0.1)
    print(result)  # Output: 5.8
