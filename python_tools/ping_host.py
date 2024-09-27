from scapy.all import (
        IP,
        ICMP,
        sr1,
        )

if __name__ == "__main__":
    src_ip = "192.168.122.168"
    dst_ip = "www.google.com"

    # Create a ICMP ping package layer at a time.
    ip_layer = IP(src=src_ip, dst=dst_ip)
    icmp_req = ICMP(id=100)
    packet = ip_layer / icmp_req

    response = sr1(packet, iface="enp1s0")
    if response:
        print(response.show())
