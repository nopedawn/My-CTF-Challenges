from PIL import Image, ImageOps

# Nama file yang berisi ASCII
filename = "qr.txt"

# Membuka file yang berisi ASCII
with open(filename, "r") as f:
    ascii_im = f.read()

# Membuat list dari ASCII
ascii_list = ascii_im.split("\n")

# Membuat gambar dari ASCII
im = Image.new("1", (len(ascii_list[0]), len(ascii_list)))
pixels = im.load()

for y in range(im.height):
    for x in range(im.width):
        if ascii_list[y][x] == "X":
            pixels[x, y] = 0
        else:
            pixels[x, y] = 1

# Mengatur resolusi gambar menjadi 500x500 pixel
im = im.resize((500,500), Image.NEAREST)

# Menambahkan border warna putih sebesar 20 pixel
im = ImageOps.expand(im, border=20, fill='white')
# im = ImageOps.pad(im, 20, "white")

# Simpan gambar
im.save("qr.jpg")
