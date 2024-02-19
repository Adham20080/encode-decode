from cryptography.fernet import Fernet

message = input("Enter: ")
keyw = Fernet.generate_key()
fernet = Fernet(keyw)
encrypted = fernet.encrypt(message.encode())

# decode

decrypted = fernet.decrypt(encrypted).decode()

print(message)
print(encrypted)
print(decrypted)
