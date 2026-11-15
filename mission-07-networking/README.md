# Mission 7 — Networking

## 1. Objective

To understand basic networking concepts, how devices communicate over networks, and how websites are accessed through the Internet.

## 2. Types of Networks

- **LAN (Local Area Network):** Connects devices within a small geographical area, such as a home, school, or office.
- **MAN (Metropolitan Area Network):** Connects networks across a city or metropolitan area.
- **WAN (Wide Area Network):** Covers large geographical areas and connects networks across cities, countries, or continents. The Internet is a major example.

## 3. Networking Concepts

- **DNS (Domain Name System):** Translates human-readable domain names into IP addresses.
- **Router:** Forwards data packets between different networks.
- **Network Protocol:** A set of rules that devices follow to communicate. Examples include HTTP, HTTPS, TCP, and UDP.
- **Packet Switching:** Divides data into smaller packets that travel through a network and are reassembled at the destination.
- **Client-Server Architecture:** The client requests resources or services, while the server processes requests and provides responses.

## 4. Practical Networking Commands

I practised the following commands:

| Command                 | Purpose |

| `nslookup google.com`   | Performs a DNS lookup for a domain |

| `ping -c 4 google.com`  | Sends four packets to test connectivity |

### DNS Lookup Result

- DNS server: `8.8.8.8`
- Resolved domain: `google.com`
- Returned IP address: `142.251.221.206`
- Result: Successful DNS resolution.

### Ping Result

- Packets transmitted: 4
- Packets received: 4
- Packet loss: 0%
- Average round-trip time: 23.549 ms

The test confirmed that the destination responded to all four packets.

## 5. Latency and Bandwidth

- **Latency:** The time taken for data to travel between devices. It is commonly measured using round-trip time in milliseconds (ms).
- **Bandwidth:** The maximum data-transfer capacity of a network connection, commonly measured in Mbps or Gbps.

Lower latency is generally important for responsive online gaming, while higher bandwidth allows more data to be transferred per second.

## 6. How a Website Loads

1. The user enters a domain name, such as `www.google.com`, into the browser.
2. DNS resolves the domain name into the server's IP address.
3. The browser establishes a connection with the server.
4. The browser sends an HTTP/HTTPS request for the webpage.
5. The server processes the request and sends an HTTP response.
6. The response data travels back to the client in network packets.
7. The browser processes the received resources and renders the webpage.

## 7. What I Learned

I learned how different types of networks work, how DNS resolves domain names, and how routers forward data between networks.

I also understood packet switching, client-server architecture, latency, bandwidth, and the basic process of loading a website.

Through practical commands, I successfully performed a DNS lookup and tested network connectivity using ping.

## 8. Files and Evidence

- `README.md` — Mission documentation.
- Practical command outputs: `nslookup` and `ping`.

## 9. Commit Details

- Commit message: `Complete Mission 7`
- Branch: `main`