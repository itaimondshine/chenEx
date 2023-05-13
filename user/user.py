import socket
import hashlib
from tqdm import tqdm

# Set up listening socket
user_addr = ('10.9.0.6', 9000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(user_addr)
s.listen()


# Wait for connection from sender
print("User is listening...")
conn, addr = s.accept()
print(f"Connection established with {addr}.")


data = conn.recv(1024)

filedata = b''
filehash = b''

print(data)
filedata, filehash  = data.split(b'__EOF__')

md5_hash = hashlib.md5(filedata).hexdigest()
print(filedata)
print(filehash)

# Compare computed hash with given hash
if filehash.decode() == md5_hash:
    print("File integrity verified. Hashes match.")
else:
    print("File integrity verification failed. Hashes do not match.")

# Close the connection
s.close()
