import socket
import subprocess

def get_wifi_ipv4_address():
    try:
        # Run ipconfig command to get network interface information
        output = subprocess.check_output(['ipconfig'], shell=True)
        output = output.decode('cp1252')  # Decode byte string to Unicode using cp1252 encoding

        # Find the line containing the IPv4 address of the Wi-Fi interface
        lines = output.split('\n')
        for line in lines:
            if 'Wi-Fi' in line:
                
                next_line = lines[lines.index(line) + 4]
                if 'IPv4 Address' in next_line:
                    ip_start_index = next_line.find(':') + 2  # Find the starting index of IP address
                    ip_address = next_line[ip_start_index:]
                    
                    return ip_address.strip()  # Remove any leading/trailing whitespace
    except subprocess.CalledProcessError:
        return None


if __name__ == '__main__':
    # Get the IPv4 address of the Wi-Fi adapter
    wifi_ipv4_address = get_wifi_ipv4_address()

    print(wifi_ipv4_address)