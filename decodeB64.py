import base64

base64_string = "RW5jb2RlIHRoaXMgdGV4dA=="
base64_bytes = base64_string.encode("ascii")

sample_string_bytes = base64.b64decode(base64_bytes)
sample_string = sample_string_bytes.decode("ascii")

print(f"\nEncoded string: {base64_string}")
print(f"\nDecoded string: {sample_string}")