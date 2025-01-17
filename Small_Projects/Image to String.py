from PIL import Image
import pytesseract

# Load the uploaded image
image_path = "/mnt/data/image.png"
image = Image.open(image_path)

# Perform OCR to extract text
extracted_text = pytesseract.image_to_string(image)
print(extracted_text)
