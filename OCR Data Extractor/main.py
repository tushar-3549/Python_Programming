import cv2
import pytesseract
from pdf2image import convert_from_path
import numpy as np

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    extracted_txt = ""
    for img in images:
        extracted_txt += pytesseract.image_to_string(img) + "\n"
    return extracted_txt

def extract_text_from_jpg(jpg_path):
    img = cv2.imread(jpg_path)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    file_path = 'medicine_report.jpg'
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_jpg(file_path)
    print("\nExtracted data:\n", text)



# gray scale convert , blur remve , thresholding
'''
import cv2
import pytesseract
import numpy as np

def preprocess_image(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) 
    img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]  
    img = cv2.GaussianBlur(img, (3, 3), 0)
    return img

def extract_text_from_png(png_path):
    img = preprocess_image(png_path)
    text = pytesseract.image_to_string(img, lang="eng") 
    return text

if __name__ == "__main__":
    file_path = "medicine_report.jpg"
    extracted_text = extract_text_from_png(file_path)
    print("\nExtracted Text:\n", extracted_text)
'''