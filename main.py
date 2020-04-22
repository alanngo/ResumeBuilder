from reportlab.pdfgen import canvas
from Fonts import *

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


def intro(pdf, name, email, phone, x, y):
    # draw name
    pdf.setFont(BOLD, 36)
    pdf.setFillColorRGB(0, 0, 255)
    pdf.drawString(x, y, name)

    # draw credentials
    pdf.setFont(NORMAL, 12)
    pdf.setFillColorRGB(0, 0, 0)
    pdf.drawString(x, y - 20, email)
    pdf.drawString(x, y - 35, phone)


def section(pdf, name, x, y, line_start, line_end):
    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont(NORMAL, 24)
    pdf.drawString(x, y, name)
    pdf.line(line_start, y, line_end, y)
    pdf.setFillColorRGB(0, 0, 0)


def list_skill(pdf, skill, skill_values, x_left, x_right, y):
    pdf.setFont(NORMAL, 12)
    pdf.drawString(x_left, y, skill)
    pdf.setFont(SKILL_VALUE, 8)

    values = ""
    cnt = 0
    for s in skill_values:
        if cnt == len(skill_values) - 1:
            values += str(s)
            break
        else:
            values += str(s + ", ")
            cnt += 1

    pdf.drawString(x_right, y, values)


def list_exp(pdf, company, job_title, location, date, x_left, x_right, y, bullets):
    pdf.setFont(NORMAL, 14)
    pdf.drawString(x_left, y, company)
    pdf.setFont(NORMAL, 12)
    pdf.drawString(x_left, y - 15, job_title)  # y-15 apart from Company n
    pdf.setFont(ITALIC, 12)
    pdf.drawString(x_right, y, location)
    pdf.setFont(ITALIC, 10)
    pdf.drawString(500, y - 15, date)  # y-15 apart from Location
    pdf.setFont(NORMAL, 10)

    spacing = 30
    # y-10 apart
    for b in bullets:
        pdf.drawString(x_left, y - spacing, "- " + b)  # y-30 apart from Company n
        spacing += 10


def list_project(pdf, name, x, y, bullets):
    pdf.setFont(NORMAL, 14)
    pdf.drawString(x, y, name)
    pdf.setFont(NORMAL, 10)

    spacing = 15
    # y-10 apart
    for b in bullets:
        pdf.drawString(x, y - spacing, "- " + b)  # y-30 apart from Company n
        spacing += 10


def list_edu(pdf, school, degree, location, date, x_left, x_right, y):
    pdf.setFont(NORMAL, 14)
    pdf.drawString(x_left, y, school)
    pdf.setFont(NORMAL, 12)
    pdf.drawString(x_left, y - 15, degree)
    pdf.setFont(ITALIC, 12)
    pdf.drawString(x_right, y, location)
    pdf.setFont(ITALIC, 10)
    pdf.drawString(500, y - 15, date)  # y-15 apart from Location


def main():
    # initialize pdf
    pdf = canvas.Canvas(FILE_TITLE)
    pdf.setTitle(DOC_TITLE)

    # draw ruler
    draw_ruler(pdf)

    intro(pdf, name=NAME, email=EMAIL, phone=PHONE, x=20, y=770)

    skills = ("skill0", "skill1", "skill2")
    # Skills
    section(pdf, name="Skills", x=20, y=675, line_start=80, line_end=550)

    # 15 apart for skills
    for i in range(0, 4):
        list_skill(pdf, skill="Skill", skill_values=skills, x_left=40, x_right=70, y=650 - (15 * i))

    # Experience
    section(pdf, name="Experience", x=20, y=575, line_start=130, line_end=550)

    # jobs (75 apart from each job)
    points = ["b0", "b1", "b2"]
    for i in range(3):
        list_exp(pdf, company="company",
                 job_title="job title",
                 location="Location",
                 date="date",
                 x_left=40, x_right=500, y=550 - (75 * i),  # 75 apart
                 bullets=points)

    # Projects
    proj = ["b0", "b1", "b2"]
    section(pdf, name="Projects", x=20, y=325, line_start=100, line_end=550)
    # 75 apart
    for i in range(3):
        list_project(pdf, name="proj", x=40, y=300 - 75 * i, bullets=proj)

    # Education
    section(pdf, name="Education", x=20, y=75, line_start=120, line_end=550)
    list_edu(pdf,
             school="Bikini Bottom University",
             degree="BA Music",
             date="date",
             location="Location",
             x_left=40,
             x_right=500,
             y=50)
    # finalize
    pdf.save()

    for font in pdf.getAvailableFonts():
        print(font)


main()
