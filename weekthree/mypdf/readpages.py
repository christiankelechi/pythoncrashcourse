from PyPDF2 import PdfFileReader,PdfFileWriter
from pathlib import Path
from reportlab.pdfgen.canvas import Canvas


pdfpath=Path('D:\\codeblazebackendcourse\\weekthree\\mypdf\\django4byexample.pdf')
# readme=PdfFileReader(str(pdfpath))
# print(readme.getPage(27).extractText())
# A programe that generates a receipt after completing a form
canvas=Canvas("paymentreceipttwo.pdf")
name=input("What is your name\n ")
age=input("How old are you? \n")

amount=input("Amount Paid\n")

canvas.drawString(72,720,"Hello Welcome to Codeblaze")
canvas.drawString(72,680,"Name :"+name)
canvas.drawString(72,640,"age :"+age)
canvas.drawString(72,600,"Amound Paid :"+amount)
canvas.setFont('Arial',50)
canvas.save()