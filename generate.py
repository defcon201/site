#!/usr/bin/env python3

# Based mostly on https://github.com/m-labs/web

import os
import re
import shutil

from pages.meetings import MeetingDetails

class PageMethods:
    def __init__(self, path):
        self.path = path

    def resource(self, resource):
        return os.path.relpath("output/" + resource, self.path)

    def header(self, title, menu_hl=None, nodiv=False, white_bg=False):
        bodystyle = " style=\"background: #fff; color: #000;\"" if white_bg else ""

        # TODO: Get header, footer from ext. file like page content

        title = "DEFCON 201 | " + title if title else "DEFCON 201"

        r = """<!DOCTYPE html>
<html lang="en">

    <head>

        <meta charset="utf-8"/>
        <title>""" + title + """</title>
        <link rel="stylesheet" type="text/css" media="screen" href=\"""" + self.resource("res/css/style.css") +  """\" />
        <link rel="stylesheet" href=\"""" + self.resource("res/font/dc201stencam/dc201-stencil-camera.css") +  """\" charset="utf-8">
        <link rel="stylesheet" href=\"""" + self.resource("res/font/voltaire-webfont/voltaire-webfont.css") +  """\" type="text/css" charset="utf-8">
        <link rel="stylesheet" href=\"""" + self.resource("res/font/overpass-webfont/overpass.css") +  """\" type="text/css" charset="utf-8">

    </head>

    <body""" + bodystyle + """>
        <div class="sidenav">

            <div id="header-logos">
                <a href="https://defcon201.org/" class="linknoformat">
                    <div class="dc201-logo">
                        <span class="image njbell-logo"><img class="njbell-logo-print" src=\"""" + self.resource("res/img/njbell.svg") +  """\"></span>
                        <h4 class="dc201-wordmark">DEFCON&#x200a;<span class="image jersey">&nbsp;</span>&#x200a;201</h4>
                    </div>
                </a>
                <div class="dc201-logo-subheader">
                    <span class="subheader-left-side"></span>
                    <h4>Jersey City&#x2009;<span class="image liberty"><span>&#x2003;</span></span>&#x2009;New Jersey</h4>
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
            r += "\" class=\"sub\">&#x200a;" + title + "</a></li>\n"

        # TODO: generate sidebar nav link list from existing .page or .link (for ext/special link) files in directory

        item("meetings/meetings.html", "Meetings", "meetings")
        subitem("meetings/location.html", "About the location")
        subitem("meetings/events.html", "Special events")
        item("https://medium.com/@defcon201/", "News", "news", True)
        item("about/info.html", "Info", "info")
        subitem("about/info.html", "About DEFCON 201")
        subitem("about/partners.html", "Partners")
        subitem("about/contact.html", "Contact us")
        item("https://github.com/defcon201", "Projects", "projects", True)
        item("https://www.zazzle.com/defcon201", "Store", "Store", True)
        item(None, "Social", "social")
        subitem("https://www.meetup.com/DEFCON201/", "Meetup.com", True)
        subitem("https://www.facebook.com/groups/1743426829004414/", "Facebook", True)
        subitem("https://twitter.com/defcon201nj", "Twitter", True)
        subitem("https://instagram.com/defcon201", "Instagram", True)
        subitem("https://hostux.social/@defcon201", "Mastodon", True)

        r += """
            </ul>
            <footer id="attrib">
                <div>
                    Text content: <a href="https://creativecommons.org/licenses/by/4.0">CC-BY 4.0</a><br>
                    Site code: <a href="https://twitter.com/sirocyl">sirocyl</a> &mdash; <a href="http://github.com/defcon201/site">Github</a><br>
                    DEFCON201 Logo: <a href="https://twitter.com/tekcopedis">sidepocket</a> &amp; <a href="http://1dark1.com/">1dark1</a> &amp; <a href="https://twitter.com/sirocyl">sirocyl</a><br>
                    <br>
                    Questions, changes or comments about the website? <a href="https://github.com/defcon201/site/issues">See the issue tracker.</a><br>
                    <br>
                    <span style="font-family: Voltaire-webfont;"><span class="image jersey" style="">&emsp;</span> Proudly made in New Jersey.</span>
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


def process(path_in, path_out, name_in, name_out):
    fullname = os.path.join(path_in, name_in)
    print("process: processing", str(fullname))
    with open(fullname, "r") as infile:
        indata = infile.read()

    pm = PageMethods(path_out)
    outdata = ""

    # FIXME: this is just a buggy quick hack
    splits = re.split("({{{[^}]+}}})", indata)
    for split in splits:
        if split and split[:3] == "{{{":
            outdata += eval(split[3:-3], pm.get_globals())
        else:
            outdata += split

    try:
        os.makedirs(path_out)
    except FileExistsError:
        pass

    with open(os.path.join(path_out, name_out), "w") as outfile:
        outfile.write(outdata)


def main():
    print("generate: clearing output")
    try:
        shutil.rmtree("output/")
    except FileNotFoundError:
        print("generate: nothing to clear")
        pass
    print("generate: copying static resources")
    shutil.copytree("res/", "output/res/")

    for root, dirs, files in os.walk("./pages"):
        for file in files:
            if file.endswith(".page"):
                process(root, "output/" + os.path.relpath(root, "pages/"), file, file[:-5] + ".html")

if __name__ == "__main__":
    main()
