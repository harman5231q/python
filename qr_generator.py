from PIL import Image, ImageDraw, ImageFont
import qrcode

def generate_qr_code(data, size=100, border_color="grey"):
    # qr code variable for operations
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img




data=input("Enter your data you Want to make QR code of : ")
img_name=input("Enter the name you want to save QR code as : ")
img_name=img_name+".png"
qr_img = generate_qr_code(data)

qr_img.save(img_name)

print("You have succesfully generated QR code. ")
print("Find your QR code in current folder.")
