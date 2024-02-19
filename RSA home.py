import rsa

public_key, private_key = rsa.newkeys(1024)
message = 'Hello World!'.encode('utf8')

ciphertext = rsa.encrypt(message, public_key)
message2 = rsa.decrypt(ciphertext, private_key)

print(ciphertext)
print(message2)
print(message2.decode('utf8'))

# Digital Signature and Harsh

data = 'Hello World Again!'.encode('utf8')
data2 = 'Hello World2'.encode('utf8')
Hash = rsa.compute_hash(data2, 'SHA-1')

signature = rsa.sign(data, private_key, 'SHA-1')
signature2 = rsa.sign_hash(Hash, private_key, 'SHA-1')

rsa.verify(data, signature, public_key)

# Manba: https://medium.com/@metechsolutions/python-by-examples-rsa-encryption-decryption-d07a226430b4 # noqa
