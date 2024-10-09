import hashlib

def hash_file(file_path):
    """Calculate the hashes of a file."""
    hashes = {
        'md5': hashlib.md5(),
        'sha1': hashlib.sha1(),
        'sha256': hashlib.sha256(),
        'sha384': hashlib.sha384(),
        'sha512': hashlib.sha512(),
    }

    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):  # Read in chunks of 8KB
                for hash_func in hashes.values():
                    hash_func.update(chunk)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

    return {hash_name: hash_func.hexdigest() for hash_name, hash_func in hashes.items()}

# Main script
def main():
    file_path = input("Enter the file path: ")
    file_hashes = hash_file(file_path)

    if file_hashes is None:
        return

    print("Calculated Hashes:")
    for hash_type, hash_value in file_hashes.items():
        print(f"{hash_type.upper()}: {hash_value}")

if __name__ == "__main__":
    main()

