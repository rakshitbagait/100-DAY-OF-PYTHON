import qrcode

# Data to encode
data = "HELLO123"

# Create QR Code instance
qr = qrcode.QRCode(
    version=1,  # version 1 = 21x21 matrix
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level L
    box_size=10,  # Size of each box in pixels
    border=4,  # Border (default is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)  # Fit the QR code to the input

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qr_code.png")

print("QR code generated and saved as my_qr_code.png")
