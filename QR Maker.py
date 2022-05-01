import qrcode
link - input("Input Link")
img - qrcode.make(link)
img.save(link + "qr.png")
show img
