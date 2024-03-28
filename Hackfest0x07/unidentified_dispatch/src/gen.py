from scapy.all import *
import random
import string
from cryptography.fernet import Fernet

encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

def encrypt(data):
    return cipher_suite.encrypt(data.encode())

data_lines = []
with open("data.txt", "r") as file:
    data_lines = file.read().splitlines()

packets = []

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

data_line_number = 0

for i in range(1, 1001):
    if is_prime(i):
        if data_line_number < len(data_lines):
            data = data_lines[data_line_number]
            data_line_number += 1
        else:
            data = "Data not available"
        packets.append(Ether() / Raw(data))
    else:
        if i % 4 == 0:
            host = "www.google.com"
            http_request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
            tcp_packet = Ether() / IP(dst=host) / TCP(sport=random.randint(1024, 65535), dport=80) / encrypt(http_request)
            packets.append(tcp_packet)
        elif i % 4 == 1:
            udp_payload = ''.join(random.choice(string.ascii_letters) for _ in range(20))
            udp_packet = Ether() / IP() / UDP() / encrypt(udp_payload)
            packets.append(udp_packet)
        elif i % 4 == 2:
            bluetooth_payload = ''.join(random.choice(string.hexdigits) for _ in range(20))
            bluetooth_packet = Ether() / Raw(encrypt(bluetooth_payload))
            packets.append(bluetooth_packet)
        else:
            icmp_packet = Ether() / IP() / ICMP()
            packets.append(icmp_packet)

# Saved to pcap file
wrpcap("unidentified.pcap", packets)
