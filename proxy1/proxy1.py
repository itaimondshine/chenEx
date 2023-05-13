import socket
import hashlib

# Set up listening socket
proxy1_addr = ('10.9.0.3', 6000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(proxy1_addr)
s.listen() 

# Wait for connection from sender
print("Proxy-1 is listening...")
conn, addr = s.accept()
print(f"Connection established with {addr}.")

# Receive file data
filedata = b''
while True:
    data = conn.recv(1024)
    print(data)
    print("recived data in proxy1")
    if not data:
        break
    filedata += data


data = filedata

# Calculate MD5 hash
filehash = hashlib.md5(filedata)
md5 = filehash.hexdigest()

# Send MD5 hash to sender
conn.sendall(md5.encode())


# Implement RUDP and send to proxy 2
import socket
import sys
import time

# Constants
WINDOW_SIZE = 3
TIMEOUT = 1

# Set up UDP connection
server_addr = ("10.9.0.5", 8887)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Start sequence number
seq_num = 0

while seq_num < len(data):
    # Send packets up to window size
    for i in range(WINDOW_SIZE):
        if seq_num + i < len(data):
            packet = bytes([(seq_num + i) % 256]) + data[seq_num + i:seq_num + i + 1]
            client_socket.sendto(packet, server_addr)
            print(f"Sent packet with sequence number: {seq_num + i}")

    # Set timeout for receiving acknowledgments
    client_socket.settimeout(TIMEOUT)

    # Wait for acknowledgment
    try:
        ack, _ = client_socket.recvfrom(1)
        ack_num = int.from_bytes(ack, byteorder="big")
        print(f"Received acknowledgment for sequence number: {ack_num}")
        seq_num = ack_num + 1
    except socket.timeout:
        print("Timeout occurred, retransmitting packets...")
        continue

print("All packets sent and acknowledged.")

# Send "I got all" message to server
client_socket.sendto(b"I got all", server_addr)

client_socket.close()
