import socket

SVR_ADDR="192.168.10.10"
SVR_PORT=4444
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SVR_ADDR, SVR_PORT))
s.listen(1)
print("Server aperto")
conn, addr = s.accept()
print("Connesso da: ", addr)
while True:
    data=conn.recv(1024)
    decoded=data.decode("utf-8")
    print("Messaggio ricevuto: ", decoded.strip())
    if decoded=="end\n": break
    conn.sendall(b"Messaggio ricevuto\n")
    print(data.decode("utf-8"), end="")
conn.close()
