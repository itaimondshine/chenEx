import socket

# Set up listening socket
diode_addr = ('10.9.0.4', 7000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(diode_addr)
s.listen()


# Wait for connection from proxy-a
print("network-diode is listening...")
conn, addr = s.accept()
print(f"Connection established with {addr}.")

# Receive file data
filedata = b''
while True:
    data = conn.recv(1024)
    print(data)
    print("recived data in network")
    if not data:
        break
    filedata += data

# Connect to proxy-2
proxy2_addr = ('10.9.0.5', 8000)


#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(proxy2_addr)
    s.sendall(filedata)

# Close the connection
s.close()

