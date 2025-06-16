import os
import socket
import subprocess

def get_host_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception as e:
        print(f"Error getting host IP: {e}")
        return None

host_ip = get_host_ip()
print(f"Host IP: {host_ip}")
