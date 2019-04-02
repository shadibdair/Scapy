from scapy.all import *
packets = rdpcap('CaptureFile.cap')
for i in range(0,len(packets)):
   max = packets[i]
   if max > packets[i]:
      max = packets[i]
print(max)
