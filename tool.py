import argparse
def main():
    parser=argparse.ArgumentParser(description="simple hacking tool")
    parser.add_argument("-t","--target",help="Target IP or domain",required=True)
    args=parser.parse_args()
    print(f"Target Selected: {args.target}")
    if __name__=="__main__":
        main()

import socket
def scan_ports(target):
    print(f"Scanning {target}...")
    for port in range(1, 1025):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.settimeout(0.5)
        result =sock.connect_ex((target, port))
        if result == 0:
            print(f"[+]port {port}is open")
        sock.close()

