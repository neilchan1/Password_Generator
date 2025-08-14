import random
import string

def generate_password(character_length, numbers_length, symbols_length):
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    if numbers_length + symbols_length > character_length:
        raise ValueError(f"Numbers ({numbers_length}) + Symbols ({symbols_length}) required cannot exceed character length ({character_length})")

    password_chars = []
    letters_length = character_length - (numbers_length + symbols_length)

    password_chars.extend(random.choices(numbers, k=numbers_length))
    password_chars.extend(random.choices(symbols, k=symbols_length))
    password_chars.extend(random.choices(letters, k=letters_length))
    
    random.shuffle(password_chars)

    return ''.join(password_chars)
