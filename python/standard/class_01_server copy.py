# -*- coding: utf8 -*-

# socket 과 select 모듈 임포트
from socket import *
from select import *
import sys
from time import ctime,sleep


# 호스트, 포트와 버퍼 사이즈를 지정
HOST = ''
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST, PORT)

# 소켓 객체를 만들고..
serverSocket = socket(AF_INET, SOCK_STREAM)

# 서버 정보를 바인딩
serverSocket.bind(ADDR)

# 요청을 기다림(listen)
serverSocket.listen(10)
connection_list = [serverSocket]
print('==============================================')
print('채팅 서버를 시작합니다. %s 포트로 접속을 기다립니다.' % str(PORT))
print('==============================================')

# 무한 루프를 시작
while connection_list:
    try:
        print('[INFO] 요청을 기다립니다...[now : {0}]'.format(len(connection_list)- 1))

        # select 로 요청을 받고, 10초마다 블럭킹을 해제하도록 함
        read_socket, write_socket, error_socket = select(connection_list, [], [], 10)

        for sock in read_socket:
            # 새로운 접속
            if sock == serverSocket:
                clientSocket, addr_info = serverSocket.accept()
                connection_list.append(clientSocket)
                print('[INFO][%s] 클라이언트(%s)가 새롭게 연결 되었습니다.' % (ctime(), addr_info[0]))

                # 클라이언트로 응답을 돌려줌
                for socket_in_list in connection_list:
                    if socket_in_list != serverSocket and socket_in_list != sock:
                        try:
                            print('새로운 알림')
                            socket_in_list.send('[{0}] 새로운 방문자가 대화방에 들어왔습니다.'.format(ctime()).encode('utf-8'))
                        except Exception as e:
                            print(e)
                            socket_in_list.close()
                            connection_list.remove(socket_in_list)
            # 접속한 사용자(클라이언트)로부터 새로운 데이터 받음
            else:
                try:
                    socket_in_list.send('[{0}] test'.format(ctime()).encode('utf-8'))
                    chunks = []
                    bytes_recd = 0
                    while bytes_recd < BUFSIZE:
                        chunk = sock.recv(min(BUFSIZE - bytes_recd, 2048))
                        print(chunk)
                        if chunk == b'':
                            sleep(1)
                            print('no have data from')
                            continue
                            # raise RuntimeError("socket connection broken")
                        chunks.append(chunk)
                        bytes_recd = bytes_recd + len(chunk)
                    data = b''.join(chunks)
                    print('data', data)
                    if data:
                        print('[INFO][{0}] 클라이언트로부터 데이터를 전달 받았습니다.'.format(ctime()))
                        for socket_in_list in connection_list:
                            if socket_in_list != serverSocket and socket_in_list != sock:
                                try:
                                    socket_in_list.send("[{0}] {1}".format(ctime(), data).encode('utf-8'))
                                    print('[INFO][{0}] 클라이언트로 데이터를 전달합니다.'.format(ctime()))
                                except Exception as e:
                                    socket_in_list.close()
                                    connection_list.remove(socket_in_list)
                                    continue
                    else:
                        pass
                        # connection_list.remove(sock)
                        # sock.close()
                except Exception as e:
                    print(e)
                    connection_list.remove(sock)
                    sock.close()
                    print('[INFO][{0}] 사용자와의 연결이 끊어졌습니다.'.format(ctime()))
                    pass
    except KeyboardInterrupt:
        # 부드럽게 종료하기
        serverSocket.close()
        sys.exit()