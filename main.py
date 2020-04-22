from ResumeBuilder import ResumeBuilder

FILE_TITLE = "resume.pdf"
DOC_TITLE = "Resume"
HEADER_POS = 20
LOC_POS = 400
LINE_END = 550


def generate_list(category):
    ret = []
    again = 'y'
    while again == 'y':
        skill = input("Enter a item/description in " + category + ": ")
        ret.append(skill)

        again = input("add another item? (y)es ")
    return ret


def main():
    # initialize pdf
    doc = ResumeBuilder(FILE_TITLE, DOC_TITLE)

    # draw ruler
    # draw_ruler(pdf)

    # name = input("enter first and last name ")
    # email = input("enter email ")
    # phone = input("enter phone ")
    # doc.intro(name, email, phone, HEADER_POS, y=770)
    #
    # # Skills
    # doc.section(name="Skills", x=HEADER_POS, y=675, line_start=80, line_end=LINE_END)
    #
    # # 15 apart for skills
    # word_len = []
    # for i in range(0, 4):
    #     category = input("Enter a skill category: ")
    #     word_len.append(len(category))
    #     doc.list_skill(category,
    #                    skill_values=generate_list(category),
    #                    x_left=40, x_right=max(word_len) + 120, y=650 - (15 * i))
    #
    # # Experience
    # doc.section(name="Experience", x=HEADER_POS, y=575, line_start=130, line_end=LINE_END)
    #
    # # jobs (75 apart from each job)
    # for i in range(3):
    #     company = input("Enter your company: ")
    #     job_title = input("Enter your job title for " + company + ": ")
    #     city = input("Enter the city you worked in: ")
    #     state = input("Enter the state you worked in: ")
    #     start = input("Enter start date: ")
    #     end = input("Enter end date or 'Present' if still working: ")
    #     location = city + ", " + state
    #     date = start + " - " + end
    #     doc.list_exp(company, job_title, location, date,
    #                  x_left=40, x_right=LOC_POS, y=550 - (75 * i),  # 75 apart
    #                  bullets=generate_list(company))
    #
    # # Projects
    # doc.section(name="Projects", x=HEADER_POS, y=325, line_start=100, line_end=LINE_END)
    # # 75 apart
    # for i in range(3):
    #     name = input("Enter project name: ")
    #     doc.list_project(name, x=40, y=300 - 75 * i, bullets=generate_list(name))

    # Education
    doc.section(name="Education", x=HEADER_POS, y=75, line_start=120, line_end=LINE_END)
    school = input("Enter institution: ")
    degree = input("Enter your degree: ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")
    start = input("Enter start date: ")
    end = input("Enter end date or 'Present' if still attending: ")
    location = city + ", " + state
    date = start + " - " + end
    doc.list_edu(school, degree, date, location,
                 x_left=40,
                 x_right=500,
                 y=50)
    # finalize
    doc.save()


main()
