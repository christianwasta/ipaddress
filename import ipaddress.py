import os
import socket
import subprocess
import requests

def get_host_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception as e:
        print(f"Error getting host IP: {e}")
        return None

public_ip = requests.get("https://api.ipify.org").text
print(f"Public IP address: {public_ip}")

host_ip_2 = os.getenv("HOST_IP", "Not provided")
print(f"Host IP_v4: {host_ip_2}")

host_ip_3 = get_host_ip()
print(f"Host IP: {host_ip_3}")
