# Phawk
<p>
Phawk is a socket.py overlay with simplified syntax.
It's another one of my projects that I made because 
of frustration with a library.
</p>

# How to use?
<p>
  As of now Phawk only has functions regarding UDP packets, 
  TCP is coming soon. Anyway, this is the basic syntax:
  
```py
# Sending a UDP packet
import phawk
h = hawk.UDP(ip="127.0.0.1", port=4444)
h.send("Hello World")
```
 
```py
# Receiving a UDP packet
import phawk
con = hawk.UDP(lip="127.0.0.1", lport=4444)
con.get(buffer=1024)  
```
  
</p>

# To-do:

### High Priority
- Fix the excl=True/False kwarg
- Make Ctrl-C actually do it's intended purpose

### Mid Priority
- Add literally any functions for the TCP protocol

### Low Priority
- Get a life
