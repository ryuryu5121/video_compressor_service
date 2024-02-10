import socket
import sys
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = '0.0.0.0'
server_port = 9001

try:
    sock.connect((server_address, server_port))
except socket.error as err:
    print(err)

try:
    file_path = input('Type in a file to upload: ')

    with open(file_path, 'rb') as f:
        f.seek(0, os.SEEK_END)
        file_size = f.tell()
        f.seek(0,0)

        if file_size > pow(2, 32):
            raise Exception('File must be below 4GB')
        
        sock.send(file_size.to_bytes(32, "big"))
        data = f.read(1400)
        while data:
            print("Sending...")
            sock.send(data)
            data = f.read(1400)

        
finally:
    print('closing socket')
    sock.close()