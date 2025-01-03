import hashlib
import csv

# Function to hack passwords using brute force
def hash_password_hack(input_file, output_file_name):
    # Initialize lists for names and hashed passwords
    names = []
    hashed_passwords = []
    
    # Read the input file and populate names and passwords
    with open(input_file, 'r') as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            # Assume the file has two columns: name and hashed password
            name, hashed_password = line
            names.append(name)
            hashed_passwords.append(hashed_password)
    
    # Create a rainbow table to map hashes back to passwords
    rainbow_table = {}
    for number in range(10000):  # Generate all 4-digit combinations (0000 to 9999)
        password = str(number).zfill(4)  # Ensure passwords are 4 digits (e.g., '0001')
        hashed_value = hashlib.sha256(password.encode()).hexdigest()
        rainbow_table[hashed_value] = password  # Map the hash to the password
    
    # Find matches and write to the output file
    with open(output_file_name, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for name, hashed_password in zip(names, hashed_passwords):
            if hashed_password in rainbow_table:
                # Write the name and the original password to the output file
                csv_writer.writerow([name, rainbow_table[hashed_password]])

    print(f"Password hack complete. Results saved to {output_file_name}.")

# Main block to run the function
if __name__ == '__main__':
    hash_password_hack('input.csv', 'output.csv')
