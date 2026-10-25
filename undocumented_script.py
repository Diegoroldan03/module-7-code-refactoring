def scale_numbers(numbers):
    """Doubles even numbers and triple odd numbers.

    Args:
        numbers (list[int]): Integers to process.

    Returns:
        list[int]: Scaled numbers in their original order.
"""
    return [
        number * 2 if number % 2 == 0 else number * 3 # Select the factor by parity.
        for number in numbers
    ]


def format_words(words):
    """Format words according to their length.
    
    Args:
        words (list[str]): Words to format.

    Returns:
        str: Space-separated words, uppercase when longer than five characters and lowercase otherwise.
    """
    return " ".join(
        word.upper() if len(word) > 5 else word.lower()
        for word in words
    )


def main():
    """Process sample nmbers and words and print the results.
    
    Returns:
        None: Results are printed to the terminal.
        """
    numbers = [1, 2, 3, 4, 5, 6, 7]
    words = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    scaled_numbers = scale_numbers(numbers)
    formatted_words = format_words(words)

    print("Processed Numbers:", scaled_numbers)
    print("Processed Strings:", formatted_words)


if __name__ == "__main__":
    main()
