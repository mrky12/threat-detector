import os

def scan_directory(directory):
    threats = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension in ['.exe', '.dll', '.vbs', '.bat', '.ps1']:
                threats.append(file_path)
    return threats

def main():
    print("Welcome to Basic Threat Detection Software!")
    print("------------------------------------------")
    directory_to_scan = input("Enter the directory to scan: ")
    if not os.path.isdir(directory_to_scan):
        print("Invalid directory path.")
        return
    
    threats = scan_directory(directory_to_scan)
    
    if threats:
        print("\nThreats found:")
        for threat in threats:
            print(threat)
    else:
        print("\nNo threats found.")

if __name__ == "__main__":
    main()
