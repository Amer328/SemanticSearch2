
# from PyPDF2 import PdfReader
import PyPDF2

def get_plain_text(pdf_filename):
    # Open the PDF file in read-binary mode
    with open(pdf_filename, 'rb') as f:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(f)
        # Get the number of pages in the PDF file
        num_pages =  len(pdf_reader.pages)
        # Initialize an empty string to store the text
        document_text = ''
        # Loop through each page in the PDF file
        for page_num in range(num_pages):
        # Get the current page
            page = pdf_reader.pages[page_num]
            #Extract the text from the current page
            page_text = page.extract_text()
            # Append the page text to the document text
            document_text += page_text
        return document_text


def split_text_into_chunks(plain_text, max_chars=2000):
    text_chunks = []
    current_chunk = ""
    for line in plain_text.split("\n"):
        if len(current_chunk) + len(line) + 1 <= max_chars:
            current_chunk += line + " "
        else:
            text_chunks.append(current_chunk.strip())
            current_chunk = line + " "
    if current_chunk:
        text_chunks.append(current_chunk.strip())
    return text_chunks



def scrape_text_from_pdf(pdf_file, max_chars=2000):
    plain_text = get_plain_text(pdf_file)
    text_chunks = split_text_into_chunks(plain_text, max_chars)
    return text_chunks