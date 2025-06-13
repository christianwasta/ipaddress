import socket
import requests

host_ip = socket.gethostbyname("host.docker.internal")
print(f"Host IP: {host_ip}")

ip = requests.get("https://api.ipify.org").text
print(f"Public IP address: {ip}")
