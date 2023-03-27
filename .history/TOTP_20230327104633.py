import pyotp
import qrcode

# Generate a secret key for the user's account
totp = pyotp.TOTP(pyotp.random_base32())
secret_key = totp.secret

# Generate the QR code for the secret key
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(totp.provisioning_uri("user@example.com", issuer_name="My App"))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Display the QR code and secret key to the user
print("Scan this QR code using Google Authenticator app:")
img.show()
print("Or enter this secret key into the app:")
print(secret_key)

# Verify the user's code
user_input = input("Enter the code from Google Authenticator app: ")
if totp.verify(user_input):
    print("Authentication successful")
else:
    print("Authentication failed")
