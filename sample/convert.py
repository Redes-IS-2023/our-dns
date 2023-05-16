import base64

# binary_data = b"\xdb\xe9\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x06google\x03com\x00\x00\x01\x00\x01"
bin_file = "sample/out/package.bin"
b64_file = "sample/out/b64.txt"


# Writes the bytes from a bin file to a encoded b64 plain text
def encode_file_to_b64(input_file, output_file):
    with open(input_file, "rb") as f_in:
        binary_data = f_in.read()

    b64_data = base64.b64encode(binary_data)

    with open(output_file, "wb") as f_out:
        f_out.write(b64_data)


encode_file_to_b64(bin_file, b64_file)
