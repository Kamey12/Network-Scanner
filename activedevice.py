import socket
import threading
import time
import random
import scapy.all as scapy

services = {
    "HTTP": 8080,   
    "FTP": 2121,   
    "Telnet": 2323, 
    "DNS": 5353     
}

def start_service(service_name, port):
   
    try:
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("0.0.0.0", port))
        server_socket.listen(5)
        print(f"[+] {service_name} service running on port {port}")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"[{service_name}] Connection from {addr}")
            client_socket.close()

    except OSError as e:
        print(f"[!] {service_name} error: {e}")
    except Exception as e:
        print(f"[!] Unexpected error in {service_name}: {e}")

def spoof_ip(target_ip, target_port, fake_ip):
  
    try:
        print(f"[*] Starting IP spoofing simulation. Fake IP: {fake_ip}")
        while True:
            packet = scapy.IP(src=fake_ip, dst=target_ip) / scapy.UDP(dport=target_port,sport=target_port) 
            scapy.send(packet) 
            print(f"[+] Sent spoofed packet to {target_ip}:{target_port} from {fake_ip}")
            time.sleep(5) 
    except Exception as e:
        print(f"[!] IP Spoofing error: {e}")

if __name__ == "__main__":
    threads = []

    try:
        
        for service_name, port in services.items():
            thread = threading.Thread(target=start_service, args=(service_name, port))
            threads.append(thread)
            thread.start()

        print("[*] All services started. Listening for connections...")

    
        spoof_choice = input("Do you want to simulate IP spoofing? (yes/no): ").strip().lower()
        if spoof_choice == "yes":
            target_ip = input("Enter the target IP address: ").strip()
            target_port = int(input("Enter the target port: ").strip())
            fake_ip = f"192.168.1.{random.randint(100, 254)}"
            spoof_thread = threading.Thread(target=spoof_ip, args=(target_ip, target_port, fake_ip))
            spoof_thread.daemon = True  
            threads.append(spoof_thread)
            spoof_thread.start()

        
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n[*] Shutting down all services...")
        for thread in threads:
            thread.join()
        print("[*] All services stopped.")
