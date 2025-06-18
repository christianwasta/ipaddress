import os
import socket
import subprocess
import requests

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host_ip_3 = s.getsockname()[0]
s.close()
print(f"Host IP: {host_ip_3}")

public_ip = requests.get("https://api.ipify.org").text
print(f"Public IP address: {public_ip}")

host_ip_2 = os.getenv("HOST_IP", "Not provided")
print(f"Host IP_v4: {host_ip_2}")
