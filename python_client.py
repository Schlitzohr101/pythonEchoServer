import socket
import re

def is_valid_ip_address(ip_address):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    return bool(pattern.match(ip_address))


HOST = ''  
PORT = 5000  # Arbitrary non-privileged port

while True: 
    print("Please enter in a server",end="")
    cur_host = input(": ")
    if is_valid_ip_address(cur_host):
        HOST = cur_host
        break
    else:
        print("That wasn't a valid IP address format try again")


while True: 
    print("Please enter in a port",end="")
    cur_port = input(": ")
    try:
        cur_port = int(cur_port)
        PORT = cur_port
        break
    except Exception as e:
        print("that is not a valid port... Try again")

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Send and receive data until the user terminates the program
while True:
    print("Enter mesage to send (\"quit\" to exit)",end="")
    message = input(': ')
    if message.lower().find('quit') != -1:
        break
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print('Received:', data.decode())

# Clean up the connection
client_socket.close()