import socket


mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('en.wikipedia.org', 80))
cmd = 'GET http://en.wikipedia.org  HTTP/1.0\n\n'.encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print (data.decode())
mysocket.close()
