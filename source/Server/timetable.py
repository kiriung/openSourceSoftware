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
import webapp2
import cgi

MAIN_PAGE_HTML = """\

<HTML>

<HEAD>
    <META NAME="GENERATOR" Content="Microsoft Visual Studio" charset="utf-8">
    <TITLE></TITLE>

    <!--필요한 라이브러리의 역할을 링크를 통하여 웹에서 가져오도록 함-->
    <!--모든 기능이 필요한 것은 아니므로 min 정보로 가져온다-->
    <link href='https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.4.0/fullcalendar.min.css' rel='stylesheet' />
    <link href='https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.4.0/fullcalendar.print.css' rel='stylesheet' media='print' />
    <script src='https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.10.6/moment.min.js'></script>
    <!--<script src='https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.10.6/locale/ko.js'></script>-->

    <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js'></script>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.4.0/fullcalendar.min.js'></script>

    <script src='https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.4.0/lang/ko.js'></script>

    <link href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.5/css/bootstrap.min.css' rel='stylesheet' />
    <script src='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.5/js/bootstrap.min.js'></script>


    <style>
        .choiceSubject {
            width: 100%;
            height: 600px;
            border: 3px solid #747474;
            background: #A6A6A6;
        }
        .printTimeTable{
            width: 100%;
            height: 600px;
            /*border: 5px solid black;*/
        }
        .choiceSubject table {
            width: 100%;
        }

        .choiceSubject td {
            border-bottom: 2px solid black;
        }

    </style>
</HEAD>

<BODY>
    <div class="row" style="margin:20px">
        <div class="col-xs-4">
            <div class="choiceSubject">
                <table>
                    <tr>
                        <td align="center">
                            <input type="text" value="과목 검색" />
                            <button type="button" class="btn btn-default btn-sm" onclick="printSubject()"> 검색 </button>
                        </td>
                    </tr>
                    <tr>
                        <td align="center">
                            <input type="radio" name="grade" value="1" />1학년
                            <input type="radio" name="grade" value="2" />2학년
                            <input type="radio" name="grade" value="3" />3학년
                            <input type="radio" name="grade" value="4" />4학년
                        </td>
                    </tr>
                    <tr>
                        <td align="center">
                            학과별 과목
                            <select>
                                <option value="선택하세요.">선택하세요</option>

                            </select>
                            <br />
                        </td>
                    </tr>
                    <tr>
                        <td align="center">
                            교양분류별 과목
                            <select>
                                <option value="선택하세요.">선택하세요</option>
                                <option value="이산수학">영화듣기</option>
                            </select>
                            <br />
                        </td>
                    </tr>
                    <tr>
                        <td style="background:white;">

                        </td>
                    </tr>
                    <tr>
                        <td align="center">
                            <input type="button" value="시간표 만들기" onclick="makeTimeTable()" />
                    </tr>

                </table>
            </div>
        </div>
        <div class="col-xs-8">
            <div class="printTimeTable">
                <div id='calendar'>
                </div>
            </div>
        </div>
    </div>


     <script>
        function printSubject() {

        }

        function makeTimeTable() {

        }

        $(document).ready(function() {

            //코드가 data값이 있어야 정상적으로 작동을 하므로 아직 데이터가 없는 상황이어서 임의의 json형식의 데이터를 코드에 넣어줌
            //무의미 데이터
            var data = [
                {
                    title: 'All Day Event',
                    start: '2015-02-01'
                },
                {
                    title: 'Long Event',
                    start: '2015-02-07',
                    end: '2015-02-10'
                },
                {
                    id: 999,
                    title: 'Repeating Event',
                    start: '2015-02-09T16:00:00'
                }];

            // page is now ready, initialize the calendar...
            // 수정이 더 필요한 부분 날짜는 보여지지 않아도 됨
            $('#calendar').fullCalendar(
                {
                    header: {
                        left: '',
                        center: '',
                        right: ''
                    },
                    timeFormat: 'H시(:mm)',
                    columnFormat: 'ddd', //요일만 출력(시간표이기 때문에 날짜가 필요없음)
                    axisFormat: 'a h시',
                    allDaySlot: false,
                    defaultView: 'agendaWeek',
                    editable: false,
                    minTime:'08:00:00',
                    height: 'auto',
                    maxTime:'20:00:00',
                    lang:'ko',
                    businessHours: {
                        start: '00:00',
                        end: '24:00',
                        dow: [1,2,3,4,5]
                    };
                    events: data
                }
            )

        });
    </script>

</BODY>
</HTML>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class View_selected(webapp2.RequestHandler):
    def post(self):
        self.response.write('<html><body>You wrote:<pre>')
        self.response.write(cgi.escape(self.request.get('content')))
        self.response.write('</pre></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', View_selected),
], debug=True)
