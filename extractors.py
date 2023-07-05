# file (right now, PDF-focused) extractors
from pdfminer.high_level import extract_text
import textract
import tiktokenizer
import PyPDF2
import re
import os
import general

def pdfminer_extract_text(pdf_path):
    """Extract text from a PDF file using PDFMiner."""
    return extract_text(pdf_path)

