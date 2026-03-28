# 🛜 Network Scanner with Active Device & IP Spoofing Simulation

This project is a simple but practical network security simulation built using Python and Scapy. It includes two main components:

* **Active Device** → Simulates a machine running multiple services and optionally sends spoofed packets
* **Network Scanner** → Scans a network range for open ports and listens for incoming packets

It’s useful for understanding how port scanning works, how devices respond on a network, and how spoofed packets can be detected.

---

## 🚀 Features

* Scan a full IP range (CIDR format)
* Detect open ports using TCP SYN scan
* Multi-threaded scanning for faster results
* Simulated services (HTTP, FTP, Telnet, DNS)
* Live packet sniffing
* IP spoofing simulation
* Real-time logging of network activity

---

## ⚙️ How It Works

### 1. Active Device (`activedevice.py`)

* Starts multiple fake services on ports:

  * HTTP → 8080
  * FTP → 2121
  * Telnet → 2323
  * DNS → 5353
* Listens for incoming connections
* Optionally sends spoofed UDP packets using random IPs

---

### 2. Network Scanner (`b.py`)

* Takes:

  * IP range (e.g., `192.168.1.0/24`)
  * Ports (e.g., `8080,2121,2323,5353`)
* Sends TCP SYN packets to detect open ports
* Displays results in real time
* After scanning, starts sniffing network traffic
* Captures spoofed packets sent by the active device

---

## 📦 Installation

Install required libraries:

```bash
pip install scapy
pip install ipaddress
```

> ⚠️ `threading` is built into Python, no need to install it

---

## 🖥️ Setup Requirements

* Install **WinPcap / Npcap** (required for Scapy on Windows)
* Run scripts as **Administrator**
* Temporarily disable firewall/antivirus (if blocking packets)

---

## ▶️ Usage

### Step 1: Run Active Device

```bash
python activedevice.py
```

* Starts all services
* Optional: enable IP spoofing when prompted

---

### Step 2: Run Network Scanner (on same or different machine)

```bash
python b.py
```

Enter:

```
IP Range: 192.168.1.0/24
Ports: 8080,2121,2323,5353
```

---

## 📡 Example Output

### Scanner:

```
[*] Scanning IP: 192.168.1.5
[+] Open port 8080 on 192.168.1.5
[-] No response on 192.168.1.5:2121
```

### Packet Sniffing:

```
[*] Received packet from 192.168.1.123 on port 8080
```

### Active Device:

```
[+] HTTP service running on port 8080
[HTTP] Connection from ('192.168.1.10', 54321)
[+] Sent spoofed packet to 192.168.1.5:8080 from 192.168.1.145
```

---

## ⚠️ Important Notes

* This project is for **educational purposes only**
* IP spoofing is simulated and should not be used on real networks without permission
* Works best in a **local network (LAN) environment**
* Some networks may block spoofed or raw packets

---

## 🧠 Concepts Covered

* TCP SYN Scanning
* Multi-threading in Python
* Packet crafting with Scapy
* Network sniffing
* Basic intrusion simulation
* Client-server interaction

---

## 📁 Project Structure

```
├── activedevice.py   # Simulates services + spoofing
├── b.py              # Network scanner + packet sniffer
└── README.md
```

---

## 👨‍💻 Author

Abdul Karim Hasan



