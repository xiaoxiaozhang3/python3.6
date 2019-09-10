
import socket

# IP AF_INET TCP SOCK_STREAM
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("120.0.0.1",9090))

s.listen(5)

while True:
    res = s.accept()
    print(res)