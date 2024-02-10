import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = '0.0.0.0'
server_port = 9001
stream_rate = 1400

sock.bind((server_address, server_port))
sock.listen(1)
while True:
    connection, address = sock.accept()
    print("start connect {address}")
    file_path = input('input file_path: ')
    try:
        header = connection.recv(32)
        file_size = int.from_bytes(header, "big")

        if file_size == 0:
            raise Exception('No data')
        
        with open(file_path, 'wb+') as f:
            while file_size >0:
                data = connection.recv(file_size if file_size > stream_rate else stream_rate)
                f.write(data)
                print('recieved {} bytes'.format(len(data)))
                file_size -= len(data)
                print(file_size)
        print('Finishe download')
    except Exception as err:
        print(err)