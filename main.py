import jinja2
import webapp2
import os

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Home(webapp2.RequestHandler):
    def get(self):
        welcome = "hello"
        template_vars = {
            "welcome": welcome,
        }
        template = jinja_env.get_template('templates/index.html')
        self.response.write(template.render(template_vars))

app=webapp2.WSGIApplication([
    ('/', Home),
], debug=True)
