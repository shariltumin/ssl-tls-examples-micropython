import socket
import tls  # use tls directly
import network
import json
# import ntptime

from wifi import key # (SSID, PWD)
ssid, pwd = key  # give correct cred for your wifi

# Set up WiFi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, pwd)
while not sta_if.isconnected():
    pass

print("Client IP:", sta_if.ifconfig()[0])

# do not use certificate - no need for correct time
# # ntptime.host = 'time.google.com'
# ntptime.host = '216.239.35.12'
# ntptime.timeout = 5
# ntptime.settime()  # Syncs time with an NTP server

# Create SSL client context
ssl = tls.SSLContext(tls.PROTOCOL_TLS_CLIENT)
ssl.verify_mode = tls.CERT_NONE
# tls.check_hostname = False

# api.open-meteo.com (94.130.142.35)
# Create socket
server_ip = "94.130.142.35" # Replace with server IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = socket.getaddrinfo(server_ip, 443)[0][-1]  # Replace with server IP
s.connect(addr)

ssl_sock = ssl.wrap_socket(s, server_side=False) 

lat,log = 60.3913,5.3221 # change this to your city

req = f"""GET /v1/forecast?latitude={lat}&longitude={log}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m HTTP/1.1\r\nHost: api.open-meteo.com\r\nConnection: close\r\n\r\n"""

for i in range(1):
    try:
        print('Get weather')
        msg = f"Msg-{i} Hello from client!\n".encode()
        ssl_sock.write(req.encode())
        data = b''
        while True:
            response = ssl_sock.readline()
            if response:
               if len(response) > 100:
                  data += response
            else:
               break
        if data:
           wdata = json.loads(data.decode())
           print(json.dumps(wdata))
    except Exception as e:
        print('Error:', e)
ssl_sock.close()
s.close()
print('Done')

