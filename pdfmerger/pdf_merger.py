"""
pdf_merger
============

Merges Pdf files

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-07

Functions:
    merge_pdfs(pdf_paths, output): Pdf merger that doesnt use PdfMerger
    merge_pdfs_short(pdf_paths, output): Pdf merger with PdfMerger
"""

import sys
from PyPDF2 import PdfMerger
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

def merge_pdfs(pdf_paths, output):
    """
    Pdf merger that doesnt use PdfMerger

    Parameters:
    pdf_paths (str): paths of the odf files
    output (str): path of the outputfile

    Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
    1.0.0

    Date:
    2024-08-07
    """
    pdf_writer = PdfWriter()

    for path in pdf_paths:
        pdf_reader = PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])
    
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def merge_pdfs_short(pdf_paths, output):
    """
    Pdf merger that uses PdfMerger

    Parameters:
    pdf_paths (str): paths of the odf files
    output (str): path of the outputfile

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-07
    """
    merger = PdfMerger()
    for path in pdf_paths:
        merger.append(path)

    merger.write(output)
    merger.close()

if __name__ == '__main__':
    if len (sys.argv) < 4:
        print("Usage: python pdfmerger/pdf_merger.py input1.pdf input2.pdf ... output.pdf")
    elif len (sys.argv) >= 4:
        merge_pdfs_short(sys.argv[1:-1], output= sys.argv[-1])
    else:
        paths = ['pdfmerger/SE2_Teil1.pdf', 'pdfmerger/SE2_Teil2.pdf']
        merge_pdfs_short(paths, output='pdfmerger/merged.pdf')

# one line:
# python pdfmerger/pdf_merger.py pdfmerger/SE2_Teil1.pdf 
# pdfmerger/SE2_Teil2.pdf pdfmerger/SE2-AufgabenKomplett.pdf 
# pdfmerger/merged_console.pdf