import PyPDF2
import re
import os
path = "/home/teetayo/python_play/pdf_trial/All Invoices/All Invoices/ImageLinks/Done"
files = os.listdir(path)

def extract_text_from_pdf(pdf_file: str) -> str:
    with open(pdf_file, 'rb') as pdf:
        reader  = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = ""

        for page in reader.pages:
            content = page.extract_text()
            pdf_text += content
        
        return pdf_text
    

if __name__ == '__main__':
    for file in files:
        try:
            extracted_text = extract_text_from_pdf(path+"/"+file)
            string = extracted_text
            
            string = re.findall(r'\d{1,3}?,?\d{1,3}?,?\d{1,3}\.\d{2}', string)
            string = [str(x).strip().replace(",","") for x in string]
            unique_string = set(string)
            unique_string = list(map(float, unique_string))
            max_val = max(unique_string)
            file = file.strip("ND WESTERN")
            print(file.strip(".pdf"), end=",")
            print(max_val)
        except Exception as e:
           print(e)
        

    
    