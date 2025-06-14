import socket
import requests
import os

host_ip = socket.gethostbyname('host.docker.internal')
print(f"Host IP_host.docker.internal: {host_ip}")

public_ip = requests.get("https://api.ipify.org").text
print(f"Public IP address: {public_ip}")

host_ip_2 = os.getenv("HOST_IP", "Not provided")
print(f"Host IP_v4: {host_ip_2}")
