import socket

server = socket.socket()
server.bind(("127.0.0.1", 8080))

server.listen(5)

while True:
    conn, addr = server.accept()
    data = conn.recv(1024)
    print(data)  # 基于网络传输的数据，所以是二进制的数据 bytes
    conn.send(b"hello, old baby ~")
    conn.close()
