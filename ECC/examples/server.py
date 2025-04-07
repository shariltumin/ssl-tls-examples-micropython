import socket
import tls
import network
import ntptime

from wifi import key
ssid, pwd = key

# Set up WiFi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, pwd)
while not sta_if.isconnected():
    pass

print("Server IP:", sta_if.ifconfig()[0])

# ntptime.host = 'time.google.com'
ntptime.host = '216.239.35.12'
ntptime.timeout = 5
ntptime.settime()  # Syncs time with an NTP server

# Create ssl server context
ssl = tls.SSLContext(tls.PROTOCOL_TLS_SERVER)

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8443))
s.listen(5)

print("Waiting for connection...")
conn, addr = s.accept()
print("Connection from:", addr)

with open("ec_server.crt", "rb") as f:
     cert = f.read()
# with open("key.der", "rb") as f:
with open("ec_server.key", "rb") as f:
     key = f.read()

ssl.load_cert_chain(cert, key)
ssl_conn = ssl.wrap_socket(conn, server_side=True)
# ssl_conn = ssl.wrap_socket(conn, server_side=True, server_hostname='kaki5')

try:
    while True:
        print('Wait client message')
        # data = ssl_conn.read(1024)
        data = ssl_conn.readline()
        # data = ssl_conn.recv(1024)
        if not data:
            break
        # print('Get client message')
        print("Received:", data.decode())
        ssl_conn.write(b"Server response: " + data)
        # ssl_conn.sendall(b"Server response: " + data)
finally:
    ssl_conn.close()
    s.close()
print('Done')

