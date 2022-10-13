import socket
import datetime as dt
import sys
import json


with open('auth.json', 'w+', encoding='utf-8') as f_auth:
	try:
		auth = json.load(f_auth)
	except json.decoder.JSONDecodeError:
		auth = {}
logs = open('logs.txt', 'a')
sock = socket.socket()
correct_port = 0
port = 1020
while correct_port == 0:
    try:
        sock.bind(('', port))
        print(f'Listening to port {port}')
        logs.write(f'{dt.datetime.now()} - Listening to port {port}' + '\n')
        correct_port = 1
    except OSError:
        print(f'Port {port} is already in use')
        logs.write(f'{dt.datetime.now()} - Port {port} is already in use' + '\n')
        port += 1
    
sock.listen(1)
sock.settimeout(30)

print('Waiting for connection. 30 sec to join...')
logs.write(f'{dt.datetime.now()} - Waiting for connection...' + '\n')
try:
    conn, addr = sock.accept()
except socket.timeout:
    logs.write(f'{dt.datetime.now()} - Сonnection timeout expired.' + '\n')
    logs.close()
    print(f'Сonnection timeout expired.')
    sys.exit()
print(f'Connection is set. Addres is {addr}')
logs.write(f'{dt.datetime.now()} - Connecton is set. Addres is: {addr}.' + '\n')

if not(addr[0] in auth):
	intro = 'Glad to see you! Please, enter your Name'
	conn.send(intro.encode())
	name = conn.recv(1024)
	auth[addr[0]] = name.decode()
	logs.write(f'{dt.datetime.now()} - User {name.decode()} successfully registred.' + '\n')
hello = 'Good afternoon, ' + auth[addr[0]]
conn.send(hello.encode())
logs.write(f'{dt.datetime.now()} - User {auth[addr[0]]} logged in.' + '\n')

while True:
    data = conn.recv(1024)
        #if not data:
        #break
    if data:
        msg = data.decode()
        conn.send(data)
        print(msg)
    else:
        print('Connection lost. Waiting for connection. 30 sec to join...')
        sock.listen(1)
        sock.settimeout(30)
        logs.write(f'{dt.datetime.now()} - Connection lost. Waiting for connection. 30 sec to join...' + '\n')
        try:
            conn, addr = sock.accept()
        except socket.timeout:
            logs.write(f'{dt.datetime.now()} - Сonnection timeout expired.' + '\n')
            logs.close()
            json.dump(auth, f_auth, indent='\t')
            print(f'Сonnection timeout expired.')
            sys.exit()
        print(f'Connecton is set. Addres is: {addr}')
        logs.write(f'{dt.datetime.now()} - Connection is set. Addres is: {addr}' + '\n')

conn.close()
json.dump(auth, f_auth, indent='\t')
f_auth.close()
logs.close()
