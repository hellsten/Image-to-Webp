import os
import zipfile
from PIL import Image

input_zip = "images.zip"
extract_dir = "images_input"
output_dir = "images_webp"

target_size = (1280, 720)  # change if needed

os.makedirs(extract_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(input_zip, "r") as zip_ref:
    zip_ref.extractall(extract_dir)

def crop_and_resize(img, target_size):
    target_w, target_h = target_size
    img_ratio = img.width / img.height
    target_ratio = target_w / target_h

    if img_ratio > target_ratio:
        new_width = int(img.height * target_ratio)
        left = (img.width - new_width) // 2
        img = img.crop((left, 0, left + new_width, img.height))
    else:
        new_height = int(img.width / target_ratio)
        top = (img.height - new_height) // 2
        img = img.crop((0, top, img.width, top + new_height))

    return img.resize(target_size, Image.LANCZOS)

for root, _, files in os.walk(extract_dir):
    for file in files:
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            in_path = os.path.join(root, file)
            out_name = os.path.splitext(file)[0] + ".webp"
            out_path = os.path.join(output_dir, out_name)

            img = Image.open(in_path).convert("RGB")
            processed = crop_and_resize(img, target_size)
            processed.save(out_path, "WEBP", quality=90)

print("Done. WebP images are in:", output_dir)