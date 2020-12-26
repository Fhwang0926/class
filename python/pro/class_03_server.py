#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926

import socket,time

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 7777        # Port to listen on (non-privileged ports are > 1023)

print('server start port by', PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        time.sleep(0.5)
        # while True:
        #     data = conn.recv(1024)
        #     if not data:
        #         break
        #     conn.sendall(data)