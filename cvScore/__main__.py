import re
from docx import Document
import pypdf
from pathlib import Path
import filetype
from cvScore.classes.ScoredDoc import ScoredDoc
import os
import argparse
import click
from . import commands


...


def get_file_type(filename):
    kind = filetype.guess(filename)
    if kind is None:
        raise TypeError('File type not supported.')
    return kind.mime


def load_keywords(filename):
    """
    Load keywords from a file.
    Each keyword should be on a separate line.
    """
    with open(filename, 'r') as file:
        keywords = [line.strip() for line in file]
    return keywords


def extract_text_from_pdf(pdf_path):
    text: str = ""
    with open(pdf_path, "rb") as f:
        reader = pypdf.PdfReader(f)
        info = reader.metadata
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


def extract_text_from_docx(docx_file):
    """
    Extract text from a Word document (.docx).
    """
    # Load the Word document
    doc = Document(docx_file)

    # Initialize an empty string to store the extracted text
    text = ''

    # Iterate over each paragraph in the document and extract the text
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'

    return text.strip()


def score_resume(resume_text, keywords):
    """
    Score a resume based on the frequency of keywords.
    """
    # Convert the resume text to lowercase for case-insensitive matching
    resume_text_lower = resume_text.lower()

    # Count the frequency of each keyword in the resume
    keyword_count = {keyword: len(re.findall(r'\b' + re.escape(keyword.lower()) + r'\b', resume_text_lower))
                     for keyword in keywords}

    # Calculate the total score based on the frequency of keywords
    total_score = sum(keyword_count.values())

    return total_score, keyword_count


def process_word_document(word_document, keywords):
    """
    Returns the frequency of the words in a Word document (.docx).
    """

    file = Path(word_document)

    total_score, keyword_count = score_resume(extract_text_from_docx(file), keywords)

    return total_score, keyword_count


def process_pdf_document(pdf_document, keywords):
    """
    Returns the frequency of the words in a Word document (.docx).
    """
    total_score, keyword_count = score_resume(extract_text_from_pdf(pdf_document), keywords)

    return total_score, keyword_count


def process_files(files, keywords_path):
    retVal = set()

    keywords = load_keywords(keywords_path)

    for file_path in files:
        kind = get_file_type(file_path)

        if kind == 'application/pdf':
            total_score, keyword_count = process_pdf_document(file_path, keywords)
        elif kind == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            total_score, keyword_count = process_word_document(file_path, keywords)
        else:
            raise TypeError(('File type not supported: {}'.format(kind)))
        score = ScoredDoc(fileName=file_path, score=total_score, keywordCount=keyword_count)
        retVal.add(score)

    return sorted(retVal, reverse=True)

