import cv2
import numpy as np
import os

def combine_images(images, rows, cols):
    num_images = len(images)
    grid_width = cols * images[0].shape[1]
    grid_height = rows * images[0].shape[0]

    combined_image = np.zeros((grid_height, grid_width, 3), dtype=np.uint8)

    for i in range(rows):
        for j in range(cols):
            index = i * cols + j

            if index < num_images:
                img = images[index]
                img = cv2.resize(img, (images[0].shape[1], images[0].shape[0]))
                combined_image[i*img.shape[0]:(i+1)*img.shape[0], j*img.shape[1]:(j+1)*img.shape[1]] = img

    return combined_image

# Mengambil daftar nama file gambar dari frame299.jpg sampai frame382.jpg
image_paths = ['data/frame{}.jpg'.format(i) for i in range(299, 383)]

# Membaca gambar-gambar
images = []
for path in image_paths:
    img = cv2.imread(path)
    images.append(img)

# Menggabungkan 84 gambar dalam satu frame
combined_image = combine_images(images, rows=7, cols=12)

# Menyimpan gambar hasil ke file JPG
output_file = 'combined_image.jpg'
cv2.imwrite(output_file, combined_image)

print(f"Output file: `{output_file}`.")
