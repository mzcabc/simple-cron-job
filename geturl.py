#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
import datetime
 
from google.appengine.api import urlfetch
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
 
url = ""
 
class MainPage(webapp.RequestHandler):
    def get(self):
        result=urlfetch.fetch(url)
        if result.status_code==200:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write(datetime.datetime.now())
 
application = webapp.WSGIApplication([('/geturl', MainPage)],
                                     debug=True)
 
def main():
    run_wsgi_app(application)
 
if __name__ == "__main__":
    main()