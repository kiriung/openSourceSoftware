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



class Classlist(ndb.Model):
    subjectname = ndb.StringProperty(indexed=True)
    grade = ndb.StringProperty(indexed=True)
    time = ndb.StringProperty(indexed=False)
    classcode = ndb.StringProperty(indexed=True)
    classnum = ndb.StringProperty(indexed=False)
    ismajor = ndb.StringProperty(indexed=False)
    classcredit = ndb.StringProperty(indexed=False)
    professor = ndb.StringProperty(indexed=True)


class Student(ndb.Model):

    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    personalclass = ndb.StringProperty(indexed=False)


class Greeting(ndb.Model):

    student = ndb.StructuredProperty(Student)



def getSubject(input):

    search_name = Classlist.query(Classlist.subjectname == input)   #Classlist에 원소가 없는것 처럼 보임
    search_professor = Classlist.query(Classlist.professor == input)
    search_code = Classlist.query(Classlist.classcode == input)

    return search_name.fetch()


class MainPage(webapp2.RequestHandler):
    def get(self):

        input_grade = self.request.get('selected_grade')
        grade_qry = Classlist.query(Classlist.grade == input_grade).fetch()
        template_value = {
            'Classlist': grade_qry,

        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_value))

class View_selected(webapp2.RequestHandler):
    def post(self):

        #grade_option = self.request.get("control")

        self.response.write('<html><body> post response <pre>')
        input_string = self.request.get('input_textbox')
        self.response.write('searching data with ')
        self.response.write(input_string+'</br>')
        selected_Subject = getSubject(input_string)
        for i in range(0,len(selected_Subject)):
            self.response.write(selected_Subject[i].subjectname +'</br>')
        self.response.write('</pre></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', View_selected),
    ('/select',MainPage)
], debug=True)
