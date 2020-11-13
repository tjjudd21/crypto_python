"""
Base64 encoding is used to convert bytes that have binary or text data into ASCII characters. 
Encoding prevents the data from getting corrupted when it is processed through a text-only 
system.
"""

import base64 

sample_string = "Encode this text"
sample_string_bytes = sample_string.encode("ascii") #converts the string into a byte-like object

base64_bytes = base64.b64encode(sample_string_bytes) #encoded using base64
base64_string = base64_bytes.decode("ascii")

print(f"\nOriginal string: {sample_string}")
print(f"\nEncoded string: {base64_string}")