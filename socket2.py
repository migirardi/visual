import socket
def capture_socket(host, port):  
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Socket creato con successo")
    except socket.error as err_msg:
        print(f"Creazione del socket fallita: {err_msg}")
        return None
    try:
      
        s.connect((host, port))
        print(f"Socket connesso a {host}:{port}")
    except socket.error as err_msg:
        print(f"Connessione del socket fallita: {err_msg}")
        s.close()
        return None
    return s
def main():
    host = '192.168.20.10'  
    port = 80            
    captured_socket = capture_socket(host, port)
    if captured_socket:      
        try:
            request = "GET / HTTP/1.1\r\nHost: 192.168.20.10\r\nConnection: close\r\n\r\n"
            captured_socket.sendall(request.encode())
            print("Richiesta inviata con successo")            
            response = b''
            while True:
                data = captured_socket.recv(4096)
                if not data:
                    break
                response += data           
            print("Risposta ricevuta:")
            print(response.decode('utf-8', errors='ignore'))  
        except socket.error as err_msg:
            print(f"Errore durante l'invio/ricezione dati: {err_msg}")
        finally:
            captured_socket.close()  
            print("Socket chiuso")
if __name__ == "__main__":
    main() 