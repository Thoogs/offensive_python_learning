import subprocess


if __name__ == "__main__":
    nic = "enp1s0"
    new_mac = "22:11:22:33:44:57"

    print("shutting down interface")
    subprocess.run(["ifconfig", nic, "down"])
    print(f"Changing mac address for interface {nic}")
    subprocess.run(["ifconfig", nic, "hw", "ether", new_mac])
    print(f"New mac address for interface {nic} is {new_mac}")
    subprocess.run(["ifconfig", nic, "up"])
    print(f"Interface {nic} up again")
