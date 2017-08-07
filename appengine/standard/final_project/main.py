from google.appengine.ext import ndb
from google.appengine.api import memcache

import os
import jinja2
import json
import webapp2

JINJA_ENV = jinja2.Environment(
 loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class User(ndb.Model):
    username = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    email = ndb.StringProperty()



class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write('Hello, Almost Done. Final Project. Yay!')
        template = JINJA_ENV.get_template('index.html')
        # controller tells to render the index.html template
        self.response.out.write(template.render())

class Users(webapp2.RequestHandler):
    def get(self):
        # get all users
        get_user_query_results = [get_user_query.to_dict()
                                      for get_user_query in User.query()]
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(json.dumps(get_user_query_results))  # display results to user

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/users', Users)
], debug=True)
