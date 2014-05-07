import socket

sock = socket.socket()
print "Port:"
port = int(raw_input())
sock.bind(('', port))
sock.listen(5)

while True:
    conn, addr = sock.accept()    
    data = conn.recv(1024)
    if not data:
        conn.close()
    conn.send("Recieved:"+data)
