
# Convert decimal format IP address to Binary format
def convert_to_binary(ip_address):
    octets = ip_address.split('.')
    binary_octets = []
    
    for octet in octets:
        decimal_value = int(octet)
        binary_value = bin(decimal_value)[2:].zfill(8)
        binary_octets.append(binary_value)
    
    binary_address = '.'.join(binary_octets)
    return binary_address, binary_octets

# Outputs the CIDR notation for a given binary subnet mask
def get_cidr_notation(binary_netmask):
    normalized_mask = binary_netmask.replace('.', '')
    network_bits = sum(1 for bit in normalized_mask if bit == '1')
    return f"/{network_bits}"

# calculates the network and broadcast address given an IP address and a CIDR range
def calculate_network_range(binary_ip, cidr):
    prefix_length = int(cidr.replace("/", ""))
    normalized_ip = binary_ip.replace(".", "")
    
    network_prefix = normalized_ip[:prefix_length]
    host_zeros = "0" * (32 - prefix_length)
    host_ones = "1" * (32 - prefix_length)
    
    network_address = network_prefix + host_zeros
    broadcast_address = network_prefix + host_ones
    
    network_formatted = '.'.join(network_address[i:i+8] for i in range(0, 32, 8))
    broadcast_formatted = '.'.join(broadcast_address[i:i+8] for i in range(0, 32, 8))
    
    return network_formatted, broadcast_formatted

# converts a binary formatted IP address or netmask into decimal format with . separating each octet.
def convert_to_decimal(binary_address):
    octets = binary_address.split('.')
    decimal_octets = [str(int(octet, 2)) for octet in octets]
    return '.'.join(decimal_octets)

def display_menu():
    print("\nAvailable Operations:")
    print("1. Display IP/Netmask Conversion")
    print("2. Calculate Network Range")
    print("3. Exit")
    return input("Select option (1-3): ")

def main():
    while True:
        ip_address = input("Enter IPv4 address: ")
        netmask = input("Enter netmask (e.g., 255.255.255.0): ")
        
        binary_ip, ip_octets = convert_to_binary(ip_address)
        binary_netmask, netmask_octets = convert_to_binary(netmask)
        cidr_notation = get_cidr_notation(binary_netmask)
        
        selection = display_menu()
        
        if selection == "1":
            print("\nAddress Information:")
            print(f"IPv4 Address: {ip_address}")
            print(f"Binary: {binary_ip}")
            print(f"Netmask: {netmask}")
            print(f"Netmask (Binary): {binary_netmask}")
            print(f"CIDR Notation: {cidr_notation}")
            
        elif selection == "2":
            network_address, broadcast_address = calculate_network_range(binary_ip, cidr_notation)
            
            print("\nNetwork Range Information:")
            print(f"IPv4 Address: {ip_address}")
            print(f"Binary Address: {binary_ip}")
            print(f"Network Address: {convert_to_decimal(network_address)}")
            print(f"Network Address (Binary): {network_address}")
            print(f"Broadcast Address: {convert_to_decimal(broadcast_address)}")
            print(f"Broadcast Address (Binary): {broadcast_address}")
            print(f"Network Bits: {cidr_notation.replace('/', '')}")
            
        elif selection == "3":
            print("Exiting")
            break
            
        else:
            print("Invalid selection. Please try again.")

        if input("\nCalculate another address? (y/n): ").lower() != 'y':
            print("Exiting")
            break

if __name__ == "__main__":
    main()