import qrcode as qr
img = qr.make(input("What You Want : "))
img.save(input("enter your file name With (.png) : "))
print("Your QR Code Ready")