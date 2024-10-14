import qrcode

img = qrcode.make("https://tanialonso.github.io/cv/index.html")

img.save("qr_cv.png")
