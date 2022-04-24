import phawk

con = phawk.UDP(lip="127.0.0.1", lport=4444)

con.get(buffer=1024)
