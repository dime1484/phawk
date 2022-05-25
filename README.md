# Phawk \[INACTIVE\]
<p>
Phawk is a socket.py overlay with simplified syntax.
</p>

# How to use?
<p>
  As of now Phawk only has functions regarding UDP packets, 
  TCP is coming soon. This is the basic syntax:
  
```py
# Sending a UDP packet
import phawk
h = phawk.UDP(ip="127.0.0.1", port=4444)
h.send("Hello World")
```
 
```py
# Receiving a UDP packet
import phawk
con = phawk.UDP(lip="127.0.0.1", lport=4444)
con.get(buffer=1024)  
```

 Usage of exclusive listening is now supported. In this mode 
 hawk.UDP.get will only listen for packets coming from a
 set ip+port combination. Syntax:

```py
# Receiving a UDP packet with excl
import phawk
con = phawn.UDP(lip="127.0.0.1", lport=4444, ip="192.168.0.12", excl="y")
```

</p>

# To-do:

### High Priority
- Make Ctrl-C actually do it's intended purpose

### Mid Priority
- Add literally any functions for the TCP protocol

# Done:

- Added excl support
- Acquired a life
