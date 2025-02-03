class Frame:
    def __init__(self, src_mac, dest_mac, payload):
        self.src_mac = src_mac
        self.dest_mac = dest_mac
        self.payload = payload

    def serialize(self):
        # Create a string format for the frame
        return f"{self.dest_mac}|{self.src_mac}|{self.payload}".encode()

    @staticmethod
    def deserialize(frame_data):
        # Convert the frame back into readable components
        parts = frame_data.decode().split('|')
        return Frame(parts[1], parts[0], parts[2])

# Example frame creation
frame = Frame("AA:BB:CC:DD:EE:FF", "ZZ:YY:XX:WW:VV:UU", "Hello, Network!")
serialized_frame = frame.serialize()
print(f"Serialized Frame: {serialized_frame}")

# Deserialize the frame
received_frame = Frame.deserialize(serialized_frame)
print(f"Received Frame - From: {received_frame.src_mac}, To: {received_frame.dest_mac}, Data: {received_frame.payload}")
