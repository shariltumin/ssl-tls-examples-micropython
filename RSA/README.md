
# OpenSSL Commands for generating keys and self-signed certificates.

```bash
openssl genrsa -des3 -out ca.key 2048

openssl req -new -x509 -days 1826 -key ca.key -out ca.crt

openssl genrsa -out server.pem 2048

openssl req -new -out server.csr -key server.pem

openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server_cert.der -days 1826

openssl genrsa -out server.pem 2048

openssl req -new -out client.csr -key client.pem

openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client_cert.der -days 1826

openssl rsa -inform pem -in server.pem -outform der -out server_key.der

openssl rsa -inform pem -in client.pem -outform der -out client_key.der
```

# OpenSSL Commands Explained

The following provides a detailed explanation of each OpenSSL command.

1. **`openssl genrsa -des3 -out ca.key 2048`**
   - This command generates a new RSA private key using OpenSSL.
   - `-des3`: Encrypts the key with DES3 (Triple DES) encryption to protect it with a passphrase.
   - `-out ca.key`: Specifies the output filename for the private key (`ca.key`).
   - `2048`: The key size in bits. A 2048-bit key is considered secure for most applications.

2. **`openssl req -new -x509 -days 1826 -key ca.key -out ca.crt`**
   - This generates a new self-signed X.509 certificate (CA certificate).
   - `-new`: Indicates a new certificate request.
   - `-x509`: Specifies that the certificate will be self-signed.
   - `-days 1826`: Sets the validity period of the certificate to 1826 days (approximately 5 years).
   - `-key ca.key`: Specifies the private key to sign the certificate (the `ca.key` from the previous command).
   - `-out ca.crt`: Specifies the output filename for the certificate (`ca.crt`).

3. **`openssl genrsa -out server.pem 2048`**
   - This generates a new RSA private key for the server.
   - `-out server.pem`: Specifies the output filename (`server.pem`).
   - `2048`: The key size in bits.

4. **`openssl req -new -out server.csr -key server.pem`**
   - This creates a Certificate Signing Request (CSR) for the server.
   - `-new`: Indicates a new CSR.
   - `-out server.csr`: Specifies the output filename for the CSR (`server.csr`).
   - `-key server.pem`: Specifies the private key to use for signing the CSR (the `server.pem` from the previous command).

5. **`openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server_cert.der -days 1826`**
   - This command signs the server's CSR (`server.csr`) using the CA's certificate (`ca.crt`) and private key (`ca.key`) to generate a valid certificate.
   - `-req`: Indicates the input is a CSR.
   - `-in server.csr`: Specifies the input CSR.
   - `-CA ca.crt`: Specifies the CA's certificate to use for signing.
   - `-CAkey ca.key`: Specifies the CA's private key to sign the certificate.
   - `-CAcreateserial`: Tells OpenSSL to create a new serial number for the certificate (if one doesn’t already exist).
   - `-out server_cert.der`: Specifies the output filename for the signed certificate (`server_cert.der`).
   - `-days 1826`: Sets the certificate’s validity period to 1826 days (approximately 5 years).

6. **`openssl genrsa -out server.pem 2048`**
   - Same as the previous `genrsa` command, this generates a new RSA private key for the server (`server.pem`) with a 2048-bit key.

7. **`openssl req -new -out client.csr -key client.pem`**
   - This creates a Certificate Signing Request (CSR) for the client.
   - `-new`: Indicates a new CSR.
   - `-out client.csr`: Specifies the output filename for the CSR (`client.csr`).
   - `-key client.pem`: Specifies the private key to use for signing the CSR (the `client.pem` private key).

8. **`openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client_cert.der -days 1826`**
   - This command signs the client’s CSR (`client.csr`) using the CA’s certificate (`ca.crt`) and private key (`ca.key`) to generate a valid client certificate.
   - `-req`: Indicates the input is a CSR.
   - `-in client.csr`: Specifies the input CSR.
   - `-CA ca.crt`: Specifies the CA's certificate to use for signing.
   - `-CAkey ca.key`: Specifies the CA's private key to sign the certificate.
   - `-CAcreateserial`: Tells OpenSSL to create a new serial number for the certificate (if one doesn’t already exist).
   - `-out client_cert.der`: Specifies the output filename for the signed certificate (`client_cert.der`).
   - `-days 1826`: Sets the certificate’s validity period to 1826 days (approximately 5 years).

9. **`openssl rsa -inform pem -in server.pem -outform der -out server_key.der`**
   - This command converts the server's private key from PEM format to DER format.
   - `-inform pem`: Specifies that the input format is PEM (the format in which `server.pem` is stored).
   - `-in server.pem`: Specifies the input private key.
   - `-outform der`: Specifies that the output format should be DER (binary format).
   - `-out server_key.der`: Specifies the output filename for the converted key (`server_key.der`).

10. **`openssl rsa -inform pem -in client.pem -outform der -out client_key.der`**
   - This command converts the client’s private key from PEM format to DER format.
   - `-inform pem`: Specifies that the input format is PEM (the format in which `client.pem` is stored).
   - `-in client.pem`: Specifies the input private key.
   - `-outform der`: Specifies that the output format should be DER (binary format).
   - `-out client_key.der`: Specifies the output filename for the converted key (`client_key.der`).

Use `ca.crt`, `server_key.der`, `server_cert.der`, `client_key.der`, and `client_cert.der` in your program.

     - `ca.crt`: The certificate authority’s public certificate.
     - `server_key.der`: The server’s private key in DER format.
     - `server_cert.der`: The server’s certificate in DER format.
     - `client_key.der`: The client’s private key in DER format.
     - `client_cert.der`: The client’s certificate in DER format.

These files are typically used in SSL/TLS, for encrypting and authenticating communications between the client and server, based on RSA and Triple DES.

You can use the keys and certificates in the examples if you are unable to create your own. The CN registered in the server certificate is 'kaki5'.

The ```ssl``` module is just a wrapper class for ```tls```. In all examples we ```import tls``` directly.


