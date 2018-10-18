#!/usr/bin/env python3

# Based mostly on https://github.com/m-labs/web

import os
import re

from meetings import MeetingDetails

class PageMethods:
    def __init__(self, path):
        self.path = path

    def resource(self, resource):
        return os.path.relpath(resource, self.path)

    def header(self, title, menu_hl=None, nodiv=False, white_bg=False):
        bodystyle = " style=\"background: #fff; color: #000;\"" if white_bg else ""

        # TODO: Get header, footer from ext. file like page content

        title = "DEFCON 201 | " + title if title else "DEFCON 201"

        r = """<!DOCTYPE html>
<html lang="en">

    <head>

        <meta charset="utf-8"/>
        <title>""" + title + """</title>
        <link rel="stylesheet" type="text/css" media="screen" href=\"""" + self.resource("style.css") +  """\" />
        <link rel="stylesheet" href=\"""" + self.resource("res/font/dc201stencam/dc201-stencil-camera.css") +  """\" charset="utf-8">
        <link rel="stylesheet" href=\"""" + self.resource("res/font/voltaire-webfont/voltaire-webfont.css") +  """\" type="text/css" charset="utf-8">
        <link rel="stylesheet" href=\"""" + self.resource("res/font/overpass-webfont/overpass.css") +  """\" type="text/css" charset="utf-8">

    </head>

    <body""" + bodystyle + """>
        <div class="sidenav">

            <div id="header-logos">
                <div class="dc201-logo">
                    <span class="image njbell-logo"><img class="njbell-logo-print" src=\"""" + self.resource("res/img/njbell.svg") +  """\"></span>
                    <h4 class="dc201-wordmark">DEFCON&hairsp;<span class="image jersey">&nbsp;</span>&hairsp;201</h4>
                </div>
                <div class="dc201-logo-subheader">
                    <span class="subheader-left-side"></span>
                    <h4>Jersey City&thinsp;<span class="image liberty"><span>&emsp;</span></span>&thinsp;New Jersey</h4>
                    <span class="subheader-right-side"></span>
                </div>
            </div>
            <ul class="sidelinks">
"""
        def item(target, title, highlight, ext_link=False, item_icon=None):
            nonlocal r
            r += "                "
            r += "<li class=\"sidelink\"><a"
            if target is not None:
                r += " href=\""
                if ext_link:
                    r += target
                else:
                    r += self.resource(target)
                r += "\""
                if menu_hl is not None and menu_hl == highlight:
                    r += " class=\"highlight\""
            r += ">" + title + "</a></li>\n"

        def subitem(target, title, ext_link=False, item_icon=None):
            nonlocal r
            r += "                "
            r += "<li class=\"sublink\"><a href=\""
            if ext_link:
                r += target
            else:
                r += self.resource(target)
            r += "\" class=\"sub\">" + title + "</a></li>\n"

        # TODO: generate sidebar nav link list from existing .page or .link (for ext/special link) files in directory

        item("meetings/meetings.html", "Meetings", "meetings")
        subitem("meetings/location.html", "About the location")
        subitem("meetings/previous.html", "Previous meetings")
        subitem("meetings/events.html", "Special events")
        item("https://medium.com/@defcon201/", "News", "news", True)
        item("about/info.html", "Info", "info")
        subitem("about/info.html", "About DEFCON 201")
        subitem("about/contact.html", "Contact us")
        item("projects.html", "Projects", "projects")
        item("partners.html", "Partners", "partners")
        item("https://www.zazzle.com/defcon201", "Store", "Store", True)
        item(None, "Social", "social")
        subitem("https://www.facebook.com/groups/1743426829004414/", "Facebook", True)
        subitem("https://twitter.com/defcon201nj", "Twitter", True)
        subitem("https://instagram.com/defcon201", "Instagram", True)
        subitem("https://hostux.social/@defcon201", "Mastodon", True)

        r += """
            </ul>
            <footer id="attrib">
                <div>
                    &copy; 2018 DEFCON 201.
                    Text content: CC-BY 4.0<br>
                    Site code: <a href="http://twitter.com/sirocyl">sirocyl</a> &mdash; <a href="http://github.com/defcon201/site">Github</a><br>
                </div>
            </footer>
        </div>
        """
        if not nodiv:
            r += "<div class=\"main\">"

        return r

    def footer(self, nodiv=False):
        d = " " if nodiv else "        </div>\n"
        return d + """
    </body>
</html>
"""

    def get_globals(self):
        return {
            "header": self.header,
            "footer": self.footer,
            "resource": self.resource,
            "MeetingDetails": MeetingDetails,
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
#    print(MeetingDetails.Date() + ": " + MeetingDetails.Title())
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".page"):
                process(root, file, file[:-5] + ".html")


if __name__ == "__main__":
    main()
