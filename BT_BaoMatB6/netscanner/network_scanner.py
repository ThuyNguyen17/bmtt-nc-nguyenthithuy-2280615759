import requests
from scapy.all import ARP, Ether, srp
# quét và liệt kê các thiết bị đang kết nối trong một mạng cục bộ (LAN) hoặc trên Internet. Nó giúp xác định địa chỉ IP, địa chỉ MAC,
def local_network_scan(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({
            'ip': received.psrc,
            'mac': received.hwsrc,
            'vendor': get_vendor_by_mac(received.hwsrc)
        })

    return devices

def get_vendor_by_mac(mac):
    try:
        response = requests.get(f"https://api.macvendors.com/{mac}")
        if response.status_code == 200:
            return response.text
        else:
            return "Unknown"
    except Exception as e:
        print("Error fetching vendor information:", e)
        return "Unknown"

def main():
    ip_range = "10.14.66.1/24"  # Thử thay đổi dải IP ở đây
    devices = local_network_scan(ip_range)

    print("Devices on the local network:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}, Vendor: {device['vendor']}")

if __name__ == '__main__':
    main()
