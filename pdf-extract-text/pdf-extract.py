from langchain_text_splitters import CharacterTextSplitter
import pdfplumber

def get_pdf_text(pdf_files):
    text = ""
    for pdf_file in pdf_files:
        with pdfplumber.open(pdf_file) as reader:
            i = 0
            for page in reader.pages:
                i += 1
                text += page.extract_text()
    return text

def get_chunk_text(text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks

text = get_pdf_text(["1.pdf"])
text = get_chunk_text(text)
print(text)
