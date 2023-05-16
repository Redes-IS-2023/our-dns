import base64

binary_data = b"\xdb\xe9\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x06google\x03com\x00\x00\x01\x00\x01"

# Writes the bytes to a bin file
with open("sample/package.bin", "wb") as f:
    f.write(binary_data)

# Converts binary data to base64
base64_data = base64.b64encode(binary_data)

# Writes base64 data to file
with open("sample/b64.txt", "w") as f:
    f.write(base64_data.decode("utf-8"))
