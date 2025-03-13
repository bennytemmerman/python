import zipfile
import itertools
import string

def brute_force_zip(zip_file, charset, min_length, max_length):
    # Iterate through the range of password lengths
    for length in range(min_length, max_length + 1):
        print(f"\nTrying passwords of length {length}...")
        # Generate all possible combinations of the given charset and length
        for password in itertools.product(charset, repeat=length):
            password = ''.join(password)  # Convert tuple to string
            try:
                with zipfile.ZipFile(zip_file) as zf:
                    # Try to read the first file in the archive with the password
                    file_to_test = zf.namelist()[0]  # Get the first file in the ZIP
                    zf.read(file_to_test, pwd=password.encode('utf-8'))
                print(f"\nSuccess! Password found: {password}")
                return password
            except (RuntimeError, zipfile.BadZipFile):
                # Print progress
                print(f"Trying password: {password}", end="\r")
                continue  # If the password is incorrect, move to the next one
    print("\nPassword not found.")
    return None

def get_charset(choice):
    # Define character sets based on user input
    if choice == "1":
        return string.digits  # Numerical (0-9)
    elif choice == "2":
        return string.ascii_letters  # Alphabetical (a-z, A-Z)
    elif choice == "3":
        return string.digits + string.ascii_letters  # Alphanumerical (0-9, a-z, A-Z)
    else:
        raise ValueError("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    # Ask for user input
    print("Select the password type:")
    print("1. Numerical (0-9)")
    print("2. Alphabetical (a-z, A-Z)")
    print("3. Alphanumerical (0-9, a-z, A-Z)")
    choice = input("Enter your choice (1, 2, or 3): ")

    try:
        charset = get_charset(choice)
    except ValueError as e:
        print(e)
        exit(1)

    min_length = int(input("Enter the minimum password length: "))
    max_length = int(input("Enter the maximum password length: "))
    zip_file = input("Enter the path to the ZIP file: ")

    # Run the brute-force attack
    brute_force_zip(zip_file, charset, min_length, max_length)
