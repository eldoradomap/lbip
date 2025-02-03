# Function to convert a letter-based MAC address to a numerical value (for easier processing)
def letter_mac_to_int(mac_address):
    parts = mac_address.split(':')
    int_mac = []
    for part in parts:
        num = (ord(part[0]) - ord('A')) * 26 + (ord(part[1]) - ord('A'))
        int_mac.append(num)
    return int_mac

# Function to convert a numerical MAC back to a letter-based format
def int_to_letter_mac(int_mac):
    mac_address = []
    for num in int_mac:
        first_letter = chr((num // 26) + ord('A'))
        second_letter = chr((num % 26) + ord('A'))
        mac_address.append(f"{first_letter}{second_letter}")
    return ':'.join(mac_address)

# Example usage
mac_address = "AA:BB:CC:DD:EE:FF"
converted = letter_mac_to_int(mac_address)
print(f"Converted to integers: {converted}")

reversed_mac = int_to_letter_mac(converted)
print(f"Converted back to letters: {reversed_mac}")
