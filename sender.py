import socket
from dataFrame import Frame

# Host A sends a frame
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)  # Simulating a local network

frame = Frame("AA:BB:CC:DD:EE:FF", "ZZ:YY:XX:WW:VV:UU", "Hello from Host A!")
sock.sendto(frame.serialize(), server_address)
sock.close()
