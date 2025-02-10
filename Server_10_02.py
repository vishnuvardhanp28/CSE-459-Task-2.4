import socket
from Crypto.Cipher import ARC4

# Function to decrypt the file using RC4
def decrypt_data(encrypted_data, key):
    cipher = ARC4.new(key.encode())  # RC4 decryption
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data

# Server Code
def server():
    server_ip = '192.168.139.29'  # Update to the IP address you are using (or '127.0.0.1' for localhost)
    server_port = 50000  # Updated port to avoid potential conflicts

    # Key for RC4 encryption/decryption
    key = 'mysecretkey'

    # Create a socket and bind to the IP/Port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    print(f'Server listening on {server_ip}:{server_port}')

    # Accept connection from client
    client_socket, client_address = server_socket.accept()
    print(f'Connected to {client_address}')

    # Receive the encrypted data
    encrypted_data = client_socket.recv(1024*1024)  # Buffer size 1 MB

    # Decrypt the data
    decrypted_data = decrypt_data(encrypted_data, key)

    # Save the encrypted file
    with open('encrypted_file.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    # Save the decrypted file
    with open('decrypted_file.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print("Files saved: 'encrypted_file.txt' and 'decrypted_file.txt'")

    # Close the connection
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    server()
