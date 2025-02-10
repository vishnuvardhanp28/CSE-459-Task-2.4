import socket
from Crypto.Cipher import ARC4
import os

# Function to encrypt the file using RC4
def encrypt_file(input_file, key):
    try:
        # Check if the file exists before attempting to read it
        print(f"Checking if file exists at: {input_file}")
        if not os.path.exists(input_file):
            print(f"Error: The file '{input_file}' was not found.")
            exit(1)  # Exit the program if file is not found

        # Open the input file in binary read mode
        with open(input_file, 'rb') as f:
            file_data = f.read()

        # Create an RC4 cipher using the provided key
        cipher = ARC4.new(key.encode())
        encrypted_data = cipher.encrypt(file_data)
        return encrypted_data

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit(1)

# Client Code
def client():
    server_ip = '192.168.139.29'  # Use the same IP as the server (or '127.0.0.1' for localhost)
    server_port = 50000  # Port used by the server

    # Key for RC4 encryption
    key = 'mysecretkey'

    # Define the input file (New.txt located in the specified folder)
    input_file = r'C:\Users\vishn\Desktop\Cyber Lab\New.txt'  # New file path

    # Encrypt the file
    encrypted_data = encrypt_file(input_file, key)

    # Setup socket connection to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    # Send encrypted data to the server
    client_socket.sendall(encrypted_data)

    print("Encrypted data sent to server.")

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    client()
