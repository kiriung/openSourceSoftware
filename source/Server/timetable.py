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
import unittest

from google.appengine.ext import ndb
from google.appengine.api import users

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


class Student(ndb.Model):

    identity = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)
    personalclass = ndb.StringProperty(indexed=True)

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

class MainPage(webapp2.RequestHandler):
    def get(self):

        user = users.get_current_user()

        if user:
            template = JINJA_ENVIRONMENT.get_template('index.html')
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            template_value = {
                'url' : url,
                'url_linktext' : url_linktext

            }
            self.response.write(template.render(template_value))
            qry = Student.query(Student.email == user.email()).fetch()
            if qry:
                for elem in qry:
                    elem.key.delete()
            Student(identity = user.user_id(),email = user.email()).put()

        else:
            self.redirect(users.create_login_url(self.request.uri))
            #url = users.create_login_url(self.request.uri)
            #url_linktext = 'Login'


class View_searched(webapp2.RequestHandler):
    def post(self):

        input_string = self.request.get('input_textbox').encode('utf-8')
        searched_Subject = Classlist.query(Classlist.subjectname == input_string).fetch()
        searched_professr = Classlist.query(Classlist.professor == input_string).fetch()
        searched_code = Classlist.query(Classlist.classcredit == input_string).fetch()
        dict_selected_Subject = []
        for i in range(0,len(searched_Subject)):
            dict_selected_Subject.append(_todict(searched_Subject[i]))
        for i in range(0,len(searched_professr)):
            dict_selected_Subject.append(_todict(searched_professr[i]))
        for i in range(0,len(searched_code)):
            dict_selected_Subject.append((_todict(searched_code[i])))

        jsonlist = json.dumps(dict_selected_Subject,ensure_ascii=False)
        self.response.write(jsonlist)

class view_clicked(webapp2.RequestHandler):
    def post(self):
        ## 클린된 강의가 중간 col에 추가되는 동시에 로그인된 유저의 데이터베이스(personalclass)에 저장이 된다.
        user = users.get_current_user()
        pass

class View_selected(webapp2.RequestHandler):
    def get(self):

        template_value = {
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_value))

class View_timtable(webapp2.RequestHandler):
    def post(self):
        ## 시간표만들기를 눌렀을 때 유저의 데이터이스에 저장되어있던 personalclass를 전달한다.
        user = users.get_current_user()
        pass


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/selected', View_selected),
    ('/searched',View_searched)
], debug=True)
