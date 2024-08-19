import pytesseract as tess
from PIL import Image

# Set the path to the Tesseract OCR executable
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def crop_and_read_text(image_path, crop_box):
    # Open the image using Pillow (PIL)
    img = Image.open(image_path)
    # Resize  
    fixed_resolution = (1920, 1080)
    img = img.resize(fixed_resolution)
    img.show()
    # Crop the image using the specified box (left, top, right, bottom)
    cropped_img = img.crop(crop_box)
    # Display the cropped image
    cropped_img.show()
    # Perform OCR on the cropped image
    cropped_text = tess.image_to_string(cropped_img)

    return cropped_text

def find_currency_type(cropped_text):
    currency_types = ["USD", "EUR", "JPY", "GBP", "CHF", "CAD", "AUD", "CNY", "SEK", "LKR"]

    for currency in currency_types:
        if currency in cropped_text:
            return currency
    # If none of the currency types are found
    return "Unknown Currency"

if __name__ == "__main__":
    # Specify the path to your image
    image_path = 'LKR.png'
    # Define the crop box (left, top, right, bottom)
    crop_box = (837, 499, 1237, 569)  # Adjust these values based on your requirement
    crop_box_2 = (837, 499, 1237, 569)
    # Crop and read text
    cropped_text = crop_and_read_text(image_path, crop_box)
    cropped_text_2 = crop_and_read_text(image_path, crop_box_2)
    # detect currency
    detected_currency = find_currency_type(cropped_text)
    detected_currency_2 = find_currency_type(cropped_text_2)
    
    print("Detected Currency 1:", detected_currency)
    print("Detected Currency 2:", detected_currency_2)
    