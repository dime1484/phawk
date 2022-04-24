import phawk

h = phawk.UDP(ip="127.0.0.1", port=4444)

h.send("Hello World")
