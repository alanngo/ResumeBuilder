from tkinter import *
from Paper import *
from Color import *
from ResumeBuilder import ResumeBuilder

attr = ('Name', 'Email', 'Phone Number',
        'Skill0', 'Skill1', 'Skill2', 'Skill3',
        'Company0', 'Job0', 'City0', 'State0', 'Start0', 'End0',
        'Company1', 'Job1', 'City1', 'State1', 'Start1', 'End1',
        'Company2', 'Job2', 'City2', 'State2', 'Start2', 'End2',
        'Project0', 'Project1', 'Project2',
        'School', 'Degree', 'Start', 'End', 'City', 'State')
FILE_TITLE = "sample_gui.pdf"
DOC_TITLE = "Sample"

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

    skill_list = [entries['Skill0'].get(), entries['Skill1'].get(), entries['Skill2'].get(), entries['Skill3'].get()]
    word_len = [len(skill_list[0]), len(skill_list[1]), len(skill_list[2]), len(skill_list[3])]
    i = 0
    for skill in skill_list:
        doc.list_skill(skill, skill_values=skills,
                       x_left=SUB_HEADER_POS, x_right=max(word_len) + dist, y=650 - (15 * i))
        i += 1

    exp = ["Lorem ipsum dolor sit amet", "Ut enim ad minim veniam", "Duis aute irure dolor in reprehenderit"]
    # Experience
    doc.section(name="Experience", x=HEADER_POS, y=575, line_start=130, line_end=LINE_END)

    companies = [entries['Company0'].get(), entries['Company1'].get(), entries['Company2'].get()]
    jobs = [entries['Job0'].get(), entries['Job1'].get(), entries['Job2'].get()]
    cities = [entries['City0'].get(), entries['City1'].get(), entries['City2'].get()]
    states = [entries['State0'].get(), entries['State1'].get(), entries['State2'].get()]
    start = [entries['Start0'].get(), entries['Start1'].get(), entries['Start2'].get()]
    end = [entries['End0'].get(), entries['End1'].get(), entries['End2'].get()]

    # jobs (75 apart from each job)
    for i in range(0, 3):
        location = cities[i] + ", " + states[i]
        date = start[i] + " - " + end[i]
        doc.list_exp(companies[i], jobs[i], location, date,
                     x_left=SUB_HEADER_POS, x_right=LOC_POS, y=LINE_END - (75 * i),  # 75 apart
                     bullets=exp)

    proj = ["Lorem ipsum dolor sit amet", "Ut enim ad minim veniam", "Duis aute irure dolor in reprehenderit"]
    # Projects
    doc.section(name="Projects", x=HEADER_POS, y=325, line_start=100, line_end=LINE_END)
    projects = [entries['Project0'].get(), entries['Project1'].get(), entries['Project2'].get()]
    # 75 apart
    for i in range(3):
        name = projects[i]
        doc.list_project(name, x=SUB_HEADER_POS, y=300 - 75 * i, bullets=proj)

    # Education
    doc.section(name="Education", x=HEADER_POS, y=75, line_start=120, line_end=LINE_END)
    school = entries['School'].get()
    degree = entries['Degree'].get()
    city = entries['City'].get()
    state = entries['State'].get()
    start = entries['Start'].get()
    end = entries['End'].get()
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
        ent.insert(0, "Lorem ipsum ")
        row.pack(side=TOP, fill=X, padx=5, pady=4)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, expand=NO, fill=X)
        entries[field] = ent
    return entries


def main():
    root = Tk()
    ents = make_form(root, attr)
    root.bind('<Return>', (lambda event, e=None: fetch(e)))
    submit = Button(root, text='Make Resume',
                    command=(lambda e=ents: make_resume(e)))
    submit.pack(side=RIGHT, padx=5, pady=5)
    root.mainloop()


main()
