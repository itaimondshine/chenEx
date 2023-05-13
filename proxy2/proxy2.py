import socket
import os
import sys
import time

# Constants
WINDOW_SIZE = 5

# Set up UDP connection
server_addr = ("10.9.0.5", 8887)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_addr)

# Buffer to store received packets
buffer_size = 1024
buffer = bytearray(buffer_size)

# Sequence number of expected packet
expected_seq_num = 0

# Set timeout for receiving packets
server_socket.settimeout(30)

while True:
    try:
        # Receive packet
        packet, client_addr = server_socket.recvfrom(buffer_size)

        # Extract sequence number and data from packet
        seq_num = int.from_bytes(packet[0:1], byteorder="big")

        # Check if received packet is expected packet
        if seq_num == expected_seq_num:
            # Send acknowledgment
            server_socket.sendto(packet[0:1], client_addr)
            print(f"Received packet with sequence number: {seq_num}, Sent acknowledgment")

            # Write received data to file
            with open("received_file.txt", "ab") as file:
                file.write(packet[1:])

            expected_seq_num += 1
        else:
            # Send acknowledgment for last received packet
            ack = expected_seq_num - 1
            server_socket.sendto(ack.to_bytes(1, byteorder="big"), client_addr)
            print(f"Received out-of-order packet with sequence number: {seq_num}, Sent acknowledgment for last received packet: {ack}")

    except socket.timeout:
        print("Timeout occurred, closing connection...")
        break

# Close the socket connection after receiving all packets or timeout
server_socket.close()

user_addr = ('10.9.0.6', 9000)


user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_socket.connect(user_addr)

with open("received_file.txt", "rb") as file:
    file_data = file.read(buffer_size)
    while file_data:
        user_socket.send(file_data)
        file_data = file.read(buffer_size)

os.remove('received_file.txt')
user_socket.close()
print("File sent to user.")
