import socket

# Dati di input
target = "192.168.20.10"
start_port = 1
end_port = 1024

# Porte che idealmente dovrebbero essere chiuse
porte_sicure_da_chiudere = list(range(1, 1024))

# Porte note e relativa valutazione di sicurezza
porte_note = {
    21: ("FTP", "Non Sicura"),    
    22: ("SSH", "Sicura"),   
    23: ("TELNET", "Non Sicura"),     
    25: ("SMTP", "Potenzialmente Rischiosa"), 
    53: ("DNS", "Sicura se ben configurata"), 
    80: ("HTTP", "Non Sicura"),  
    110: ("POP3", "Non Sicura"), 
    111: ("RPCBind", "Potenzialmente Rischiosa"), 
    139: ("NetBios", "Potenzialmente Rischiosa"), 
    143: ("IMAP", "Non Sicura"),  
    445: ("SMB", "Potenzialmente Rischiosa"), 
    873: ("rsync", "Non Sicura"),
    993: ("IMAPS", "Sicura"),   
    995: ("POP3S", "Sicura"),   
    3389: ("RDP", "Non Sicura"),
    8080: ("HTTP Alternativo", "Non Sicura"),
}


def scan_ports(target, start_port, end_port):
    print(f"\n🔍 Scansione delle porte su {target} da {start_port} a {end_port}...\n")

    avvisi_sicurezza = []
    porte_sicure = []
    porte_conosciute_non_sicure = []
    porte_sconosciute = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex((target, port))

        if result == 0:
            # Porta aperta
            if port in porte_note:
                servizio, sicurezza = porte_note[port]
                if "Sicura" in sicurezza:
                    print(f"✅ Porta {port} è APERTA - Servizio: {servizio} - Sicurezza: {sicurezza}")
                    porte_sicure.append((port, servizio, sicurezza))
                else:
                    print(f"⚠️ Porta {port} è APERTA - Servizio: {servizio} - Sicurezza: {sicurezza}")
                    porte_conosciute_non_sicure.append((port, servizio, sicurezza))
            else:
                # Servizio sconosciuto
                print(f"🔍 Porta {port} è APERTA - Servizio sconosciuto")
                porte_sconosciute.append(port)

        else:
            print(f"❌ Porta {port} è CHIUSA")

        sock.close()

    # Riepilogo finale
    print("\n📋 RIEPILOGO SICUREZZA:")

    if avvisi_sicurezza:
        print("\n⚠️  Porte aperte potenzialmente rischiose:")
        for idx, avviso in enumerate(avvisi_sicurezza, 1):
            print(f"{idx}. {avviso}")
    else:
        print("\n✅ Nessuna porta potenzialmente pericolosa rilevata.")

    if porte_sicure:
        print("\n🔐 Porte aperte considerate sicure:")
        for idx, (port, servizio, sicurezza) in enumerate(porte_sicure, 1):
            print(f"{idx}. Porta {port} - Servizio: {servizio} - Sicurezza: {sicurezza}")
    else:
        print("\n🚫 Nessuna porta sicura rilevata aperta.")

    if porte_conosciute_non_sicure:
        print("\n⚠️ Porte conosciute aperte e non sicure:")
        for idx, (port, servizio, sicurezza) in enumerate(porte_conosciute_non_sicure, 1):
            print(f"{idx}. Porta {port} - Servizio: {servizio} - Sicurezza: {sicurezza}")
    else:
        print("\n✅ Nessuna porta conosciuta e non sicura aperta.")

    if porte_sconosciute:
        print("\n🔍 Servizi sconosciuti aperti:")
        for idx, port in enumerate(porte_sconosciute, 1):
            print(f"{idx}. Porta {port} - Servizio sconosciuto")

# Avvia scansione
scan_ports(target, start_port, end_port)
