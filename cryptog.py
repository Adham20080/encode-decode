from cryptography.fernet import Fernet

message = input("Enter: ")
keyw = Fernet.generate_key()
fernet = Fernet(keyw)
encrypted = fernet.encrypt(message.encode())

print(message)
print(encrypted)
