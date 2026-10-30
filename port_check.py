import socket

open_count = 0
close_count = 0

for line in open("targets.txt"):
    line = line.strip()
    if not line:
        continue

    parts = line.split()
    host = parts[0]
    port = int(parts[1])

    s = socket.socket()
    s.settimeout(1)
    code = s.connect_ex((host, port))
    s.close()

    if code == 0:
        print(f"{host}:{port} 开放")
        open_count += 1
    else:
        print(f"{host}:{port} 关闭")
        close_count += 1

print(f"开放 {open_count} 个，关闭 {close_count} 个")