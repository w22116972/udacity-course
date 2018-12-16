
#### To connect to web server

1. Client needs to translate the hostname into an IP address
2. My OS network configuration uses the Domain Name Service (DNS)
3. DNS(a set of servers maintained by Internet Service Providers (ISPs)) look up hostnames and get back IP addresses.

```bash
host URL # show IPv4 address and IPv6 address
```

- localhost(IPv4) = `127.0.0.1`
- localhost(IPv6) = `::1` = `0000:0000:0000:0000:0000:0000:0000:0001`
- `0.0.0.0` = **All** IPv4 address **on this computer**, include localhost

#### why `en.wikipedia.org` and `ja.wikipedia.org` have same address

A single web server can have lots of different web sites running on it, each with their own hostname. 
When a client asks the server for a resource, it has to specify what hostname it intends to be talking to.

## Ports

IP addresses distinguish computers; port numbers distinguish *programs* on those computers.

**Listen on port**: when the server starts up, it tells its operating system that it wants to receive connections from clients on a particular port number. When a client (such as a web browser) "connects to" that port and sends a request, the operating system knows to forward that request to the server that's listening on that port.

- default port of **HTTP** URL = `80`
- default port of **HTTPS** URL = `443`

---

# Request 

Every request contains **HTTP verb or method** to tell server **what client is asking server to do**

#### `GET`: ask server to send copy of resource to client 

```bash
127.0.0.1 - - [15/Dec/2018 09:11:29] "GET /readme.png HTTP/1.1" 200 -
```

- `"GET /readme.png HTTP/1.1"`: request line, server 告訴你他收到的請求長這樣
- `GET`: **method** to ask server to send copy of resource to client 
- `/readme.png`: **path** of resource being requested
- `HTTP/1.1`: **protocol** of request 

# HTTP response

```bash
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.7.1
Date: Sun, 16 Dec 2018 15:52:33 GMT
Content-type: text/html; charset=utf-8
Content-Length: 528
```

- `HTTP/1.0 200 OK`: status line with status code 
- Headers, line starts with **keyword**
    - `Content-type: text/html; charset=utf-8`: The server is telling the client that the response body is an HTML document written in UTF-8 text.