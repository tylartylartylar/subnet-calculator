def to_binary(address: str) -> tuple[str, list]:
    octets = address.split('.')
    bin_list = []
    for octet in octets:
        decimal = int(octet)
        binary = bin(decimal)[2:].zfill(8)
        bin_list.append(binary)
    bin_string = '.'.join(bin_list)
    return bin_string, bin_list

def get_cidr(netmask: str) -> str:
    clean_mask = netmask.replace('.', '')
    count = sum(1 for bit in clean_mask if bit == '1')
    return f"/{count}"

def get_networkRange(ip: str, cidr: str):
    # Given: IP 192.168.1.1 and CIDR /24
    # Need to calculate:
    # - Network address (first address in range)
    # - Broadcast address (last address in range)
    # - Usable range (network address + 1 to broadcast address - 1)
    pass

def main():
    ip_address = input("Enter IPv4 address: ")
    netmask = input("Enter netmask as XXX.XXX.XXX.XXX: ")
    
    binary_str, binary_list = to_binary(ip_address)
    netmask_str, netmask_list = to_binary(netmask)
    cidr = get_cidr(netmask_str)
    
    print(f"\nIP Address: {ip_address}")
    print(f"Binary: {binary_str}")
    print(f"Netmask: {netmask}")
    print(f"Netmask Binary: {netmask_str}")
    print(f"CIDR: {cidr}")

if __name__ == "__main__":
    main()