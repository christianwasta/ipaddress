import socket
import requests
import os

host_ip = socket.gethostbyname(socket.gethostname())
print(f"Host IP: {host_ip}")

ip = requests.get("https://api.ipify.org").text
print(f"Public IP address: {ip}")

host_ip = os.getenv("HOST_IP", "Not provided")
print(f"Host IP_v4: {host_ip}")
