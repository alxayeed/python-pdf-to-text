import PyPDF2
from input_output import links
import urllib.request
import os


def get_pdf_reader_obj(pdf_file):
    # creating a pdf file object
    pdf_file_obj = open(pdf_file, 'rb')
    # creating a PdfFileReader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    return pdf_reader, pdf_file_obj


def extract_text_from_pdf(pdf_file):
    pdf_reader, pdf_file_obj = get_pdf_reader_obj(pdf_file)
    # prints number of pages
    print(pdf_reader.numPages)
    # extract text of a specific page
    page_obj = pdf_reader.getPage(14)
    text = page_obj.extractText()
    print(text)
    # closing pdf file object
    pdf_file_obj.close()


def rotate_pdf(original_pdf, rotated_pdf_name, rotation):
    pdf_reader, pdf_file_obj = get_pdf_reader_obj(original_pdf)

    # creating pdf writer object
    pdf_writer = PyPDF2.PdfFileWriter()

    # rotate all pages
    for page in range(pdf_reader.numPages):
        # creating rotated page object
        page_obj = pdf_reader.getPage(page)
        page_obj.rotateClockwise(rotation)

        # adding rotated page to pdf writer
        pdf_writer.addPage(page_obj)

    # new pdf file obj
    new_file = open(rotated_pdf_name, 'wb')
    pdf_writer.write(new_file)

    new_file.close()
    pdf_file_obj.close()


def merge_pdf(pdf_list, output_file):
    pdf_merger_obj = PyPDF2.PdfFileMerger()

    # appending pdfs one by one
    for pdf in pdf_list:
        pdf_merger_obj.append(pdf)

    # writing merged into a new file
    with open(output_file, 'wb') as f:
        pdf_merger_obj.write(f)


def split_pdf():
    pass


def add_watermark():
    pass


if __name__ == '__main__':
    file_path = 'file/prac.pdf'
    # extract_text_from_pdf(file_path)

    # rotate
    # new_file = 'file/rotated_prac.pdf'
    # rotate_pdf(file_path, new_file, 180)

    # merge
    pdf_list = ['file/table.pdf', 'file/tb1.pdf']
    output = 'file/merged_pdf.pdf'

    # merge_pdf(pdf_list, output)
