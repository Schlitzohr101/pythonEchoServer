import socket
import re

def is_valid_ip_address(ip_address):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    return bool(pattern.match(ip_address))


HOST = ''  
PORT = 5000  # Arbitrary non-privileged port
server_socket = None
while True:
    while True: 
        print("Please enter in address to bind to",end="")
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


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((HOST, PORT))
        break
    except Exception as e:
        print("Failed to bind for server port or address...")
        print("error: ",e)
        print("Try again....")

# Listen for incoming connections
server_socket.listen(1)

print('Echo server listening on port', PORT)

while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()
    print('Client connected:', client_address)

    # Receive and echo back data until the client closes the connection
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print("recieved data: %s" % (data))
        client_socket.sendall(data)

    # Clean up the connection
    print('Client disconnected:', client_address)
    client_socket.close()