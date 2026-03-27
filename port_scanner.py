import socket

def scan_ports(target, ports):
    print(f"\n[+] Scanning Target: {target}")
    print("[+] Scanning started...\n")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
            sock.close()

        except KeyboardInterrupt:
            print("\n[!] Scan interrupted.")
            break
        except socket.gaierror:
            print("[!] Hostname could not be resolved.")
            break
        except socket.error:
            print("[!] Couldn't connect to server.")
            break

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443]

    scan_ports(target, ports)