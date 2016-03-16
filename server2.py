import socket, _thread

def connect():
    conn, addr = s.accept()
    answers_th(conn)
    
def client(i):
    while True:
        data=i.recv(1024)
        if not data or data.decode()=='close':
            i.close()
            print('закрыто')
            break
        else:
            i.send(data)
            print(data.decode())

def answers_th(k):
    _thread.start_new_thread(client,(k,))

def connect_th():
    while True:
        connect()

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(10)

connect_th()

input()
