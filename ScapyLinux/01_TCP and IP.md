# TCP

* TCP - layer 4 (with udp) - in TCP we have the ports
* IP - layer 3 - In IP we have dist address and src address
* Ethernet - layer 2 (with blutooth) - In Ethernet we have dist address and src address of the MAC

#### With scapy, we can check all the properties of TCP:
```
ls(TCP())
sport      : ShortEnumField                      = 20              (20)
dport      : ShortEnumField                      = 80              (80)
seq        : IntField                            = 0               (0)
ack        : IntField                            = 0               (0)
dataofs    : BitField (4 bits)                   = None            (None)
reserved   : BitField (3 bits)                   = 0               (0)
flags      : FlagsField (9 bits)                 = <Flag 2 (S)>    (<Flag 2 (S)>)
window     : ShortField                          = 8192            (8192)
chksum     : XShortField                         = None            (None)
urgptr     : ShortField                          = 0               (0)
options    : TCPOptionsField                     = []              (b'')
```
#### With scapy, we can check all the properties of IP:
```
ls(IP())
version    : BitField (4 bits)                   = 4               (4)
ihl        : BitField (4 bits)                   = None            (None)
tos        : XByteField                          = 0               (0)
len        : ShortField                          = None            (None)
id         : ShortField                          = 1               (1)
flags      : FlagsField (3 bits)                 = <Flag 0 ()>     (<Flag 0 ()>)
frag       : BitField (13 bits)                  = 0               (0)
ttl        : ByteField                           = 64              (64)
proto      : ByteEnumField                       = 0               (0)
chksum     : XShortField                         = None            (None)
src        : SourceIPField                       = '127.0.0.1'     (None)
dst        : DestIPField                         = '127.0.0.1'     (None)
options    : PacketListField                     = []              ([])
```

#### Change properties of IP
```
a=IP(src="1.1.1.1")  # here we change the src of this IP
ls(a)

version    : BitField (4 bits)                   = 4               (4)
ihl        : BitField (4 bits)                   = None            (None)
tos        : XByteField                          = 0               (0)
len        : ShortField                          = None            (None)
id         : ShortField                          = 1               (1)
flags      : FlagsField (3 bits)                 = <Flag 0 ()>     (<Flag 0 ()>)
frag       : BitField (13 bits)                  = 0               (0)
ttl        : ByteField                           = 64              (64)
proto      : ByteEnumField                       = 0               (0)
chksum     : XShortField                         = None            (None)
src        : SourceIPField                       = '1.1.1.1'       (None)
dst        : DestIPField                         = '127.0.0.1'     (None)
options    : PacketListField                     = []              ([])

```

```
a=IP(dst="1.1.1.1")  # here we change the src of this IP
ls(a)

version    : BitField (4 bits)                   = 4               (4)
ihl        : BitField (4 bits)                   = None            (None)
tos        : XByteField                          = 0               (0)
len        : ShortField                          = None            (None)
id         : ShortField                          = 1               (1)
flags      : FlagsField (3 bits)                 = <Flag 0 ()>     (<Flag 0 ()>)
frag       : BitField (13 bits)                  = 0               (0)
ttl        : ByteField                           = 64              (64)
proto      : ByteEnumField                       = 0               (0)
chksum     : XShortField                         = None            (None)
src        : SourceIPField                       = '10.6.3.56'     (None)
dst        : DestIPField                         = '1.1.1.1'       (None)
options    : PacketListField                     = []              ([])


```