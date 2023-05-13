import socket
import hashlib


filename = 'file.txt'
host = '10.9.0.3'
port = 6000

with open(filename, 'rb') as f:
    data = f.read()


md5_hash = hashlib.md5(data).hexdigest()
data += b'__EOF__'
print(f"MD5 hash of {filename}: {md5_hash}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(data)
    s.sendall(md5_hash.encode())
