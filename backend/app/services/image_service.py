import easyocr

reader = easyocr.Reader(['en'])

def extract_image_text(image_path):

    results = reader.readtext(image_path)

    extracted_text = ""

    for item in results:
        extracted_text += item[1] + " "

    return extracted_text