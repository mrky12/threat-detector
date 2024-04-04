import hashlib

# Database of known malicious file hashes
MALICIOUS_HASHES = {
    'e4d909c290d0fb1ca068ffaddf22cbd0': 'malware.exe',
    '5eb63bbbe01eeed093cb22bb8f5acdc3': 'trojan.docx'
}

# Function to calculate SHA256 hash of a file
def calculate_hash(file_path):
    try:
        with open(file_path, 'rb') as f:
            file_content = f.read()
            hash_object = hashlib.sha256()
            hash_object.update(file_content)
            file_hash = hash_object.hexdigest()
            return file_hash
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# Function to check if file hash matches known malicious hashes
def detect_threat(file_path):
    file_hash = calculate_hash(file_path)
    if file_hash:
        if file_hash in MALICIOUS_HASHES:
            print(f"Threat detected: {MALICIOUS_HASHES[file_hash]}")
        else:
            print("No threat detected.")
    else:
        print("Unable to detect threat.")

# Example usage
if __name__ == "__main__":
    file_path = 'file_to_scan.exe'  # Replace with the path to the file you want to scan
    detect_threat(file_path)
