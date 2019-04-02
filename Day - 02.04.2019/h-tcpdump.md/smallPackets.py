from scapy.all import *
packets = rdpcap('CaptureFile.cap')
min = packets[0]
for i in range(1,len(packets)):
  if packets[i] < min:
    min = packets[i]
print(min)
