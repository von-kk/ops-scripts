import socket


s = socket.socket()
s.settimeout(1)
code = s.connect_ex(("127.0.0.1", 22))
s.close()

print(("返回码：",code))