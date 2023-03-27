import time
import pyotp
import qrcode

key = "Mritunjay"

uri = pyotp.totp.TOTP(key).provisioning_uri(
	name='Mritunjaysp',
	issuer_name='GeeksforGeeks')

print(uri)


# Qr code generation step
qrcode.make(uri).save("qr.png")

"""Verifying stage starts"""

totp = pyotp.TOTP(key)

# verifying the code
while True:
print(totp.verify(input(("Enter the Code : "))))
