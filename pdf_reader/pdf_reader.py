import textract
import urllib.request
import os
import pdfplumber
# import camelot
from tabula import read_pdf
from tabulate import tabulate
import camelot


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


def write_to_file(text):
    current_directory = os.path.abspath(os.curdir)
    with open(current_directory+'/file/output.txt', 'w') as f:

        f.write(text)


def extract_table(pdf_file):
    # extract all the tables in the PDF file
    # address of file loation
    tables = camelot.read_pdf(pdf_file, pages='all')
    print(tables)
    print(dir(camelot))

    # print the first table as Pandas DataFrame
    # for tb in tables:
    #     print(tb.df)


def pdf_to_text(file_path):
    current_directory = os.path.abspath(os.curdir)
    pdf = current_directory + '/temp.pdf'

    urllib.request.urlretrieve(file_path, pdf)
    text = textract.process(pdf).decode()
    os.remove(pdf)

    return text


def get_content(link):
    text = pdf_to_text(link)

    search_term = "Alemtuzumab"
    is_term = text.find(f'1.1. {search_term} –')

    if is_term != -1:
        header_one = "1. Recommendations for update of the product information"
        header_two = "2. Recommendations for submission of supplementary"
        header_three = "3. Other recommendations"

        header_one_index = text.find(header_one)
        header_two_index = text.find(header_two)
        header_three_index = text.find(header_three)

        section_one = text[header_one_index:header_two_index]
        section_two = text[header_two_index:header_three_index]
        section_three = text[header_three_index:]

        print(section_one)


def use_tabula(file):
    tables = tabula.read_pdf(file, pages="all")


if __name__ == '__main__':
    file_path = "http://www.uncledavesenterprise.com/file/health/Food%20Calories%20List.pdf"
    file_path_two = "https://github.com/x4nth055/pythoncode-tutorials/blob/master/general/pdf-table-extractor/foo.pdf"
    path = 'https://www.ema.europa.eu/documents/prac-recommendation/' \
           'prac-recommendations-signals-adopted-3-6-may-2021-prac-meeting_en.pdf'

    # text = get_content(path)
    # print(text)

    extract_table(path)
