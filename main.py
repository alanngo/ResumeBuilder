from ResumeBuilder import ResumeBuilder

FILE_TITLE = "resume.pdf"
DOC_TITLE = "Resume"
NAME = "Phil Swift"
EMAIL = "squiddy_ten@bikinibottom.org"
PHONE = "(123) 456-7890"


def main():
    # initialize pdf
    doc = ResumeBuilder(FILE_TITLE, DOC_TITLE)

    # draw ruler
    # draw_ruler(pdf)

    doc.intro(name=NAME, email=EMAIL, phone=PHONE, x=20, y=770)

    skills = ("skill0", "skill1", "skill2")
    # Skills
    doc.section(name="Skills", x=20, y=675, line_start=80, line_end=550)

    # 15 apart for skills
    for i in range(0, 4):
        doc.list_skill(skill="Skill", skill_values=skills, x_left=40, x_right=70, y=650 - (15 * i))

    # Experience
    doc.section(name="Experience", x=20, y=575, line_start=130, line_end=550)

    # jobs (75 apart from each job)
    points = ["b0", "b1", "b2"]
    for i in range(3):
        doc.list_exp(company="company",
                     job_title="job title",
                     location="Location",
                     date="date",
                     x_left=40, x_right=500, y=550 - (75 * i),  # 75 apart
                     bullets=points)

    # Projects
    proj = ["b0", "b1", "b2"]
    doc.section(name="Projects", x=20, y=325, line_start=100, line_end=550)
    # 75 apart
    for i in range(3):
        doc.list_project(name="proj", x=40, y=300 - 75 * i, bullets=proj)

    # Education
    doc.section(name="Education", x=20, y=75, line_start=120, line_end=550)
    doc.list_edu(school="Bikini Bottom University",
                 degree="BA Music",
                 date="date",
                 location="Location",
                 x_left=40,
                 x_right=500,
                 y=50)
    # finalize
    doc.save()


main()
