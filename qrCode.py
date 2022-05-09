#pip install qrcode

import qrcode

img = qrcode.make("https://linktr.ee/tushar3549")
img.save("linktree.jpg")


