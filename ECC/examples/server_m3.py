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
     server_cert = f.read()
with open("ec_server.key", "rb") as f:
     server_key = f.read()
with open("ec_ca.crt", "rb") as f:
     ca_cert = f.read()

ssl.verify_mode = tls.CERT_REQUIRED          # Require client certificate
ssl.load_cert_chain(server_cert, server_key) # server certificate
ssl.load_verify_locations(ca_cert)           # CA certificate

ssl_conn = ssl.wrap_socket(conn, 
           server_side=True, )
try:
    while True:
        print('Wait client message')
        data = ssl_conn.readline()
        if not data:
            break
        # print('Get client message')
        print("Received:", data.decode())
        ssl_conn.write(b"Server response: " + data)
finally:
    ssl_conn.close()
    s.close()
print('Done')

