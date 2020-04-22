from ResumeBuilder import ResumeBuilder

HEADER_POS = 20
LOC_POS = 400
FILE_TITLE = "sample.pdf"
DOC_TITLE = "Resume"
NAME = "Phil Swift"
EMAIL = "phil_swift@flex_seal.com"
PHONE = "1234567890"
CATEGORY = "Category"
COMPANY = "Flex Seal"
JOB_TITLE = "CEO"
CITY = "San Francisco"
STATE = "California"
START = "December 2001"
END = "Present"
SCHOOL = "University of California at Berkley"
DEGREE = "Bachelor's Degree in Marketing"
PROJECT = "Flex Glue Clear"


def main():
    # initialize pdf
    doc = ResumeBuilder(FILE_TITLE, DOC_TITLE)

    # hard code
    name = NAME
    email = EMAIL
    phone = PHONE

    doc.intro(name, email, phone, HEADER_POS, y=770)

    # Skills
    doc.section(name="Skills", x=HEADER_POS, y=675, line_start=80, line_end=550)
    skills = ["Lorem ipsum dolor sit amet", "Ut enim ad minim veniam", "Duis aute irure dolor in reprehenderit"]
    # 15 apart for skills
    word_len = []
    for i in range(0, 4):
        category = CATEGORY
        word_len.append(len(category))
        doc.list_skill(category,
                       skill_values=skills,
                       x_left=40, x_right=max(word_len) + 120, y=650 - (15 * i))

    exp = ["Lorem ipsum dolor sit amet", "Ut enim ad minim veniam", "Duis aute irure dolor in reprehenderit"]
    # Experience
    doc.section(name="Experience", x=HEADER_POS, y=575, line_start=130, line_end=550)

    # jobs (75 apart from each job)
    for i in range(3):
        company = COMPANY
        job_title = JOB_TITLE
        city = CITY
        state = STATE
        start = START
        end = END
        location = city + ", " + state
        date = start + " - " + end
        doc.list_exp(company, job_title, location, date,
                     x_left=40, x_right=LOC_POS, y=550 - (75 * i),  # 75 apart
                     bullets=exp)

    proj = ["Lorem ipsum dolor sit amet", "Ut enim ad minim veniam", "Duis aute irure dolor in reprehenderit"]
    # Projects
    doc.section(name="Projects", x=HEADER_POS, y=325, line_start=100, line_end=550)
    # 75 apart
    for i in range(3):
        name = PROJECT
        doc.list_project(name, x=40, y=300 - 75 * i, bullets=proj)

    # Education
    doc.section(name="Education", x=HEADER_POS, y=75, line_start=120, line_end=550)
    school = SCHOOL
    degree = DEGREE
    city = CITY
    state = STATE
    start = START
    end = END
    location = city + ", " + state
    date = start + " - " + end
    doc.list_edu(school, degree, location, date,
                 x_left=40,
                 x_right=LOC_POS,
                 y=50)
    # finalize
    doc.save()


main()
