from scapy.all import *
packets = rdpcap('CaptureFile.cap')
counter=0
for i in range(0,len(packets)):
    counter += 1 
print(counter)
