# Connecting IoT Clients to Cloud Servers Using SSL/TLS

In our IoT applications, we will write internet client scripts that use **SSL/TLS** to securely connect to cloud servers. Depending on the level of security and resources available, we can use different TLS handshake modes.

## TLS Handshake Modes

We typically consider three modes of TLS handshakes in IoT systems:

### 🔹 Mode 1 – Simplified Handshake (No Authentication)
- **Use case:** Default for resource-constrained IoT clients.
- **Description:** The client does **not validate** the server’s certificate.
- **Pros:** Faster and uses fewer resources.
- **Cons:** Not secure — vulnerable to man-in-the-middle (MITM) attacks.

### 🔹 Mode 2 – Server Authentication
- **Use case:** When we need to **trust the server’s identity**.
- **Description:** The client authenticates the server using its **TLS certificate** and a trusted **intermediate CA certificate**.
- **Requirement:** The intermediate certificate that signed the server's certificate must be available on the client side.
- **Pros:** Secures the connection by verifying the server.
- **Cons:** Requires managing certificate files on the client.

### 🔹 Mode 3 – Mutual Authentication (Not Supported in Our Setup)
- **Use case:** Both client and server verify each other.
- **Why not used:** 
  - Our client certificates are **self-signed**.
  - Our clients have **non-static IP addresses** outside the local network.
  - This makes mutual verification impractical in many real-world IoT deployments.

## Extracting the Intermediate CA Certificate

Suppose we want to connect securely to `ollama.com` using **Mode 2**. We’ll need to extract its intermediate CA certificate.

### 🔧 Step 1: Fetch the Full Certificate Chain

Use OpenSSL to connect to the server and dump the full certificate chain:

```bash
$ openssl s_client -showcerts -connect ollama.com:443 </dev/null > ollama.cert
```

This saves all certificates (root, intermediate, and server) into a file called ollama.cert.

You might see output like:

```
depth=2 C = US, O = Google Trust Services LLC, CN = GTS Root R1
verify return:1
depth=1 C = US, O = Google Trust Services, CN = WR3
verify return:1
depth=0 CN = ollama.com
verify return:1
DONE
```

Save the CN ("ollama.com") we will need this in our script.

### 🔧 Step 2: Extract Only the Intermediate Certificate

Now, we’ll clean up the file to keep only the intermediate certificate:

```bash
$ cp ollama.cert intermediate.cert
$ vi intermediate.cert
```

Inside the file:

    1st certificate (depth=2) → Root CA → ❌ Delete

    2nd certificate (depth=1) → Intermediate CA → ✅ Keep this

    3rd certificate (depth=0) → Server certificate → ❌ Delete

After editing, the file should contain only one certificate, like this:

```
-----BEGIN CERTIFICATE-----
... (base64 data) ...
-----END CERTIFICATE-----
```

This is our intermediate certificate, which we'll use to verify the server’s identity (ollama.com).



### 🔧 Using the Intermediate Certificate in Our Script

When using Mode 2 in your IoT client:

    Include the intermediate.cert file.

    Configure our client script or firmware to verify the server’s certificate against this intermediate.

    This ensures we're truly talking to the trusted server (e.g. ollama.com) and not a fake one.

### This what we will do

    Use Mode 1 when simplicity and low resource usage are the priority (no server verification).

    Use Mode 2 when security matters — this requires the intermediate CA certificate.

    Mode 3 is not practical in our setup due to self-signed client certs and dynamic IPs.

This balance gives us flexibility between performance and security in different scenarios.

The ```ssl``` module is just a wrapper class for ```tls```. In all examples we ```import tls``` directly.

