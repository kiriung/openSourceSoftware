# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import json

from google.appengine.ext import ndb

import cgi
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def getSubject(input_subjectname):
    subject = ndb.Key('subjectname',input_subjectname)

    return subject

class MainPage(webapp2.RequestHandler):
    def get(self):

        template_value ={
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_value))

class View_selected(webapp2.RequestHandler):
    def post(self):

        #grade_option = self.request.get("control")

        self.response.write('<html><body> post response <pre>')
        input_string = self.request.get('input_subject')
        selected_Subject = getSubject(input_string)
        self.response.write(selected_Subject)
        self.response.write('</pre></body></html>')

class classlist(ndb.Model):

    subjectname = ndb.StringProperty(indexed=False)
    grade = ndb.StringProperty(indexed=False)
    time = ndb.StringProperty(indexed=False)
    classcode = ndb.StringProperty(indexed=False)
    classnum = ndb.StringProperty(indexed=False)
    ismajor = ndb.StringProperty(indexed=False)
    classcredit = ndb.StringProperty(indexed=False)
    professor = ndb.StringProperty(indexed=False)

class Student(ndb.Model):

    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    personallist = ndb.StringProperty(indexed=False)


class Greeting(ndb.Model):

    student = ndb.StructuredProperty(Student)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', View_selected),
], debug=True)
