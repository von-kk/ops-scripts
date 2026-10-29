import subprocess
up = 0
down = 0

for line in open("ips.txt"):
    ip = line.strip()
    if not ip:
        continue

    result = subprocess.run(
        ["ping","-c","1","-W","1000",ip],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(ip,"通")
        up += 1
    else:
        print(ip,"不通")
        down += 1

print(f"通 {up} 个,不通 {down}个")