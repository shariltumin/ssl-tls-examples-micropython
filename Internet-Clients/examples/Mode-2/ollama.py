import socket
import tls  # use tls directly
import network
import json
import ntptime

from wifi import key # (SSID, PWD)
ssid, pwd = key  # give correct cred for your wifi

# Set up WiFi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, pwd)
while not sta_if.isconnected():
    pass

print("Client IP:", sta_if.ifconfig()[0])

# ntptime.host = 'time.google.com'
ntptime.host = '216.239.35.12'
ntptime.timeout = 5
ntptime.settime()  # Syncs time with an NTP server


# Load Intermediate CA certificate
with open("intermediate.cert") as f:
    imcacert = f.read()

# Create SSL client context
ssl = tls.SSLContext(tls.PROTOCOL_TLS_CLIENT)
ssl.load_verify_locations(imcacert)

# Create socket
server = "ollama.com"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = socket.getaddrinfo(server, 443)[0][-1]  # Replace with server IP
s.connect(addr)

ssl_sock = ssl.wrap_socket(s, server_side=False, server_hostname=server) 


# Send HTTPS request
ssl_sock.write(f"GET /search?q=llama HTTP/1.1\r\nHost: {server}\r\n\r\n".encode())
print(ssl_sock.read(2048))  # Read response

ssl_sock.close()
s.close()
print('Done')

