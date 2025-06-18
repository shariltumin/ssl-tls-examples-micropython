
This is an example for an MQTT client with mode 2 TLS handshake. The script and certificate are directly linked to a response to https://github.com/orgs/micropython/discussions/17096.

The "mqtt.py" is a copy of "lib/micropython-lib/micropython/umqtt.simple/umqtt/simple.py" with a slight modification where the socket connect and TLS handshake are done outside the library.

The example script, "std_emqxsl.py", uses the standard MicroPython MQTT library. The TLS handshake is performed in the ```connect()``` method. The ```client = MQTT.MQTTClient()``` uses the ```ssl_params={}``` to set the desired parameters for the ```ssl.wrap_socket()```. The "cadata" variable contains the intermediate certificate needed for mode 2 TLS. Please read "GET_CERT.txt" to learn how to obtain the certificates. You need to have "openssl" installed.
