import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
connected = 0
while connected == 0:
    addr = ['localhost', 9090]
    port_is_correct = 0
    try:
        host = input('Enter the host name, default value: localhost ')
        while port_is_correct == 0:
            try:
                port = input('Enter the port number, default value: 9090 ')
                if not port:
                    port_is_correct = 1
                    break
                port = int(port)
                port_is_correct = 1
            except ValueError:
                print('Invalid port number. Enter an INTEGER.')
        if host:
            addr[0] = host
        if port:
            addr[1] = port
        addr = tuple(addr)
        sock.connect(addr)
        connected = 1
    except socket.gaierror:
        print('Invalid data entered, try again.')
    except ConnectionRefusedError:
        print('Invalid data entered, try again.')
print(f'Successful connection. Host: {addr[0]}, port: {addr[1]}')

print(sock.recv(1024).decode())
name = input('Enter your name: ')
sock.send(name.encode())
while True:
    msg = input()
    if msg == 'exit':
        break
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(f'Данные полученные от сервера: {data.decode()}')
    
    
sock.close()
print('Connection lost.')
