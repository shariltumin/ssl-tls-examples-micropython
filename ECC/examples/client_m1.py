import socket
import tls
import network

from wifi import key
ssid, pwd = key

# Set up WiFi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, pwd)
while not sta_if.isconnected():
    pass

print("Client IP:", sta_if.ifconfig()[0])

# Create SSL client context
ssl = tls.SSLContext(tls.PROTOCOL_TLS_CLIENT)
ssl.verify_mode = tls.CERT_NONE

# Create socket
server_ip = "192.168.5.0" # Replace with server IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = socket.getaddrinfo(server_ip, 8443)[0][-1]  # Replace with server IP
s.connect(addr)

ssl_sock = ssl.wrap_socket(s, server_side=False) 

for i in range(5):
    try:
        print('Send to server')
        msg = f"Msg-{i} Hello from client!\n".encode()
        ssl_sock.write(msg)
        response = ssl_sock.readline()
        print("Server response:", response.decode())
    except Exception as e:
        print('Error:', e)
ssl_sock.close()
s.close()
print('Done')

