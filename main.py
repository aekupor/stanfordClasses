import webapp2
import jinja2
import os
import json

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Course:
    # add quarters offered, description, pre-reqs
    def __init__(self, title, units, defaultQ, subject, description, prereqs):
        self.title = title
        self.units = units
        self.defaultQ = defaultQ
        self.subject = subject
        self.description = description
        self.prereqs = prereqs

allCourses = []

CS106A = Course("CS106A", 5, "1A", "Engr", "intro to programming", "none")
allCourses.append(CS106A)
think = Course("Think", 5, "1A", "Other", "required class", "none")
allCourses.append(think)
CS106B = Course("CS106B", 5, "1W", "Engr", "intro to programming part 2", "CS106A")
allCourses.append(CS106B)
CS107 = Course("CS107", 5, "1S", "Engr", "intro to programming part 3", "CS106A CS106B")
allCourses.append(CS107)

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
