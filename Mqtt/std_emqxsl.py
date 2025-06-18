import network
import time
# import umqtt.simple as mqtt
import umqtt.robust as mqtt

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

# Load Intermediate CA certificate
with open("immd.emqxsl.cert") as f:
    cadata = f.read()

MQTT_BROKER = "y90166f4.ala.cn-hangzhou.emqxsl.cn"
user, pwd = 'test', 'test'

client = mqtt.MQTTClient('uf2', # client ID
                         MQTT_BROKER, 
                         user=user, 
                         password=pwd, 
                         keepalive=0, 
                         ssl=True,
                         ssl_params={'cert_reqs':2, # ssl.CERT_REQUIRED
                                     'cadata':cadata,
                                     'server_hostname':MQTT_BROKER})

# Connect
client.connect()

# Assign the callback
client.set_callback(on_message)

TOPIC = b"micropython/test"
# Subscribe
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

client.disconnect()
print('Done')

