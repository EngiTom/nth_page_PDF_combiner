from PyPDF2 import PdfFileReader, PdfFileWriter
import os
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen.canvas import Canvas

def make(pdfname, ind, lookfor, matchnum): 
    # ind: 0-index page index
    # lookfor: required string in original filename
    # pdfname: name of produced pdf file
    pdf_writer = PdfFileWriter()
    
    # pdf cover page
    canvas = Canvas("x.pdf", pagesize=LETTER) # x.pdf is a buffer file
    canvas.setFont("Helvetica", 30)
    if ind == 6: # team round
        canvas.drawString(72, LETTER[1]/2, "Math Team Match {} Team Round".format(matchnum))
    else:
        canvas.drawString(72, LETTER[1]/2, "Math Team Match {} Round {}".format(matchnum, ind+1))
    canvas.save()
    cover = PdfFileReader('x.pdf').getPage(0)
    pdf_writer.add_page(cover)

    # find pages and add to pdfwriter
    for i, fname in enumerate(os.listdir()):
        if lookfor in fname:
            pdf = PdfFileReader(fname)
            pagewanted = pdf.getPage(ind)
            if i == 1:
                pagewanted.scaleBy(0.24) # the 2016 pdf is larger than the rest
            pdf_writer.addPage(pagewanted)
    
    #write pages
    output = f'{pdfname}.pdf'
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)


# Call functions for all round numbers
if __name__ == '__main__':
    for i in range(7):
        make('m1r{}'.format(i+1), i, "Match1", "1") # run make function