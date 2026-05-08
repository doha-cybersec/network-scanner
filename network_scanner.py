import os
import platform
import datetime

def ping(ip):
   
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    result = os.system(f"ping {param} -w 1000 {ip} > {'nul' if platform.system().lower() == 'windows' else '/dev/null'} 2>&1")
    return result == 0

def scan_network(base_ip, start=1, end=254):
    print(f"\n Scanning network: {base_ip}.{start} → {base_ip}.{end}")
    print("-" * 40)
    
    alive = []
    for i in range(start, end + 1):
        ip = f"{base_ip}.{i}"
        if ping(ip):
            print(f"   {ip} is ALIVE")
            alive.append(ip)
        else:
            print(f"   {ip}", end="\r")  # overwrite line
    
    return alive

def save_results(alive_devices):
    filename = f"alive_devices_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(f"Scan date: {datetime.datetime.now()}\n")
        f.write(f"Alive devices found: {len(alive_devices)}\n\n")
        for ip in alive_devices:
            f.write(f"{ip} - ALIVE\n")
    print(f"\n Results saved to {filename}")

if __name__ == "__main__":
    base_ip = input("Enter base IP (ex: 192.168.1): ").strip()
    alive = scan_network(base_ip, start=1, end=10)
    
    print(f"\n Summary: {len(alive)} device(s) found")
    if alive:
        save_results(alive)

