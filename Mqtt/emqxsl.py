import socket
import tls  # use tls directly
import network
import time
import ntptime
import mqtt

from wifi import key # (SSID, PWD)
ssid, pwd = key  # give correct cred for your wifi

# Define the message handler
def on_message(topic, message):
    print(f"Received message: Topic={topic.decode()}, Message={message.decode()}")

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
with open("immd.emqxsl.cert") as f:
    imcacert = f.read()

# Create SSL client context
ssl = tls.SSLContext(tls.PROTOCOL_TLS_CLIENT)
ssl.load_verify_locations(imcacert)

# Create socket
server = "y90166f4.ala.cn-hangzhou.emqxsl.cn"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = socket.getaddrinfo(server, 8883)[0][-1]  # Replace with server IP
s.connect(addr)

MQTT_BROKER = "y90166f4.ala.cn-hangzhou.emqxsl.cn"
user, pwd = 'test', 'test'

ssl_sock = ssl.wrap_socket(s, server_side=False, server_hostname=MQTT_BROKER) 

client = mqtt.MQTTClient('uf2', MQTT_BROKER, port=8883, user=user, password=pwd, keepalive=0, ssl=ssl_sock) 

# Assign the callback
client.set_callback(on_message)

TOPIC = b"micropython/test"
# Connect and subscribe
client.connect(ssl_sock)
client.subscribe(TOPIC)
print(f"Connected to MQTT broker: {MQTT_BROKER}, Subscribed to: {TOPIC.decode()}")

# Publish a test message
client.publish(TOPIC, b"Hello from MicroPython!")
print("Published message")

i = 0
# Wait for incoming messages (non-blocking)
try:
    while True:
        client.check_msg()
        time.sleep(3)
        i += 1
        msg = f"This is message number {i}, next message in 3 seconds."
        client.publish(TOPIC, msg.encode())

except KeyboardInterrupt:
    client.disconnect()
    print("Disconnected from MQTT broker")

s.close()
print('Done')

