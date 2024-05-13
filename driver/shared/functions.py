from langchain_community.document_loaders import PyPDFium2Loader
from .variables import DEFAULT_PDF_URL

def load_pdf_from_url(url=DEFAULT_PDF_URL):
    # Your code here
    loader = PyPDFium2Loader(url)
    return loader.load()


def load_pdf_from_file(file_path):
    # Create an instance of PyPDFium2Loader with the file path
    loader = PyPDFium2Loader(file_path)
    
    # Load the PDF document using the loader
    pdf_document = loader.load()
    
    # Return the loaded PDF document
    return pdf_document
