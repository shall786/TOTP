import pyotp
import qrcode
from PIL import Image

# Generate a secret key for the user's account
totp = pyotp.TOTP(pyotp.random_base32())
secret_key = totp.secret

# Generate the QR code for the secret key
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(totp.provisioning_uri("Mritunjay", issuer_name="Mritunjay_PWD"))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("qr_code.png")

# Display the QR code and secret key to the user
print("Scan this QR code using Google Authenticator app:")
Image.open("qr_code.png").show()
print("Or enter this secret key into the app:")
print(secret_key)

# Verify the user's code
user_input = input("Enter the code from Google Authenticator app: ")
if totp.verify(user_input):
    print("Authentication successful")
else:
    print("Authentication failed")
