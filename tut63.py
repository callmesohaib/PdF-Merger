from pypdf import PdfWriter
import os
merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]   #store all PDF files in Files variable

for pdf in files:
    merger.append(pdf)
merger.write("merged-pdf.pdf") #file name
merger.close()
