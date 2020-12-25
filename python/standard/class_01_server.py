# Python program to implement server side of chat room.  
import socket  
import select  
import sys  
import threading
import time
  
"""The first argument AF_INET is the address domain of the  
socket. This is used when we have an Internet Domain with  
any two hosts The second argument is the type of socket.  
SOCK_STREAM means that data or characters are read in  
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  

# python .\python\standard\class_01_server.py 127.0.0.1 8888
# checks whether sufficient arguments have been provided  
if len(sys.argv) != 3:  
    print("Correct usage: script, IP address, port number") 
    print("python .\python\standard\class_01_server.py 127.0.0.1 8888")
    exit()  
  
# takes the first argument from command prompt as IP address  
IP_address = str(sys.argv[1])  
  
# takes second argument from command prompt as port number  
Port = int(sys.argv[2])  
  
"""  
binds the server to an entered IP address and at the  
specified port number.  
The client must be aware of these parameters  
"""
server.bind((IP_address, Port))  
  
"""  
listens for 5 active connections. This number can be  
increased as per convenience.  
"""
server.listen(5)  
  
list_of_clients = []  
list_of_threads = []
  
def clientthread(conn, addr):  
  
    # sends a message to the client whose user object is conn  
    conn.send("Welcome to this chatroom!".encode('utf-8'))  
  
    while True:  
            try:  
                message = conn.recv(2048)  
                if message:  
  
                    """prints the message and address of the  
                    user who just sent the message on the server  
                    terminal"""
                    
  
                    # Calls broadcast function to send message to all  
                    message_to_send = "<" + addr[0] + ":" + str(addr[1]) + "> " + message.decode()  
                    broadcast(message_to_send, conn)  
                    print(message_to_send)  
                else:
                    continue
                    
            except Exception as e:
                print(e)
                remove(conn)
                print('clientthread down')
                break

  
"""Using the below function, we broadcast the message to all  
clients who's object is not the same as the one sending  
the message """
def broadcast(message, connection):  
    for clients in list_of_clients:  
        if clients!=connection:  
            try:  
                clients.send(message.decode())  
            except:  
                clients.close()  
  
                # if the link is broken, we remove the client  
                remove(clients)  
  
"""The following function simply removes the object  
from the list that was created at the beginning of  
the program"""
def remove(connection):  
    for index, target in enumerate(list_of_clients):
        if target == connection:
            list_of_clients.pop(index)
            list_of_threads.pop(index)
    # if connection in list_of_clients:  
    #     list_of_clients.remove(connection)  


try:
    print('started server, port is {0}'.format(Port))
    while True:  
        time.sleep(1)
  
        """Accepts a connection request and stores two parameters,  
        conn which is a socket object for that user, and addr  
        which contains the IP address of the client that just  
        connected"""
        conn, addr = server.accept()
    
        """Maintains a list of clients for ease of broadcasting  
        a message to all available people in the chatroom"""
        list_of_clients.append(conn)  
    
        # prints the address of the user that just connected  
        print(addr[0] + " connected") 
    
        # creates and individual thread for every user  
        # that connects  
        list_of_threads.append(threading.Thread(target=clientthread, args=(conn,addr,)))
        list_of_threads[len(list_of_threads) - 1].start()
        print('runing threads : {0}'.format(len(list_of_threads)))
        
except Exception as e:
    print(e)
    try:
        conn.close()
    except:
        print('conn error')

    try:
        server.close()
    except:
        print('server error')

    pass