import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Course:
    def __init__(self, title, units, defaultQ, subject):
        self.title = title
        self.units = units
        self.defaultQ = defaultQ
        self.subject = subject

allCourses = []

CS106A = Course("CS106A", 5, "1A", "Engr")
allCourses.append(CS106A)
CS106B = Course("CS106B", 5, "1W", "Engr")
allCourses.append(CS106B)

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
