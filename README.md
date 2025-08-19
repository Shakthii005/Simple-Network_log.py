# Simple Network log Automation 

This mini-project connects to multiple Linux devices using **Netmiko**, runs a set of commands, and saves results into a single log file.

---

## 🚀 Features
- Connects to multiple devices via SSH
- Executes basic commands (`hostname`, `whoami`, `pwd`)
- Handles errors during connection attempts

---

## ⚡ Installation & Usage

1. Clone the repo:
   https://github.com/Shakthii005/Network_log_Automation-using-Netmiko.py.git
   cd Network_log_Automation-using-Netmiko.py
   
3. Install dependencies:
   pip install -r requirements.txt
   
5. Update the devices in network_audit.py:
    devices =
    
    {"device_type": "your device type", "host": "your device ip", "username": "your device username", "password": "your device password"},
   
    {"device_type": "your device type", "host": "your device ip", "username": "your device username", "password": "your device password"},
}

7. Run the script: 
   Network_log_Automation-using-Netmiko.py

8. Check results in: 
   network_audit_log.txt


