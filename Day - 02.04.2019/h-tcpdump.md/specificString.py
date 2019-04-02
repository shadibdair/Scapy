from scapy.all import *
str1="google"
cnt=0
packet= rdpcap('CaptureFile.cap')
for i in range(0,len(packet)):
    if str1 == packet[i]:  
      cnt++
      print(cnt)
