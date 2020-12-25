# -*- coding: utf8 -*-

# socket 모듈을 임포트
from socket import *
from select import select
import time
import sys
import threading

# 호스트, 포트와 버퍼 사이즈를 지정
HOST = '127.0.0.1'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST, PORT)

# 소켓 객체를 만들고
clientSocket = socket(AF_INET, SOCK_STREAM)

# 서버와의 연결을 시도
try:
    clientSocket.connect(ADDR)
except Exception as e:
    print('채팅 서버(%s:%s)에 연결 할 수 없습니다.' % ADDR)
    sys.exit()
print('채팅 서버(%s:%s)에 연결 되었습니다.' % ADDR)


def prompt():
    sys.stdout.write('<나> ')
    sys.stdout.flush()

def msg_from_server(clientSocket):
    try:
        chunks = []
        bytes_recd = 0
        data = clientSocket.recv(BUFSIZE)
        while bytes_recd < BUFSIZE:
            time.sleep(1)
            chunk = clientSocket.recv(min(BUFSIZE - bytes_recd, 2048))
            if chunk == b'':
                continue
                # raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        data = b''.join(chunks)
        if data:
            print(data)
    except Exception as e:
        print(e)
        pass
 
# # 데몬 쓰레드
t1 = threading.Thread(target=msg_from_server, args=(clientSocket,))
t1.start()
# 무한 루프를 시작
prompt()
while True:
    try:
        time.sleep(1)
        connection_list = [clientSocket]

        message = sys.stdin.readline()
        message = message.replace('\n', '')
        clientSocket.send(message.encode('utf-8'))
        prompt()
    except KeyboardInterrupt:
        clientSocket.close()
        sys.exit()
    except Exception as e:
        print(e)
        clientSocket.close()
        sys.exit()