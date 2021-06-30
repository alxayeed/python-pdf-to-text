import textract
import urllib.request
import os
import pdfplumber
import tabula
from tabulate import tabulate
import camelot
import re
from pdf2docx import Converter, parse

from input_output import links


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


def use_tabula(file):
    tables = tabula.read_pdf(file, pages="all")


def pdf_to_text(file_path):
    """ converts a pdf file into text"""
    current_directory = os.path.abspath(os.curdir)
    pdf = current_directory + '/temp.pdf'

    urllib.request.urlretrieve(file_path, pdf)
    text = textract.process(pdf).decode()
    os.remove(pdf)

    return text


def get_sections_text(pdf_file):
    """Split the whole text of pdf into 3 main sections"""
    text = pdf_to_text(pdf_file)

    header_one = "1. Recommendations for update of the product information"
    header_two = "2. Recommendations for submission of supplementary"
    header_three = "3. Other recommendations"

    header_one_index = text.find(header_one)
    header_two_index = text.find(header_two)
    header_three_index = text.find(header_three)

    section_one = text[header_one_index:header_two_index]
    section_two = text[header_two_index:header_three_index]
    section_three = text[header_three_index:]

    return section_one, section_two, section_three


def extract_table_data(pdf_file, page):
    # extract tabular data of a specific page from a pdf
    tables = camelot.read_pdf(pdf_file, pages=f'{page}')

    return tables[0].df


def get_subsection_text(sub_section, keyword, pdf_path):
    """Splits a section into it's subsection and returns text"""
    sub_header_extra_lines = "".join(sub_section.splitlines()[:5])
    sub_header = sub_header_extra_lines.split("Authorisation procedure")[0]
    is_term = sub_header.find(keyword)

    if is_term != -1:
        recommendation = "Recommendation"
        recommendation_index = sub_section.index(recommendation)

        # gives text that contains page number eg- Page 4/10)
        page_num_regex = re.findall(r'Page \d+/\d+', sub_section)
        page_num = "".join(page_num_regex).split(
            " ")[1][0]  # gives precise page number eg -4
        table_data = extract_table_data(pdf_path, page_num)
        # print(table_data)

        return f"{sub_header} \n{table_data} \n{sub_section[recommendation_index:]}"
    else:
        return ""


def get_content(pdf_path, search_term):
    text = pdf_to_text(pdf_path)
    section_one, section_two, section_three = get_sections_text(pdf_path)

    section_one_result = ""
    for i in range(1, 10):
        if f'1.{i}' in section_one:

            start_index = section_one.index(f'1.{i}')
            try:
                end_index = section_one.index(f'1.{i+1}')
            except ValueError:
                header_two = "2. Recommendations for submission of supplementary"
                header_two_index = text.find(header_two)
                end_index = header_two_index

            sub_section = section_one[start_index:end_index]

            result = get_subsection_text(sub_section, search_term, pdf_path)
            section_one_result += result
    return section_one_result


def read_table(file, page_no):
    current_directory = os.path.abspath(os.curdir)
    pdf = current_directory + '/temp.pdf'

    urllib.request.urlretrieve(file, pdf)

    cv = Converter(pdf)
    # page_no = page_no - 1
    tables = cv.extract_tables(start=page_no-1)
    cv.close()
    # os.remove(pdf)
    # print(f'Total tables : {tables}')

    term = 'Ceftriaxone'

    for table in tables[0]:
        if term in table[0]:
            print(table)


if __name__ == '__main__':
    path = links['1']

    search_term = "Anakinra"
    # text = get_content(path, search_term)
    # print(text)

    # extract_table(path)

    # read table
    read_table(links['5'], page_no=4)
