import socket

def con():
    s = socket.socket()
    print "Server:"
    addr = raw_input()
    print "Port"
    port = int(raw_input())
    s.connect((addr, port)) 
    print "Message:"
    mes = raw_input()
    s.send(mes)
    print "Recieved from server:"
    mes = s.recv(1024)
    print mes
    s.close()

con()
