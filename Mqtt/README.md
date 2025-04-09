
This is an example for an MQTT client with mode 2 TLS handshake. The script and certificate are directly linked to a response to https://github.com/orgs/micropython/discussions/17096.

The "mqtt.py" is a copy of "lib/micropython-lib/micropython/umqtt.simple/umqtt/simple.py" with a slight modification where the socket connect and TLS handshake are done outside the library.


