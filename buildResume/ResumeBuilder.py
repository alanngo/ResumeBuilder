from reportlab.pdfgen import canvas
from buildResume.Fonts import *
from buildResume.Color import set_color


class ResumeBuilder:

    def __init__(self,
     header_color, 
     category_color, 
     list_color, 
     file_title="sampleRes.pdf", 
     doc_title ="Sample",):
        self.pdf = canvas.Canvas(file_title)
        self.pdf.setTitle(doc_title)
        self.header_color = header_color
        self.category_color = category_color
        self.list_color = list_color

    def draw_ruler(self):
        for x in range(0, 6):
            self.pdf.drawString(x * 100, 0, "x" + str(x * 100))
        for y in range(0, 9):
            self.pdf.drawString(0, y * 100, "y" + str(y * 100))

    def intro(self, name, email, phone, x, y):
        # draw name
        set_color(self.pdf, self.header_color)
        set_font(self.pdf, BOLD, 36)
        self.pdf.drawString(x, y, name)

        # draw credentials
        set_font(self.pdf, NORMAL, 12)
        set_color(self.pdf, self.category_color)
        self.pdf.drawString(x, y - 20, email)
        area_code = phone[0:3]
        three_digits = phone[3:6]
        four_digits = phone[6:10]
        phone_number = str("(" + area_code + ")" + " " + three_digits + "-" + four_digits)
        self.pdf.drawString(x, y - 35, phone_number)

    def section(self, name, x, y, line_start, line_end):
        set_color(self.pdf, self.header_color)
        set_font(self.pdf, NORMAL, 24)
        self.pdf.drawString(x, y, name)
        self.pdf.line(line_start, y, line_end, y)
        set_color(self.pdf, self.category_color)

    def list_skill(self, skill, skill_values, x_left, x_right, y):

        # skill category
        set_font(self.pdf, NORMAL, 12)
        self.pdf.drawString(x_left, y, skill)
        set_font(self.pdf, LIST_VAL, 8)

        # category values
        values = ""
        cnt = 0
        for s in skill_values:
            if cnt == len(skill_values) - 1:
                values += str(s)
                break
            else:
                values += str(s + ", ")
                cnt += 1
        set_color(self.pdf, self.list_color)
        self.pdf.drawString(x_right, y, values)
        set_color(self.pdf, self.category_color)

    def list_exp(self, company, job_title, location, date, x_left, x_right, y, bullets):

        # company
        set_font(self.pdf, NORMAL, 14)
        self.pdf.drawString(x_left, y, company)

        # job title
        set_font(self.pdf, NORMAL, 10)
        self.pdf.drawString(x_left, y - 10, job_title)  # y-10 apart from Company n

        # location
        set_color(self.pdf, self.header_color)
        set_font(self.pdf, ITALIC, 12)
        self.pdf.drawString(x_right, y, location)

        # date
        set_color(self.pdf, self.category_color)
        set_font(self.pdf, ITALIC, 10)
        self.pdf.drawString(x_right, y - 15, date)  # y-15 apart from Location

        # bullets
        spacing = 20
        set_font(self.pdf, LIST_VAL, 8)
        set_color(self.pdf, self.list_color)
        for b in bullets:  # y-10 apart
            self.pdf.drawString(x_left, y - spacing, " - " + b)  # y-30 apart from Company n
            spacing += 10
        set_color(self.pdf, self.category_color)

    def list_project(self, name, x, y, bullets):
        set_font(self.pdf, NORMAL, 14)
        self.pdf.drawString(x, y, name)
        set_font(self.pdf, NORMAL, 10)

        spacing = 15
        set_font(self.pdf, LIST_VAL, 8)
        set_color(self.pdf, self.list_color)
        for b in bullets:  # y-10 apart
            self.pdf.drawString(x, y - spacing, "- " + b)  # y-30 apart from Company n
            spacing += 10
        set_color(self.pdf, self.category_color)

    def list_edu(self, school, degree, location, date, x_left, x_right, y):
        set_font(self.pdf, NORMAL, 14)
        self.pdf.drawString(x_left, y, school)

        set_font(self.pdf, NORMAL, 12)
        self.pdf.drawString(x_left, y - 15, degree)

        set_color(self.pdf, self.header_color)
        set_font(self.pdf, ITALIC, 12)
        self.pdf.drawString(x_right, y, location)
        set_color(self.pdf, self.category_color)

        set_font(self.pdf, ITALIC, 10)
        self.pdf.drawString(x_right, y - 15, date)  # y-15 apart from Location

    def save(self):
        self.pdf.save()
