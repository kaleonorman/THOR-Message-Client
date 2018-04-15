# THOR Message Client

### THOR Protocol
This project is part of the THOR protocol that allows a message to travel through a network of servers using HTTP. The protocol uses Onion Routing where the message contains multiple layers of encryption, making the source of traffic anonymous.

### THOR Message Client
The THOR Message Client is a Python applicaiton that sends a message through a list of IP addresses on the THOR network. Before sending the message out, it first goes through multiple layers of encryption, and each encryption includes a randomly assigned IP address.




### Create VirtualEnvironment
```
mkdir THOR-Message-Client
cd THOR-Message-Client
virtualenv env
source env/bin/activate
```

### Install Crypto
``` pip install pycryptodome ```