#!/usr/bin/env python3

import os
import re


#
#'ssdf'



class PageMethods:
    def __init__(self, path):
        self.path = path

    def resource(self, resource):
        return os.path.relpath(resource, self.path)

    def header(self, title, menu_hl=None, nodiv=False, black_bg=False):
        bodystyle = " style=\"background: #000; color: #fff;\"" if black_bg else ""

        r = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>""" + title +  """ | M-Labs</title>
<link rel="stylesheet" type="text/css" media="screen" href=\"""" + self.resource("style.css") +  """\" />
<link rel="icon" type="image/png" href=\"""" + self.resource("favicon.png") + """\" />
</head>
<body""" + bodystyle + """>
<div class="sidenav">
  <img src=\"""" + self.resource("m_labs_logo_white.svg") + """\" width="200px">
"""
        def item(target, title, highlight):
            nonlocal r
            if menu_hl is not None and menu_hl == highlight:
                r += "<a href=\"" + self.resource(target) + "\" class=\"highlight\">&#8600; " + title + "</a>\n"
            else:
                r += "<a href=\"" + self.resource(target) + "\">&#8600; " + title + "</a>\n"

        def subitem(target, title):
            nonlocal r
            r += "<a href=\"" + self.resource(target) + "\" class=\"sub\">" + title + "</a>\n"
  
        item("artiq/index.html", "ARTIQ", "artiq")
        subitem("artiq/index.html", "Overview")
        subitem("artiq/sinara.html", "Sinara hardware")
        subitem("artiq/resources.html", "Resources")
        item("migen/index.html", "Migen", "migen")
        item("solvespace/index.html", "SolveSpace", "solvespace")
        item("about.html", "About", "about")
        subitem("about.html", "Company")
        subitem("office.html", "Office")
        r += """</div>
        """
        if not nodiv:
            r += "<div class=\"main\">"

        return r

    def footer(self, nodiv=False):
        d = "" if nodiv else "</div>\n"
        return d + """</body>
</html>
"""

    def get_globals(self):
        return {
            "header": self.header,
            "footer": self.footer,
            "resource": self.resource
        }


def process(path, name_in, name_out):
    fullname = os.path.join(path, name_in)
    print("processing", fullname)
    with open(fullname, "r") as infile:
        indata = infile.read()

    pm = PageMethods(path)
    outdata = ""
    # FIXME: this is just a buggy quick hack
    splits = re.split("({{{[^}]+}}})", indata)
    for split in splits:
        if split and split[:3] == "{{{":
            outdata += eval(split[3:-3], pm.get_globals())
        else:
            outdata += split

    with open(os.path.join(path, name_out), "w") as outfile:
        outfile.write(outdata)


def main():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".page"):
                process(root, file, file[:-5] + ".html")


if __name__ == "__main__":
    main()
