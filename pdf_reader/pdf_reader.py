import textract
import urllib.request
import os
# import pdfplumber


def use_texttract(file_path):
    current_directory = os.path.abspath(os.curdir)
    pdf = current_directory + '/temp.pdf'

    urllib.request.urlretrieve(file_path, pdf)

    text = textract.process(pdf).decode()

    os.remove(pdf)
    return text


# def use_pdfplumber(file_path):
#     current_directory = os.path.abspath(os.curdir)
#     pdf = current_directory + '/temp.pdf'
#     urllib.request.urlretrieve(file_path, pdf)

#     pdf = pdfplumber.open(pdf)
#     page = pdf.pages[0]
#     text = page.extract_text()
#     pdf.close()

#     os.remove(pdf)
#     return text


if __name__ == '__main__':
    file_path = 'https://www.ema.europa.eu/documents/prac-recommendation/prac-recommendations-signals-adopted-3-6-may-2021-prac-meeting_en.pdf'

    text = use_texttract(file_path)

    current_directory = os.path.abspath(os.curdir)
    with open(current_directory+'/file/output.docx', 'w') as f:

        f.write(text)
