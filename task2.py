from PIL import Image
import numpy as np
import os
import sys

def swap_pixels(img_array):
   
    return img_array[::-1]

def math_operation(img_array, operation='add', value=50):
    if operation == 'add':
        return np.clip(img_array + value, 0, 255)
    elif operation == 'subtract':
        return np.clip(img_array - value, 0, 255)
    elif operation == 'xor':
        return np.bitwise_xor(img_array, value)
    else:
        raise ValueError("Unsupported operation. Choose from 'add', 'subtract', or 'xor'.")

def encrypt_image(image_path, method='swap', operation='add', value=50, output_path='encrypted_image.png'):
    img = Image.open(image_path)
    img_array = np.array(img)

    if method == 'swap':
        encrypted_array = swap_pixels(img_array)
    elif method == 'math':
        encrypted_array = math_operation(img_array, operation, value)
    else:
        raise ValueError("Invalid method. Choose 'swap' or 'math'.")

    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_img.save(output_path)
    print(f" Encrypted image saved as: {output_path}")

def decrypt_image(encrypted_path, method='swap', operation='add', value=50, output_path='decrypted_image.png'):
    img = Image.open(encrypted_path)
    img_array = np.array(img)

    if method == 'swap':
        decrypted_array = swap_pixels(img_array)
    elif method == 'math':
        if operation == 'add':
            inverse_op = 'subtract'
        elif operation == 'subtract':
            inverse_op = 'add'
        elif operation == 'xor':
            inverse_op = 'xor'
        else:
            raise ValueError("Invalid operation during decryption.")
        decrypted_array = math_operation(img_array, inverse_op, value)
    else:
        raise ValueError("Invalid method. Choose 'swap' or 'math'.")

    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_img.save(output_path)
    print(f" Decrypted image saved as: {output_path}")

def main():
    input_image = "doll.jpg"

    if not os.path.exists(input_image):
        print(f" Image '{input_image}' not found.")
        sys.exit()

    mode = input("Choose mode: (E)ncrypt or (D)ecrypt: ").strip().lower()
    if mode not in ['e', 'd']:
        print(" Invalid mode. Choose 'E' for encrypt or 'D' for decrypt.")
        return

    method = input("Choose method: 'swap' or 'math': ").strip().lower()
    if method not in ['swap', 'math']:
        print(" Invalid method. Choose 'swap' or 'math'.")
        return

    if method == 'math':
        operation = input("Choose operation ('add', 'subtract', 'xor'): ").strip().lower()
        if operation not in ['add', 'subtract', 'xor']:
            print(" Invalid operation. Choose from 'add', 'subtract', 'xor'.")
            return
        try:
            value = int(input("Enter value (0–255, e.g., 50): "))
        except ValueError:
            print(" Value must be an integer.")
            return
    else:
        operation, value = None, None

    if mode == 'e':
        encrypt_image(input_image, method, operation, value)
    elif mode == 'd':
        decrypt_image(input_image, method, operation, value)

if __name__ == "__main__":
    main()
