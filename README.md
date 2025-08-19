# Network log Automation 

This mini-project connects to multiple Linux devices using **Netmiko**, runs a set of commands, and saves results into a single log file.

---

## 🚀 Features
- Connects to multiple devices via SSH
- Executes basic commands (`hostname`, `whoami`, `pwd`)
- Handles errors during connection attempts

---

## ⚡ Installation & Usage

1. Clone the repo:
   git clone https://github.com/YOUR_USERNAME/network-audit-automation.git
   cd network-audit-automation
   
3. Install dependencies:
   pip install -r requirements.txt
   
5. Update the devices in network_audit.py:
    devices = [
    {"device_type": "your device type", "host": "your device ip", "username": "your device username", "password": "your device password"},
    {"device_type": "your device type", "host": "your device ip", "username": "your device username", "password": "your device password"},
}

6. Run the script:
   python network_audit.py

7. Check results in:
   network_audit_log.txt


