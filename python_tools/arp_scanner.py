from scapy.all import (
        srp,
        ARP,
        Ether
        )

if __name__ == "__main__":
    broadcast = "FF:FF:FF:FF:FF:FF"
    ip_range = "192.168.122.1/24"
    nic = "enp1s0"

    ether_layer = Ether(dst=broadcast)
    arp_layer = ARP(pdst=ip_range)

    packet = ether_layer/arp_layer
    ans, unans = srp(packet, iface=nic, timeout=2)
    for send, receive in ans:
        ip = receive[ARP].psrc
        mac = receive[Ether].src
        print(f"IP: {ip}, MAC: {mac}")
