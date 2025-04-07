
# OpenSSL Commands for generating keys and self-signed certificates

```bash
openssl ecparam -genkey -name secp384r1 -out ec_ca.key

openssl req -new -x509 -key ec_ca.key -out ec_ca.crt -days 2190

openssl ecparam -genkey -name secp384r1 -out ec_server.key

openssl req -new -key ec_server.key -out ec_server.csr

openssl x509 -req -in ec_server.csr -CA ec_ca.crt -CAkey ec_ca.key -CAcreateserial -out ec_server.crt -days 2190

openssl ecparam -genkey -name secp384r1 -out ec_client.key

openssl req -new -key ec_client.key -out ec_client.csr

openssl x509 -req -in ec_client.csr -CA ec_ca.crt -CAkey ec_ca.key -CAcreateserial -out ec_client.crt -days 2190
```

# OpenSSL EC Commands Explained

The following provides a detailed explanation of each OpenSSL command related to elliptic curve cryptography (ECC).

## 1. `openssl ecparam -genkey -name secp384r1 -out ec_ca.key`
   - This command generates a new elliptic curve (EC) private key using the `secp384r1` curve.
   - `ecparam`: The OpenSSL command used for EC operations.
   - `-genkey`: Instructs OpenSSL to generate a private key.
   - `-name secp384r1`: Specifies the elliptic curve to use. `secp384r1` is a standard curve with a 384-bit key size.
   - `-out ec_ca.key`: Specifies the output filename for the private key (`ec_ca.key`).

## 2. `openssl req -new -x509 -key ec_ca.key -out ec_ca.crt -days 2190`
   - This command generates a self-signed X.509 certificate for a Certificate Authority (CA) using the EC private key generated in the previous command.
   - `-new`: Indicates a new certificate request.
   - `-x509`: Instructs OpenSSL to create a self-signed certificate (as opposed to a certificate signing request).
   - `-key ec_ca.key`: Specifies the private key to sign the certificate (`ec_ca.key`).
   - `-out ec_ca.crt`: Specifies the output filename for the certificate (`ec_ca.crt`).
   - `-days 2190`: Sets the validity of the certificate to 2190 days (approximately 6 years).

## 3. `openssl ecparam -genkey -name secp384r1 -out ec_server.key`
   - This generates a new EC private key for the server using the `secp384r1` elliptic curve.
   - `ecparam`: The OpenSSL command used for EC operations.
   - `-genkey`: Instructs OpenSSL to generate a private key.
   - `-name secp384r1`: Specifies the elliptic curve (`secp384r1`).
   - `-out ec_server.key`: Specifies the output filename for the server's private key (`ec_server.key`).

## 4. `openssl req -new -key ec_server.key -out ec_server.csr`
   - This command creates a Certificate Signing Request (CSR) for the server.
   - `-new`: Indicates a new CSR.
   - `-key ec_server.key`: Specifies the private key (`ec_server.key`) to sign the CSR.
   - `-out ec_server.csr`: Specifies the output filename for the CSR (`ec_server.csr`).

## 5. `openssl x509 -req -in ec_server.csr -CA ec_ca.crt -CAkey ec_ca.key -CAcreateserial -out ec_server.crt -days 2190`
   - This command signs the server's CSR (`ec_server.csr`) with the CA's certificate (`ec_ca.crt`) and private key (`ec_ca.key`), generating the server's certificate.
   - `-req`: Indicates that the input is a CSR.
   - `-in ec_server.csr`: Specifies the input CSR (`ec_server.csr`).
   - `-CA ec_ca.crt`: Specifies the CA's certificate to use for signing (`ec_ca.crt`).
   - `-CAkey ec_ca.key`: Specifies the CA's private key to sign the server’s certificate (`ec_ca.key`).
   - `-CAcreateserial`: Tells OpenSSL to create a new serial number for the certificate (if one doesn’t already exist).
   - `-out ec_server.crt`: Specifies the output filename for the signed server certificate (`ec_server.crt`).
   - `-days 2190`: Sets the certificate’s validity period to 2190 days (approximately 6 years).

## 6. `openssl ecparam -genkey -name secp384r1 -out ec_client.key`
   - This generates a new EC private key for the client using the `secp384r1` elliptic curve.
   - `ecparam`: The OpenSSL command used for EC operations.
   - `-genkey`: Instructs OpenSSL to generate a private key.
   - `-name secp384r1`: Specifies the elliptic curve (`secp384r1`).
   - `-out ec_client.key`: Specifies the output filename for the client’s private key (`ec_client.key`).

## 7. `openssl req -new -key ec_client.key -out ec_client.csr`
   - This command creates a Certificate Signing Request (CSR) for the client.
   - `-new`: Indicates a new CSR.
   - `-key ec_client.key`: Specifies the private key (`ec_client.key`) to sign the CSR.
   - `-out ec_client.csr`: Specifies the output filename for the CSR (`ec_client.csr`).

## 8. `openssl x509 -req -in ec_client.csr -CA ec_ca.crt -CAkey ec_ca.key -CAcreateserial -out ec_client.crt -days 2190`
   - This command signs the client's CSR (`ec_client.csr`) with the CA's certificate (`ec_ca.crt`) and private key (`ec_ca.key`), generating the client's certificate.
   - `-req`: Indicates that the input is a CSR.
   - `-in ec_client.csr`: Specifies the input CSR (`ec_client.csr`).
   - `-CA ec_ca.crt`: Specifies the CA's certificate to use for signing (`ec_ca.crt`).
   - `-CAkey ec_ca.key`: Specifies the CA's private key to sign the client’s certificate (`ec_ca.key`).
   - `-CAcreateserial`: Tells OpenSSL to create a new serial number for the certificate (if one doesn’t already exist).
   - `-out ec_client.crt`: Specifies the output filename for the signed client certificate (`ec_client.crt`).
   - `-days 2190`: Sets the certificate’s validity period to 2190 days (approximately 6 years).

Use `ec_ca.crt`, `ec_server.crt`, `ec_server.key`, `ec_client.crt`, `ec_client.key` in your program
   - This statement indicates that your program should use the following files:
     - `ec_ca.crt`: The certificate of the Certificate Authority (CA).
     - `ec_server.crt`: The server's signed certificate.
     - `ec_server.key`: The server’s private key.
     - `ec_client.crt`: The client's signed certificate.
     - `ec_client.key`: The client's private key.

Each of these commands is part of the process of creating a public key infrastructure (PKI) system using elliptic curve cryptography (ECC) with the `secp384r1` curve. The generated private keys, CSRs, and signed certificates are used for encryption, authentication, and securing communication between clients and servers.

You can view the contents of a certificate:
```bash
openssl x509 -in ec_client.crt -text -noout
```

You can use the keys and certificates in the examples if you are unable to create your own. The CN registered in the server certificate is 'kaki5'.
 
The ```ssl``` module is just a wrapper class for ```tls```. In all examples we ```import tls``` directly.
