from netmiko import ConnectHandler
from datetime import datetime

devices = [

    {
    "device_type": "your device type",
    "host": "your device ip",
    "username": "your device username",
    "password": "your device password"
  },
  {
      "device_type": "your device type",
      "host": "your device ip",
      "username": "your device username",
      "password": "your device password"
  },

]
commands = ['hostname', 'whoami', 'pwd']
master_log = "network_audit_log.txt"
try:            
    for device in devices:
        print(f"Connecting to {device['host']}...")
        connection = ConnectHandler(**device)
    
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        
        with open(master_log, 'a') as f:
            f.write(f"\n==== Device: {device['host']} | Time: {timestamp} ====\n")
            for cmd in commands:
                output = connection.send_command(cmd)
                f.write(f"\n--- Command: {cmd} ---\n")
                f.write(output + '\n') 


        connection.disconnect()
        print(f"Disconnected from {device['host']}\n")
except Exception as e:
    print(f"Error connecting to {device['host']}: {e}")
print(f"Output saved to {master_log}\n")