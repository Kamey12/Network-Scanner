import scapy.all as scapy
import ipaddress
from threading import Thread, Lock

print_lock = Lock()

open_ports = {}

def scan_port(ip, port):
    
    try:
        
        packet = scapy.IP(dst=ip) / scapy.TCP(dport=port, flags="S")
        response = scapy.sr1(packet, timeout=2, verbose=False)

        
        if response and response.haslayer(scapy.TCP) and response[scapy.TCP].flags == "SA":
            with print_lock:
                print(f"[+] Open port {port} on {ip}")
            if ip not in open_ports:
                open_ports[ip] = []
            open_ports[ip].append(port)
        else:
            with print_lock:
                print(f"[-] No response on {ip}:{port}")
    except Exception as e:
        with print_lock:
            print(f"[!] Error scanning {ip}:{port} - {e}")

def scan_target(ip, ports):
    
    print(f"[*] Scanning IP: {ip}")
    for port in ports:
        scan_port(ip, port)

def listen_for_packets():
    def packet_callback(packet):
        if packet.haslayer(scapy.IP):
            with print_lock:
                print(f"[*] Received packet from {packet[scapy.IP].src} on port {packet.sport}")
    
    iface = "Intel(R) Wireless-AC 9560 160MHz"
    scapy.sniff(iface=iface,filter="udp and (port 8080 or port 2121 or port 2323 or port 5353)", prn=packet_callback, store=False)



def network_scanner(ip_range, ports):

    print("[*] Starting network scan...")

    threads = []

    for ip in ipaddress.IPv4Network(ip_range, strict=False):
        thread = Thread(target=scan_target, args=(str(ip), ports))
        threads.append(thread)
        thread.start()

 
    for thread in threads:
        thread.join()

    
    if open_ports:
        print("\n[*] Open Ports Summary:")
        for ip, ports in open_ports.items():
            for port in ports:
                print(f"open port {port} on ip: {ip}")
    else:
        print("[*] No open ports found.")

   
    listen_for_packets()


if __name__ == "__main__":
    try:
    
        ip_range = input("Enter IP range (e.g., 192.168.1.0/24): ").strip()
        ports_input = input("Enter ports to scan (comma-separated): ").strip()

     
        ports = [int(port.strip()) for port in ports_input.split(",")]

    
        network_scanner(ip_range, ports)

    except ValueError:
        print("[!] Invalid port input. Please enter numbers separated by commas.")
    except Exception as e:
        print(f"[!] Error: {e}")
