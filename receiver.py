import socket
from dataFrame import Frame

# Host B listens for incoming frames
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 10000))  # Listening on the same address

while True:
    data, address = sock.recvfrom(4096)
    frame = Frame.deserialize(data)
    print(f"Received Frame - From: {frame.src_mac}, To: {frame.dest_mac}, Data: {frame.payload}")
