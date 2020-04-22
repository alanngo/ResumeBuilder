from reportlab.pdfgen import canvas
from Fonts import *


class ResumeBuilder:
    def __init__(self, file_title, doc_title):
        self.pdf = canvas.Canvas(file_title)
        self.pdf.setTitle(doc_title)

    def draw_ruler(self):
        for x in range(0, 6):
            self.pdf.drawString(x * 100, 0, "x" + str(x * 100))
        for y in range(0, 9):
            self.pdf.drawString(0, y * 100, "y" + str(y * 100))

    def intro(self, name, email, phone, x, y):
        # draw name
        self.pdf.setFont(BOLD, 36)
        self.pdf.setFillColorRGB(0, 0, 255)
        self.pdf.drawString(x, y, name)

        # draw credentials
        self.pdf.setFont(NORMAL, 12)
        self.pdf.setFillColorRGB(0, 0, 0)
        self.pdf.drawString(x, y - 20, email)
        area_code = phone[0:3]
        three_digits = phone[3:6]
        four_digits = phone[6:10]
        phone_number = str("("+area_code+")"+" "+three_digits+"-"+four_digits)
        self.pdf.drawString(x, y - 35, phone_number)

    def section(self, name, x, y, line_start, line_end):
        self.pdf.setFillColorRGB(0, 0, 255)
        self.pdf.setFont(NORMAL, 24)
        self.pdf.drawString(x, y, name)
        self.pdf.line(line_start, y, line_end, y)
        self.pdf.setFillColorRGB(0, 0, 0)

    def list_skill(self, skill, skill_values, x_left, x_right, y):
        self.pdf.setFont(NORMAL, 12)
        self.pdf.drawString(x_left, y, skill)
        self.pdf.setFont(SKILL_VALUE, 8)

        values = ""
        cnt = 0
        for s in skill_values:
            if cnt == len(skill_values) - 1:
                values += str(s)
                break
            else:
                values += str(s + ", ")
                cnt += 1

        self.pdf.drawString(x_right, y, values)

    def list_exp(self, company, job_title, location, date, x_left, x_right, y, bullets):
        self.pdf.setFont(NORMAL, 14)
        self.pdf.drawString(x_left, y, company)
        self.pdf.setFont(NORMAL, 12)
        self.pdf.drawString(x_left, y - 15, job_title)  # y-15 apart from Company n
        self.pdf.setFont(ITALIC, 12)
        self.pdf.drawString(x_right, y, location)
        self.pdf.setFont(ITALIC, 10)
        self.pdf.drawString(x_right, y - 15, date)  # y-15 apart from Location
        self.pdf.setFont(NORMAL, 10)

        spacing = 30
        # y-10 apart
        for b in bullets:
            self.pdf.drawString(x_left, y - spacing, " - " + b)  # y-30 apart from Company n
            spacing += 10

    def list_project(self, name, x, y, bullets):
        self.pdf.setFont(NORMAL, 14)
        self.pdf.drawString(x, y, name)
        self.pdf.setFont(NORMAL, 10)

        spacing = 15
        # y-10 apart
        for b in bullets:
            self.pdf.drawString(x, y - spacing, "- " + b)  # y-30 apart from Company n
            spacing += 10

    def list_edu(self, school, degree, location, date, x_left, x_right, y):
        self.pdf.setFont(NORMAL, 14)
        self.pdf.drawString(x_left, y, school)

        self.pdf.setFont(NORMAL, 12)
        self.pdf.drawString(x_left, y - 15, degree)

        self.pdf.setFont(ITALIC, 12)
        self.pdf.drawString(x_right, y, location)

        self.pdf.setFont(ITALIC, 10)
        self.pdf.drawString(x_right, y - 15, date)  # y-15 apart from Location

    def save(self):
        self.pdf.save()
