import subprocess


if __name__ == "__main__":
    # Define our interface and mac address to be used
    nic = "enp1s0"
    new_mac = "22:11:22:33:44:57"

    # We will need to shutdown the interface to change MAC
    print("shutting down interface")
    subprocess.run(["ifconfig", nic, "down"])

    # Change the actual MAC address, we could want to capture old mac and save it
    # but rebooting will also return original MAC
    print(f"Changing mac address for interface {nic}")
    subprocess.run(["ifconfig", nic, "hw", "ether", new_mac])

    print(f"New mac address for interface {nic} is {new_mac}")
    subprocess.run(["ifconfig", nic, "up"])
    print(f"Interface {nic} up again")
