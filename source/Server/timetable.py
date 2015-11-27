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

MAIN_PAGE_HTML = """\
<HTML>
<HEAD>
    <META NAME="GENERATOR" Content="Microsoft Visual Studio" charset = "utf-8">
    <TITLE></TITLE>
    <style>
        .choiceSubject {
            width: 400px;
            height: 600px;
            border: 5px solid #747474;
            background: #A6A6A6;
            margin-left: 300px;
            top: 30px;
            position:fixed;
        }
        .printTimeTable{
            width: 400px;
            height: 600px;
            border: 5px solid black;
            margin-left: 750px;
            top:30px;
            position:fixed;
        }
        table {
            width: 400px;
        }

        td {
            border-bottom: 2px solid black;
        }

    </style>
</HEAD>
<script>
    function printSubject() {

    }

    function makeTimeTable() {

    }
</script>
<BODY>
    <div class="choiceSubject">
        <table>
            <tr>
                <td align="center">
                    <form>
                        <input type="text" value="과목 검색" />
                        <input type="button" onclick="printSubject()" />
                    </form>
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
    <div class="printTimeTable">

    </div>
</BODY>
</HTML>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
