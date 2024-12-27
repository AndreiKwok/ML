import os
from PIL import Image
import numpy as np
image = f"{os.getcwd()}\Image.ppm"
print(image)



def rgb_to_grayscale_and_binary(input_path, grayscale_output, binary_output, threshold=128):
    # Carregar a imagem colorida
    image = Image.open(input_path)
    
    # Converter para numpy array
    image_array = np.array(image)
    
    # Converter para tons de cinza usando a fórmula: gray = 0.2989 * R + 0.5870 * G + 0.1140 * B
    grayscale_array = (
        0.2989 * image_array[:, :, 0] + 
        0.5870 * image_array[:, :, 1] + 
        0.1140 * image_array[:, :, 2]
    ).astype(np.uint8)
    
    # Salvar a imagem em tons de cinza
    grayscale_image = Image.fromarray(grayscale_array)
    grayscale_image.save(grayscale_output)
    
    # Converter para binário (preto e branco) usando o limiar
    binary_array = np.where(grayscale_array > threshold, 255, 0).astype(np.uint8)
    
    # Salvar a imagem binarizada
    binary_image = Image.fromarray(binary_array)
    binary_image.save(binary_output)

# path of files
input_image_path = f"{os.getcwd()}\Image.jpg"  
grayscale_output_path = "grayscale_image.jpg"
binary_output_path = "binary_image.jpg"

rgb_to_grayscale_and_binary(input_image_path, grayscale_output_path, binary_output_path)

print("Imagens processadas e salvas!")
"""
infos

How define parametres related with formula:gray = 0.2989 * R + 0.5870 * G + 0.1140 * B
ITU-R Recommendation BT.601: This document provides the standard for studio encoding parameters of digital television, including the derivation of luminance coefficients. You can access it here: 
ITU

"Standard" RGB to Grayscale Conversion - Stack Overflow: This discussion explores various methods and standards for converting RGB images to grayscale, including the rationale behind different coefficient choices. Read more at: 
STACK OVERFLOW

Image Processing 101 Chapter 1.3: Color Space Conversion: This article delves into color space conversions, explaining the significance of different coefficients in grayscale conversion. Find it here: 
DYNAMSOFT

RGB to Grayscale Conversion - Mustafa Murat ARAT: This resource provides an in-depth look at various formulas for RGB to grayscale conversion and their applications. Check it out at: 
MMURATARAT



"""