
# Mode 1 test:

Server (server.py):

```
$ mpr u0 mount .
Local directory . is mounted at /remote
Connected to MicroPython at /dev/ttyUSB0
Use Ctrl-] or Ctrl-x to exit this shell
>>> import server
Server IP: 192.168.5.0
Waiting for connection...
Connection from: ('192.168.4.101', 49243)
Wait client message
Received: Msg-0 Hello from client!

Wait client message
Received: Msg-1 Hello from client!

Wait client message
Received: Msg-2 Hello from client!

Wait client message
Received: Msg-3 Hello from client!

Wait client message
Received: Msg-4 Hello from client!

Wait client message
Done
```

Client (client_m1.py):

```
$ mpr u1 mount .
Local directory . is mounted at /remote
Connected to MicroPython at /dev/ttyUSB1
Use Ctrl-] or Ctrl-x to exit this shell
>>> import client_m1
Client IP: 192.168.4.101
Send to server
Server response: Server response: Msg-0 Hello from client!

Send to server
Server response: Server response: Msg-1 Hello from client!

Send to server
Server response: Server response: Msg-2 Hello from client!

Send to server
Server response: Server response: Msg-3 Hello from client!

Send to server
Server response: Server response: Msg-4 Hello from client!

Done
```

---

# Mode 2 test:

Run the "server.py" as above

Client (client_m2.py):

```
$ mpr u1 mount .
Local directory . is mounted at /remote
Connected to MicroPython at /dev/ttyUSB1
Use Ctrl-] or Ctrl-x to exit this shell

>>> import client_m2
Client IP: 192.168.4.101
Send to server
Server response: Server response: Msg-0 Hello from client!

Send to server
Server response: Server response: Msg-1 Hello from client!

Send to server
Server response: Server response: Msg-2 Hello from client!

Send to server
Server response: Server response: Msg-3 Hello from client!

Send to server
Server response: Server response: Msg-4 Hello from client!

Done
>>> 
```

---

# Mode 3 test:

Server (server_m3.py):

```
$ mpr u0 mount .
Local directory . is mounted at /remote
Connected to MicroPython at /dev/ttyUSB0
Use Ctrl-] or Ctrl-x to exit this shell
>>> import server_m3
...
```

Client (client_m3.py):

```
$ mpr u1 mount .
Local directory . is mounted at /remote
Connected to MicroPython at /dev/ttyUSB1
Use Ctrl-] or Ctrl-x to exit this shell

>>> import client_m3
...
```

You may have to wait for the handshake to complete. Elliptic curve cryptography (ECC) provides better performance than RSA.
