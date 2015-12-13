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

import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



class Classlist(ndb.Model):
    subjectname = ndb.StringProperty(indexed=True)
    grade = ndb.StringProperty(indexed=True)
    time = ndb.StringProperty(indexed=True)
    classcode = ndb.StringProperty(indexed=True)
    classnum = ndb.StringProperty(indexed=True)
    ismajor = ndb.StringProperty(indexed=True)
    classcredit = ndb.StringProperty(indexed=True)
    professor = ndb.StringProperty(indexed=True)

def _todict(_Classlist):
    dict_obj = {
        'subjectname': _Classlist.subjectname,
        'grade': _Classlist.grade,
        'time': _Classlist.time,
        'classcode': _Classlist.classcode,
        'classnum': _Classlist.classnum,
        'ismajor': _Classlist.ismajor,
        'classcredit': _Classlist.classcredit,
        'professor': _Classlist.professor
    }

    return dict_obj




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

class Loaddata(webapp2.RequestHandler):
    def get(self):
        qry = Classlist.query().fetch()
        for elem in qry:
            self.response.write(json.dumps(_todict(elem)))


class MainPage(webapp2.RequestHandler):
    def get(self):

        template_value = {
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_value))





class View_searched(webapp2.RequestHandler):
    def post(self):

        input_string = self.request.get('input_textbox').encode('utf-8')
        searched_Subject = Classlist.query(Classlist.subjectname == input_string or Classlist.professor == input_string or Classlist.classcredit == input_string ).fetch()
        dict_selected_Subject = []
        for i in range(0,len(searched_Subject)):
            dict_selected_Subject.append(_todict(searched_Subject[i]))
        jsonlist = json.dumps(dict_selected_Subject,ensure_ascii=False)
        self.response.write(jsonlist)

class View_selected(webapp2.RequestHandler):
    def get(self):

        template_value = {
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_value))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/selected', View_selected),
    ('/searched',View_searched),
    ('/load',Loaddata)
], debug=True)
