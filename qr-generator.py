# 1. pip install qrcode

# 2. import qrcode
import qrcode

# 3. Define link
link = "YOUR_LINK"

# 4. Create QR Instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 5. Add data to the QR 
qr.add_data(link)
qr.make(fit=True)

# 6. Create an image from the QR code instance
qr_image = qr.make_image(fill_color="black", back_color="white")

# 7. Save the QR
qr_image.save("qr_code.png")