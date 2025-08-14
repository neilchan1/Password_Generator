import argparse
from password_generator import generate_password

def get_user_input():
    length = int(input("How many characters for your new password?\n"))
    numbers_required = int(input("How many numbers would you like?\n"))
    symbols_required = int(input("How many symbols would you like?\n"))

    return length, numbers_required, symbols_required

def parse_args():
    """
    Allows for CLI by passing in args.

    Args:
    --length: int (Required)
    --numbers: int - (Optional)
    --symbols: int - (Optional)
    """
    parser = argparse.ArgumentParser(description="Generate a random secure password.",
                                     usage="%(prog)s [--length int] [--numbers int] [--symbols int]")

    parser.add_argument("--length", type=int, help="Total length of password")
    parser.add_argument("--numbers", type=int, default=0, nargs='?', help="How many numbers required")
    parser.add_argument("--symbols", type=int, default=0, nargs='?', help="How many symbols required")

    return parser.parse_args()

def main():
    args = parse_args()
    character_length = args.length
    number_length = args.numbers
    symbols_length = args.symbols

    if character_length and (character_length < number_length + symbols_length):
        print("Error: total length is smaller than the sum of numbers and symbols.")
        exit(1)
    elif character_length:
        generate_password(character_length, number_length, symbols_length)
    else:
        character_length, number_length, symbols_length = get_user_input()

    try:
        password = generate_password(character_length, number_length, symbols_length)

        print(f"\nYour new password is:\n{password}")
    except ValueError as e:
        print(f"\nERROR: {e}")

if __name__ == "__main__":
    main()