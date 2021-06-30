import PyPDF2
from input_output import links


def extract_text_from_pdf(pdf_file):
    # creating a pdf file object
    pdf_file_obj = open(pdf_file, 'rb')
    # creating a PdfFileReader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    # prints number of pages
    print(pdf_reader.numPages)
    # extract text of a specific page
    page_obj = pdf_reader.getPage(14)
    text = page_obj.extractText()
    print(text)
    # closing pdf file object
    pdf_file_obj.close()


if __name__ == '__main__':
    file_path = 'file/prac.pdf'
    extract_text_from_pdf(file_path)
