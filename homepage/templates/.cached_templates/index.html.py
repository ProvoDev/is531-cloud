# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1478976599.2016742
_enable_loop = True
_template_filename = 'C:/Users/Brandon/OneDrive/Projects/is531-cloud/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html lang="en">\r\n  <head>\r\n    <meta charset="utf-8">\r\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1">\r\n    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->\r\n\r\n    <title>IS 531 Project 3</title>\r\n\r\n    <!-- Latest compiled and minified CSS -->\r\n\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\r\n\r\n\t<!-- Optional theme -->\r\n\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">\r\n\r\n\t<!-- Latest compiled and minified JavaScript -->\r\n\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\r\n   \r\n    <!-- Custom styles for this template -->\r\n    <link href="jumbotron.css" rel="stylesheet">\r\n  </head>\r\n\r\n  <body>\r\n\r\n    <nav class="navbar navbar-inverse navbar-fixed-top">\r\n      <div class="container">\r\n        <div class="navbar-header">\r\n          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">\r\n            <span class="sr-only">Toggle navigation</span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n            <span class="icon-bar"></span>\r\n          </button>\r\n          <a class="navbar-brand" href="index.html">Mr Robot Technology</a>\r\n        </div>\r\n        <div id="navbar" class="navbar-collapse collapse">\r\n          <form class="navbar-form navbar-right">\r\n            <div class="form-group">\r\n              <input type="text" placeholder="User ID" class="form-control">\r\n            </div>\r\n            <div class="form-group">\r\n              <input type="password" placeholder="Password" class="form-control">\r\n            </div>\r\n            <button type="submit" class="btn btn-success">Sign in</button>\r\n          </form>\r\n        </div><!--/.navbar-collapse -->\r\n      </div>\r\n    </nav>\r\n\r\n    <!-- Main jumbotron for a primary marketing message or call to action -->\r\n    <div class="jumbotron">\r\n      <div class="container">\r\n        <h1>Administrative Portal</h1>\r\n        <p>This website is only to be used according to authorized access for Mr Robot Technology\'s offial employees. Unauthorized access will be persecuted.</p>\r\n        <p>If you experience any issues, contact <a href="mailto:techsupport@MrRobotTech.com">techsupport@MrRobotTech.com</a></p>\r\n    \t<p>\r\n    \t\t<a class="btn btn-primary btn-lg" href="search.html" role="button">Search for Machine Details</a>\r\n        \t<a class="btn btn-primary btn-lg" href="create.html" role="button">Add New Machine Details</a>\r\n        \t<a class="btn btn-primary btn-lg" href="data.html" role="button">Manage Database</a>\r\n    \t</p>\r\n      </div>\r\n    </div>\r\n\r\n    <!-- jQuery (necessary for Bootstrap\'s JavaScript plugins) -->\r\n\t<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>\r\n\t<!-- Include all compiled plugins (below), or include individual files as needed -->\r\n\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/js/bootstrap.min.js" integrity="sha384-BLiI7JTZm+JWlgKa0M0kGRpJbF2J8q+qreVrKBC47e3K6BW78kGLrCkeRX6I9RoK" crossorigin="anonymous"></script>\r\n\t</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Brandon/OneDrive/Projects/is531-cloud/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}}
__M_END_METADATA
"""
