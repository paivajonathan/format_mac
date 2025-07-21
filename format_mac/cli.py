import sys
import re

def is_valid_mac(mac_address):
    """
    Checks if a given string is a valid MAC address.

    Args:
        mac_address (str): The string to be validated as a MAC address.

    Returns:
        bool: True if the string is a valid MAC address, False otherwise.
    """
    # Regex pattern for MAC addresses separated by colons or hyphens
    # Allows both uppercase and lowercase hexadecimal digits
    # Example formats: 01:23:45:67:89:AB or 01-23-45-67-89-AB
    pattern = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    
    return bool(pattern.match(mac_address))


def format_mac(mac: str):
    mac = mac.replace(":", "")
    formatted_mac = ""
    
    for i, c in enumerate(mac):
        if (i % 4 == 0) and (i != 0):
            formatted_mac += "-"
        formatted_mac += c
        
    return formatted_mac.upper()


def main():
    if len(sys.argv) < 2:
        print("Uso: format_mac <mac para converter>")
        return
    
    _, mac = sys.argv
    
    mac = mac.strip()
    
    if not is_valid_mac(mac):
        print("MAC inválido.")
        return
    
    print("display location", format_mac(mac))


if __name__ == "__main__":
    main()
