import textract
import urllib.request
import os
import pdfplumber


def use_texttract(file_path):
    current_directory = os.path.abspath(os.curdir)
    pdf = current_directory + '/temp.pdf'

    urllib.request.urlretrieve(file_path, pdf)

    text = textract.process(pdf).decode()

    os.remove(pdf)
    return text


def use_pdfplumber(file_path):
    current_directory = os.path.abspath(os.curdir)
    pdf = current_directory + '/temp.pdf'
    urllib.request.urlretrieve(file_path, pdf)

    pdf = pdfplumber.open(pdf)
    page = pdf.pages[0]
    text = page.extract_text()
    pdf.close()

    os.remove(pdf)
    return text


if __name__ == '__main__':
    file_path = 'https://www.bfarm.de/SharedDocs/Kundeninfos/EN/01/2021/21994-20_kundeninfo_en.pdf;jsessionid=D2C8EF2B0DE147C315FE08B2985EE04C.1_cid506?__blob=publicationFile&v=2'

    text = use_texttract(file_path)
    print(text)
