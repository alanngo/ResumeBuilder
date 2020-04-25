from tkinter import *
from ResumeBuilder import ResumeBuilder
from Paper import *
from Color import *

attr = ('Name', 'Email', 'Phone Number',
        'Skill0', 'Skill1', 'Skill2', 'Skill3',
        'Company0', 'Company1', 'Company2',
        'Job0', 'Job1', 'Job2')
FILE_TITLE = "sample_gui.pdf"
DOC_TITLE = "Sample"

JOB_TITLE = "CEO"
CITY = "San Francisco"
STATE = "California"
START = "December 2001"
END = "Present"
SCHOOL = "University of California at Berkley"
DEGREE = "Bachelor's Degree in Marketing"
PROJECT = "Flex Glue Clear"


def make_resume(entries):
    # initialize pdf
    doc = ResumeBuilder(FILE_TITLE, DOC_TITLE,
                        header_color=RED,
                        category_color=BLACK,
                        list_color=GREY)

    # hard code
    name = entries['Name'].get()
    email = entries['Email'].get()
    phone = entries['Phone Number'].get()

    doc.intro(name, email, phone, HEADER_POS, y=770)

    # Skills
    doc.section(name="Skills", x=HEADER_POS, y=675, line_start=80, line_end=LINE_END)
    skills = ["Lorem ipsum dolor sit amet", "Ut enim ad minim veniam", "Duis aute irure dolor in reprehenderit"]
    # 15 apart for skills
    dist = 150  # change to something not too far
    s0 = entries['Skill0'].get()
    s1 = entries['Skill1'].get()
    s2 = entries['Skill2'].get()
    s3 = entries['Skill3'].get()
    word_len = [len(s0), len(s1), len(s2), len(s3)]

    doc.list_skill(s0, skill_values=skills,
                   x_left=SUB_HEADER_POS, x_right=max(word_len) + dist, y=650 - (15 * 0))

    doc.list_skill(s1, skill_values=skills,
                   x_left=SUB_HEADER_POS, x_right=max(word_len) + dist, y=650 - (15 * 1))

    doc.list_skill(s2, skill_values=skills,
                   x_left=SUB_HEADER_POS, x_right=max(word_len) + dist, y=650 - (15 * 2))

    doc.list_skill(s3, skill_values=skills,
                   x_left=SUB_HEADER_POS, x_right=max(word_len) + dist, y=650 - (15 * 3))

    exp = ["Lorem ipsum dolor sit amet", "Ut enim ad minim veniam", "Duis aute irure dolor in reprehenderit"]
    # Experience
    doc.section(name="Experience", x=HEADER_POS, y=575, line_start=130, line_end=LINE_END)

    # jobs (75 apart from each job)
    c0 = entries['Company0'].get()
    j0 = entries['Job0'].get()
    city = CITY
    state = STATE
    start = START
    end = END
    location = city + ", " + state
    date = start + " - " + end
    doc.list_exp(c0, j0, location, date,
                 x_left=SUB_HEADER_POS, x_right=LOC_POS, y=LINE_END - (75 * 0),  # 75 apart
                 bullets=exp)

    c1 = entries['Company1'].get()
    j1 = entries['Job1'].get()
    city = CITY
    state = STATE
    start = START
    end = END
    location = city + ", " + state
    date = start + " - " + end
    doc.list_exp(c1, j1, location, date,
                 x_left=SUB_HEADER_POS, x_right=LOC_POS, y=LINE_END - (75 * 1),  # 75 apart
                 bullets=exp)

    c2 = entries['Company2'].get()
    j2 = entries['Job2'].get()
    city = CITY
    state = STATE
    start = START
    end = END
    location = city + ", " + state
    date = start + " - " + end
    doc.list_exp(c2, j2, location, date,
                 x_left=SUB_HEADER_POS, x_right=LOC_POS, y=LINE_END - (75 * 2),  # 75 apart
                 bullets=exp)

    proj = ["Lorem ipsum dolor sit amet", "Ut enim ad minim veniam", "Duis aute irure dolor in reprehenderit"]
    # Projects
    doc.section(name="Projects", x=HEADER_POS, y=325, line_start=100, line_end=LINE_END)
    # 75 apart
    for i in range(3):
        name = PROJECT
        doc.list_project(name, x=SUB_HEADER_POS, y=300 - 75 * i, bullets=proj)

    # Education
    doc.section(name="Education", x=HEADER_POS, y=75, line_start=120, line_end=LINE_END)
    school = SCHOOL
    degree = DEGREE
    city = CITY
    state = STATE
    start = START
    end = END
    location = city + ", " + state
    date = start + " - " + end
    doc.list_edu(school, degree, location, date,
                 x_left=SUB_HEADER_POS,
                 x_right=LOC_POS,
                 y=50)
    # finalize
    print("Resume Finished")
    doc.save()


def fetch(entries):
    print(entries)


def make_form(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field + ": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


def main():
    root = Tk()
    ents = make_form(root, attr)
    root.bind('<Return>', (lambda event, e=None: fetch(e)))
    submit = Button(root, text='Make Resume',
                    command=(lambda e=ents: make_resume(e)))
    submit.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()


main()
