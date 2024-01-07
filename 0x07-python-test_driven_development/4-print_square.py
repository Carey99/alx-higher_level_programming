def print_square(size):
    """
    Prints a square with the character #.
    Args:
    - size: an integer representing the size length of the square
    Raises:
    - TypeError: if size is not an integer or is a float
    - ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
