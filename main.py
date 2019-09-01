import webapp2
import jinja2
import os
import json

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Course:
    def __init__(self, title, units, defaultQ, subject, description, prereqs, needed):
        self.title = title
        self.units = units
        self.defaultQ = defaultQ
        self.subject = subject
        self.description = description
        self.prereqs = prereqs
        self.needed = needed

allCourses = []

CS106A = Course("CS106A", 5, "1A", "Engr", "Introduction to the engineering of computer applications emphasizing modern software engineering principles", "none", "CS106B CS107 ENGR40M")
allCourses.append(CS106A)
Think = Course("Think", 4, "1A", "Other", "Helps ask rigorous and genuine questions that can lead to scientific experimentation, literary interpretation, or social policy analysis", "none", "none")
allCourses.append(Think)
PWR1 = Course("PWR1", 4, "1A", "Other", "Engages students in the serious practice of academic analysis, college level research, and argument", "none", "none")
allCourses.append(PWR1)
CS106B = Course("CS106B", 5, "1W", "Engr", "Abstraction and its relation to programming. Software engineering principles of data abstraction and modularity", "CS106A", "CS107 CS221 CS109")
allCourses.append(CS106B)
CS107 = Course("CS107", 5, "2A", "Engr", "Introduction to the fundamental concepts of computer systems. Explores how computer systems execute programs and manipulate data, working from the C programming language down to the microprocessor", "CS106B", "CS221 CS143 CS110 CS145")
allCourses.append(CS107)
MATH19 = Course("MATH19", 5, "1A", "MaSc", "Introduction to differential calculus of functions of one variable", "none", "MATH20 MATH21")
allCourses.append(MATH19)
MATH20 = Course("MATH20", 5, "1W", "MaSc", "The definite integral, Riemann sums, antiderivatives, the Fundamental Theorem of Calculus, and the Mean Value Theorem for integrals", "MATH19", "MATH21")
allCourses.append(MATH20)
MATH21 = Course("MATH21", 5, "1S", "MaSc", "Sequences, functions, limits at infinity, and comparison of growth of functions", "MATH19 MATH20", "none")
allCourses.append(MATH21)
WAYS1 = Course("WAYS", 3, "1W", "Other", "Emphasizes synthesis and integration: individual Ways as not seen as separate, but part of an overall intellectual profile and set of complementary capacities", "none", "none")
allCourses.append(WAYS1)
WAYS2 = Course("WAYS", 3, "1W", "Other", "Emphasizes synthesis and integration: individual Ways as not seen as separate, but part of an overall intellectual profile and set of complementary capacities", "none", "none")
allCourses.append(WAYS2)
WAYS3 = Course("WAYS", 3, "1S", "Other", "Emphasizes synthesis and integration: individual Ways as not seen as separate, but part of an overall intellectual profile and set of complementary capacities", "none", "none")
allCourses.append(WAYS3)
WAYS4 = Course("WAYS", 3, "1S", "Other", "Emphasizes synthesis and integration: individual Ways as not seen as separate, but part of an overall intellectual profile and set of complementary capacities", "none", "none")
allCourses.append(WAYS4)
WAYS5 = Course("WAYS", 3, "2W", "Other", "Emphasizes synthesis and integration: individual Ways as not seen as separate, but part of an overall intellectual profile and set of complementary capacities", "none", "none")
allCourses.append(WAYS5)
WAYS6 = Course("WAYS", 3, "2W", "Other", "Emphasizes synthesis and integration: individual Ways as not seen as separate, but part of an overall intellectual profile and set of complementary capacities", "none", "none")
allCourses.append(WAYS6)
IntroSem = Course("IntroSem", 3, "1S", "Other", "Offer small-group courses taught by esteemed faculty to frosh and sophomores", "none", "none")
allCourses.append(IntroSem)
CS103 = Course("CS103", 5, "2A", "Engr", "Serves as an introduction to discrete mathematics, computability theory, and complexity theory", "CS106B", "CS109 CS145 CS161 CS154 CS143 CS221")
allCourses.append(CS103)
PWR2 = Course("PWR2", 4, "2A", "Other", "Engages students in the serious practice of academic analysis, college level research, and argument", "none", "none")
allCourses.append(PWR2)
Lang1 = Course("Lang1", 5, "2A", "Other", "Language study extends your range of knowledge and expression significantly, providing access to materials and cultures that otherwise would be out of reach", "none", "Lang2 Lang3")
allCourses.append(Lang1)
Lang2 = Course("Lang2", 5, "2W", "Other", "Language study extends your range of knowledge and expression significantly, providing access to materials and cultures that otherwise would be out of reach", "Lang1", "Lang3")
allCourses.append(Lang2)
Lang3 = Course("Lang3", 5, "2S", "Other", "Language study extends your range of knowledge and expression significantly, providing access to materials and cultures that otherwise would be out of reach", "Lang1 Lang2", "none")
allCourses.append(Lang3)
CS110 = Course("CS110", 5, "2S", "Engr", "Principles and practice of engineering of computer software and hardware systems", "CS107", "CS144 CS194")
allCourses.append(CS110)
CS109 = Course("CS109", 5, "2S", "Engr", "Introduction to Probability for Computer Scientists", "CS103 CS106B MATH51", "CS161 CS221")
allCourses.append(CS109)
MATH51 = Course("MATH51", 5, "2W", "MaSc", "Linear Algebra, Multivariable Calculus, and Modern Applications", "MATH21", "CS109")
allCourses.append(MATH51)
CS154 = Course("CS154", 5, "3A", "Engr", "Introduction to Automata and Complexity Theory", "CS103", "none")
allCourses.append(CS154)
CS145 = Course("CS145", 5, "3A", "Engr", "Introduction to the use, design, and implementation of database and data-intensive systems, including data models", "CS103 CS107", "none")
allCourses.append(CS145)
PHYS21 = Course("PHYS21", 4, "3A", "MaSc", "Mechanics, Fluids, and Heat", "none", "PHYS23")
allCourses.append(PHYS21)
PHYS23 = Course("PHYS23", 4, "3W", "MaSc", "Electricity, Magnetism, and Optics", "PHYS21", "none")
allCourses.append(PHYS23)
CS161 = Course("CS161", 5, "3W", "Engr", "Design and Analysis of Algorithms", "CS103 CS109", "CS194")
allCourses.append(CS161)
Math = Course("Math El.", 5, "3W", "MaSc", "Math Elective", "none", "none")
allCourses.append(Math)
QAbroad = Course("Q Abroad", 5, "3S", "Other", "Quarter abroad class", "none", "none")
allCourses.append(QAbroad)
allCourses.append(QAbroad)
allCourses.append(QAbroad)
CS144 = Course("CS144", 5, "4A", "Engr", "Introduction to Computer Networking", "CS110", "none")
allCourses.append(CS144)
CS221 = Course("CS221", 5, "4A", "Engr", "Artificial Intelligence: Principles and Techniques", "CS103 CS106B CS107 CS109", "none")
allCourses.append(CS221)
WAYS7 = Course("WAYS", 3, "4A", "Other", "Emphasizes synthesis and integration: individual Ways as not seen as separate, but part of an overall intellectual profile and set of complementary capacities", "none", "none")
allCourses.append(WAYS7)
SciEl = Course("Sci El.", 4, "4A", "MaSc", "Science Elective", "none", "none")
allCourses.append(SciEl)
WAYS8 = Course("WAYS", 3, "4W", "Other", "Emphasizes synthesis and integration: individual Ways as not seen as separate, but part of an overall intellectual profile and set of complementary capacities", "none", "none")
allCourses.append(WAYS8)
ENGR40M = Course("ENGR40M", 5, "4W", "Engr", "An Intro to Making: What is EE", "CS106A", "none")
allCourses.append(ENGR40M)
CSEl = Course("CS El.", 5, "4W", "Engr", "CS Elective", "none", "none")
allCourses.append(CSEl)
FundEl = Course("Fund El.", 5, "4W", "Engr", "Fundamental Elective", "none", "none")
allCourses.append(FundEl)
CSEl1 = Course("CS El.", 5, "4S", "Engr", "CS Elective", "none", "none")
allCourses.append(CSEl1)
CS194 = Course("CS194", 5, "4S", "Engr", "Design, specification, coding, and testing of a significant team programming project under faculty supervision", "CS110 CS161", "none")
allCourses.append(CS194)
CS143 = Course("CS143", 5, "4S", "Engr", "Principles and practices for design and implementation of compilers and interpreters", "CS103 CS107", "none")
allCourses.append(CS143)
CS181W = Course("CS181W", 5, "4S", "Other", "Writing-intensive version of CS181. Satisfies the WIM requirement for Computer Science, Engineering Physics, STS, and Math/Comp Sci undergraduates", "none", "none")
allCourses.append(CS181W)


class Home(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            "allCourses": allCourses,
        }
        template = jinja_env.get_template('templates/index.html')
        self.response.write(template.render(template_vars))

app=webapp2.WSGIApplication([
    ('/', Home),
], debug=True)
