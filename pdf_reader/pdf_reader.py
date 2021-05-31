import textract
import urllib.request


def text_tract(file_path):
    text = textract.process(file_path)
    return text


if __name__ == '__main__':
    file_path = 'file/git.pdf'
    text = text_tract(file_path)
    print(text)
