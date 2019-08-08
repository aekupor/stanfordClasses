import jinja2
import webapp2
import os

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Course:
    def __init__(self, title, units, defaultQ):
        self.title = title
        self.units = units
        self.defaultQ = defaultQ

CS106A = Course("CS106A", 5, "1A")
CS106B = Course("CS106B", 5, "1W")

class Home(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            
        }
        template = jinja_env.get_template('templates/index.html')
        self.response.write(template.render(template_vars))

app=webapp2.WSGIApplication([
    ('/', Home),
], debug=True)
