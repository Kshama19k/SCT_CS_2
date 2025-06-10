# 🔐 Image Encryption Tool

## 📝 Task Overview

Develop a **simple image encryption tool** using **pixel manipulation** techniques. This tool enables image encryption and decryption by modifying pixel values through operations such as:
- Swapping pixel positions
- Applying mathematical transformations (e.g., addition, subtraction, XOR)

---

## 🚀 Features

- 🔄 Encrypt and decrypt images using reversible logic
- 🔢 Apply pixel transformations such as:
  - Value shifting (`+n` / `-n`)
  - Pixel value inversion (`255 - pixel`)
  - XOR encryption with a secret key
  - Swapping pixels in a predefined/random pattern

---

## 🧰 Requirements

- Python 3.x
- Required Python packages:
  - `Pillow` – for image processing
  - `NumPy` – for efficient pixel matrix handling

### 📦 Install Dependencies

Run the following command to install required packages:

```bash
pip install pillow numpy
python image_encryptor.py --mode encrypt --input input_image.png --output encrypted_image.png --key 42
python image_encryptor.py --mode decrypt --input encrypted_image.png --output decrypted_image.png --key 42

