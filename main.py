import base64

password = input("Input: ")
encoded_da = base64.b64encode(password.encode('utf-8'))

print("Original password: ", password)
print("Encoded password: ", encoded_da)
