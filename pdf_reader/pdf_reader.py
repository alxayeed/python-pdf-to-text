import textract
import urllib.request
import os


def text_tract(file_path):
    current_directory = os.path.abspath(os.curdir)
    pdf = current_directory + '/temp.pdf'

    urllib.request.urlretrieve(file_path, pdf)

    text = textract.process(pdf, encoding='utf-8')

    os.remove(pdf)
    return text


if __name__ == '__main__':
    file_path = 'https://www.bfarm.de/SharedDocs/Kundeninfos/EN/01/2021/21994-20_kundeninfo_en.pdf;jsessionid=D2C8EF2B0DE147C315FE08B2985EE04C.1_cid506?__blob=publicationFile&v=2'

    text = text_tract(file_path)
    print(text)
