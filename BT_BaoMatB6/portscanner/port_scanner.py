import socket

# Kiểm tra kết nối: Sử dụng công cụ như ping để kiểm tra xem một thiết bị có đang hoạt động trên mạng không.
# Lấy IP từ tên miền.
# Duyệt qua danh sách COMMON_PORTS, thử kết nối từng cổng.
# Nếu cổng mở, hiển thị danh sách cổng mở.

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

def scan_common_ports(target_ip, timeout=2):
    open_ports = []
    for port in COMMON_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def main():
    target_domain = input("Enter the target domain: ").strip()
    
    try:
        target_ip = socket.gethostbyname(target_domain)
        print(f"Scanning {target_domain} ({target_ip})...\n")
    except socket.gaierror:
        print("Invalid domain. Please check the target domain.")
        return

    open_ports = scan_common_ports(target_ip)

    if open_ports:
        print("\nOpen common ports:")
        print(", ".join(map(str, open_ports)))
    else:
        print("\nNo open common ports found.")

if __name__ == "__main__":
    main()
