from reportlab.pdfgen import canvas

FILE_TITLE = "resume.pdf"
DOC_TITLE = "Resume"
NAME = "Squidward Tentacles"
EMAIL = "squiddy_ten@bikinibottom.org"
PHONE = "(123) 456-7890"


def draw_ruler(pdf):
    for x in range(0, 6):
        pdf.drawString(x * 100, 0, "x" + str(x * 100))
    for y in range(0, 9):
        pdf.drawString(0, y * 100, "y" + str(y * 100))


def main():
    # initialize pdf
    pdf = canvas.Canvas(FILE_TITLE)
    pdf.setTitle(DOC_TITLE)

    # draw ruler
    draw_ruler(pdf)

    # draw name
    pdf.setFont("Times-Bold", 36)
    pdf.setFillColorRGB(0, 0, 255)
    pdf.drawString(20, 770, NAME)

    # draw credentials
    pdf.setFont("Times-Roman", 12)
    pdf.setFillColorRGB(0, 0, 0)
    pdf.drawString(20, 750, EMAIL)
    pdf.drawString(20, 735, PHONE)

    # Skills
    pdf.setFont("Times-Roman", 24)
    pdf.drawString(20, 675, "Skills")
    pdf.line(80, 675, 550, 675)

    # Experience
    pdf.setFont("Times-Roman", 24)
    pdf.drawString(20, 575, "Experience")
    pdf.line(130, 575, 550, 575)

    pdf.setFont("Times-Roman", 14)
    pdf.drawString(40, 550, "Company 0")

    pdf.setFont("Times-Italic", 12)
    pdf.drawString(500, 550, "Location")

    # Projects
    pdf.setFont("Times-Roman", 24)
    pdf.drawString(20, 475, "Projects")
    pdf.line(100, 475, 550, 475)

    # finalize
    pdf.save()

    for font in pdf.getAvailableFonts():
        print(font)


main()
