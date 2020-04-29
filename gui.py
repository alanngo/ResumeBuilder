from tkinter import *
from Paper import *
from Color import *
from Fields import *
from ResumeBuilder import ResumeBuilder

FILE_TITLE = "sample_gui.pdf"
DOC_TITLE = "Sample"


def create_file(file_name, text):
    file = open(file_name, 'w')
    file.write(text)
    file.close()


def read_file(file_name):
    file = open(file_name, 'r')
    ret = []
    for text in file:
        ret.append(text.rstrip('\n'))
    file.close()
    return ret


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
    skill_values = [read_file("skills0.txt"),
                    read_file("skills1.txt"),
                    read_file("skills2.txt"),
                    read_file("skills3.txt")]

    # 15 apart for skills
    dist = 150  # change to something not too far

    skill_list = [entries['Skillset0'].get(),
                  entries['Skillset1'].get(),
                  entries['Skillset2'].get(),
                  entries['Skillset3'].get()]
    word_len = [len(skill_list[0]), len(skill_list[1]), len(skill_list[2]), len(skill_list[3])]
    i = 0
    for skill in skill_list:
        doc.list_skill(skill, skill_values[i],
                       x_left=SUB_HEADER_POS, x_right=max(word_len) + dist, y=650 - (15 * i))
        i += 1

    exp = [read_file("job0.txt"),
           read_file("job1.txt"),
           read_file("job2.txt")]
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
                     bullets=exp[i])

    proj = [read_file("project0.txt"),
            read_file("project1.txt"),
            read_file("project2.txt")]
    # Projects
    doc.section(name="Projects", x=HEADER_POS, y=325, line_start=100, line_end=LINE_END)
    projects = [entries['Project0'].get(), entries['Project1'].get(), entries['Project2'].get()]
    # 75 apart
    for i in range(3):
        name = projects[i]
        doc.list_project(name, x=SUB_HEADER_POS, y=300 - 75 * i, bullets=proj[i])

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

        row.pack(side=TOP, fill=X, padx=5, pady=1)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, expand=NO, fill=X)

        entries[field] = ent
    return entries


def main():
    # creating dummy files to list skills, project, and job details
    for i in range(0, 4):
        create_file("skills" + str(i)+".txt", "blah" + str(i))

    for i in range(0, 3):
        create_file("job" + str(i)+".txt", "work" + str(i))
        create_file("project" + str(i)+".txt", "project" + str(i))

    root = Tk()
    ents = make_form(root, attr)
    root.bind('<Return>', (lambda event, e=None: fetch(e)))
    submit = Button(root, text='Make Resume', command=(lambda e=ents: make_resume(e)))
    submit.pack(side=BOTTOM, padx=5, pady=5)
    root.mainloop()


main()
