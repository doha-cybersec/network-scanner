import os 
file = open("alive_devices.txt","w")
print("network scanner")
for i in range(1, 11):
   ip = "192.168.1." + str(i)
   result = os.system("ping -c 1 " + ip + " >/dev/null 2>&1")
   if result == 0:
      print(ip,"is alive")
      file.write(ip+"ip alive\n")
file.close()

