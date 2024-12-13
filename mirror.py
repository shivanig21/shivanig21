import qrcode
from PIL import Image


# Create a QR code object
qr = qrcode.QRCode(
    version=4,  # Controls the size of the QR Code (1 is smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Thickness of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data("https://www.instagram.com/mirrorpro_adfilms/reel/DDNSpvGzfo0/")
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="red", back_color="white")

# Save the image
img.save("mirror.png")

print("QR Code generated and saved as qr_code.png")