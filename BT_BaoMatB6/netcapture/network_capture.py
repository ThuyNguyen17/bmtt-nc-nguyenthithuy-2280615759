import subprocess
from scapy.all import sniff, IP, Raw
# một trình bắt gói tin mạng (Packet Sniffer), giúp theo dõi và phân tích lưu lượng mạng trên máy tính. Nó sử dụng Scapy để bắt gói tin IP và in ra nội dung của các gói tin có lớp Raw.
def get_interfaces():
    result = subprocess.run(["netsh", "interface", "show", "interface"],
                            capture_output=True, text=True)
    output_lines = result.stdout.splitlines()[3:]
    interfaces = [line.split()[3] for line in output_lines if len(line.split()) >= 4]
    return interfaces

def packet_handler(packet):
    if packet.haslayer(Raw):
        print("Captured Packet:")
        print(str(packet))

        interfaces = get_interfaces()

        print("List of network interfaces:")
        for i, iface in enumerate(interfaces, start=1):
            print(f"{i}. {iface}")

        choice = int(input("Select a network interface (enter a number): "))
        selected_iface = interfaces[choice - 1]

        # Use Layer 3 socket instead of Layer 2
        sniff(iface=selected_iface, prn=packet_handler, filter="ip")  # Change filter to IP

# Main function
if __name__ == '__main__':
    sniff(prn=packet_handler, filter="ip", store=0)  # Use IP filter instead of raw Ethernet packets
