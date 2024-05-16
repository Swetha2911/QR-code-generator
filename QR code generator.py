pip install qrcode
import qrcode

# Define the data you want to encode in the QR code (text,link etc..)
data = ""

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)

qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode_example.png")

print("QR code generated successfully!")

img.show()
