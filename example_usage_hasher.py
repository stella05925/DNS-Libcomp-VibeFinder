import string_hasher_python as vix

# Generate a hash value for a string
hash_value = vix.GENHASH("Hello World")
print(f"Hash value: {hash_value}")

if (hash_value==vix.GENHASH("Hello World")):
	print("Hash values matched")
else:
	print("Hash values did not match")
