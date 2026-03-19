# Image Processing Script (WebP + Consistent Sizing)

This project provides a simple Python script to:

- Convert images to **WebP format**
- Resize images to a consistent size
- Maintain aspect ratio (no stretching)
- Center-crop images when necessary

---

## 🛠️ Requirements

- Python 3.x
- Pillow

Install dependencies:

```
pip install pillow
```

---

## 📦 Usage

1. Place your images inside a `.zip` file named:

```
images.zip
```

2. The script will automatically extract into:

```
images_input/
```

3. Run the script:

```
python process_images.py
```

---

## ⚙️ What It Does

- Extracts images from `images.zip`
- Crops them to match a target aspect ratio
- Resizes them to a fixed size (default: 1280x720)
- Converts them to `.webp` format
- Saves them into:

```
images_webp/
```

---

## 🧠 Key Function

```python
def crop_and_resize(img, target_size):
```

- Preserves proportions
- Crops from center
- Avoids distortion

---

## 📁 Folder Structure

```
images.zip
images_input/
images_webp/
```

---

## 🎯 Customization

You can change output size here:

```python
target_size = (1280, 720)
```

Examples:
- (800, 800) → square
- (1920, 1080) → full HD
- (600, 900) → portrait

---

## 🤖 AI Attribution

This script and workflow were generated with the help of AI (ChatGPT), based on a real-world need to standardize UI images without distortion.

---

## 📅 Generated

2026-03-19

---

## 🚀 Notes

- Works with PNG, JPG, JPEG, and WEBP
- Optimized for UI consistency
- Great for portfolios, apps, and galleries
