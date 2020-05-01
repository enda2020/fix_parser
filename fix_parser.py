#!/usr/bin/env python3
import xml.etree.ElementTree as ET
from flask import Flask, render_template, request
from processing import parse_fix

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def adder_page():
    if request.method == "POST":
        fix_message = request.form["fix_message"]
        result = parse_fix(fix_message)
        html = "<table border=\"1\" cellpadding=\"3\"><tbody><tr><td><b>Number</b></td>  <td><b>Name</b></td>  <td><b>Type</b></td><td><b>Value</b></td></tr><tr>"
        for value in result.values():

          html += '<tr> <td>' + str(value['number']) + '</td>' + '<td>' + str(value['name']) + '</td>'+ '<td>'+ str(value['type']) + '</td>'+ '<td>'+ str(value['value']) + '</tr></td>'
        html += '</tbody></table>'
        print(html)
        return '''
                        <html>
                            <body>
                                {html}
                                <p><a href="/">Click here to calculate again</a>
                            </body>
                        </html>
                    '''.format(html=html)

    return '''
        <html>
            <body>
                <p>Enter your fix message</p>
                <form method="post" action=".">
                    <p><input name="fix_message" /></p>
                    <p><input type="submit" value="Parse!" /></p>
                </form>
            </body>
        </html>
    '''





if __name__ == "__main__":
    app.run(host='172.26.0.193', port=8000, debug=True)


