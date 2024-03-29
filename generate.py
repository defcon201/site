#!/usr/bin/env python3

# Based mostly on https://github.com/m-labs/web

import os
import sys
import re
import shutil

print("Working directory is" + os.getcwd())
print(os.path.dirname(os.path.realpath(__file__)))

if os.getcwd() != os.path.dirname(os.path.realpath(__file__)):
    print("error: This script is meant to be run from the repository root.")
    raise SystemExit()

from pages.docs.meetings import MeetingDetails

class PageMethods:
    def __init__(self, path):
        self.path = path

    def resource(self, resource):
        return os.path.relpath("output/base/" + resource, self.path)

    def header(self, title, menu_hl=None, nodiv=False, white_bg=False, description=None, titleimage=None, abspathroot=None):
        bodystyle = " style=\"background: #fff; color: #000;\"" if white_bg else ""

        # TODO: Get header, footer from ext. file like page content

        title = "DCG 201 | " + title if title else "DCG 201"
        description = description if description else "DCG 201 (formerly known as DEFCON 201) is a gathering point for folks interested in hacking."
        titleimage = titleimage if titleimage else "https://defcon201.org/res/img/dcg201.png"
        abspathroot = abspathroot if abspathroot else "https://defcon201.org"

        r = """<!DOCTYPE html>
<html lang="en">

    <head>

        <meta charset="utf-8"/>
        <title>""" + title + """</title>
        <meta http-equiv="onion-location" content="http://dc2oonezjanfurd34l6gi2nzqe6grh7cqhzqary2iluuzewyj77ufhyd.onion/" />
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:site" content="@defcon201nj">
        <meta name="twitter:creator" content="@sirocyl">
        <meta name="twitter:creator" content="@defcon201nj">
        <meta name="twitter:title" content=\"""" + title + """\">
        <meta name="twitter:description" content=\"""" + description + """\">
        <meta name="twitter:image" content=\"""" + titleimage + """\">
        <meta property="og:title" content=\"""" + title + """\" />
        <meta property="og:type" content="article" />
        <meta property="og:description" content=\"""" + description + """\">
        <meta ptoperty="og:image" content=\"""" + titleimage + """\">

        <link rel="stylesheet" type="text/css" media="screen" href=\"""" + self.resource("res/css/style.css") +  """\" />
        <link rel="stylesheet" href=\"""" + self.resource("res/font/dcg201-icons.css") +  """\" charset="utf-8">
        <link rel="stylesheet" href=\"""" + self.resource("res/font/voltaire-webfont/voltaire-webfont.css") +  """\" type="text/css" charset="utf-8">
        <link rel="stylesheet" href=\"""" + self.resource("res/font/overpass-webfont/overpass.css") +  """\" type="text/css" charset="utf-8">

    </head>

    <body""" + bodystyle + """>
        <div class="sidenav">

            <div id="header-logos">
                <a href=\"""" + abspathroot + """/\" class="linknoformat">
                    <div class="dc201-logo">
                        <h4 class="dc201-wordmark">DCG<span class="icon-201bell"></span>201</h4>
                    </div>
                </a>
                <div class="dc201-logo-subheader">
                    <span class="subheader-left-side"></span>
                    <h4>Jersey City &mdash; New Jersey</h4>
                    <span class="subheader-right-side"></span>
                </div>
            </div>
"""
        def list_open(root_list=False):
            nonlocal r
            r += "            "
            if root_list:
                r += '<ul class="sidelinks">'
            else:
                r += '    <ul class="sublinks">'
            r += "\n"

        def list_close(root_list=False):
            nonlocal r
            r += "            "
            if root_list:
                r += '</ul>'
            else:
                r += '    </ul>'
            r += "\n"

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
            r += "                    "
            r += "<li class=\"sublink\"><a"
            if title == "Mastodon":
                r += " rel=\"me\""
            r += " href=\""
            if ext_link:
                r += target
            else:
                r += self.resource(target)
            r += "\" class=\"sub\">&#x200a;" + title + "</a></li>\n"

        # TODO: generate sidebar nav link list from existing .page or .link (for ext/special link) files in directory

        list_open(True)
        item("meetings/meetings.html", "Meetings", "meetings")
        list_open()
        subitem("meetings/location.html", "About the location")
        subitem("meetings/events.html", "Special events")
        list_close()
        item("https://medium.com/@defcon201/", "News", "news", True)
        item("about/info.html", "Info", "info")
        list_open()
        subitem("about/info.html", "About DCG 201")
        subitem("about/coc.html", "Code of Conduct")
        subitem("about/constitution.html", "Constitution")
        subitem("about/partners.html", "Partners")
        subitem("about/contact.html", "Contact us")
        list_close()
        item("https://github.com/defcon201", "Projects", "projects", True)
        list_open()
        subitem("https://stats.foldingathome.org/team/241960", "Folding@Home", True)
        list_close()
        item("https://www.zazzle.com/defcon201", "Store", "Store", True)
        item(None, "Social", "social")
        list_open()
        subitem("https://www.meetup.com/DEFCON201/", "Meetup.com", True)
        subitem("https://www.facebook.com/groups/1743426829004414/", "Facebook", True)
        subitem("https://twitter.com/defcon201nj", "Twitter", True)
        subitem("https://instagram.com/defcon201", "Instagram", True)
        subitem("https://hostux.social/@defcon201", "Mastodon", True)
        subitem("https://github.com/defcon201", "GitHub", True)
        list_close()
        list_close(True)

        r += """
            <footer id="attrib">
                <div>
                    Text content: <a href="https://creativecommons.org/licenses/by/4.0">CC-BY 4.0</a><br>
                    Site code: <a href="https://twitter.com/sirocyl">sirocyl</a> &mdash; <a href="http://github.com/defcon201/site">Github</a><br>
                    DCG 201 Logo: sidepocket &amp; <a href="http://1dark1.com/">1dark1</a> &amp; <a href="https://twitter.com/sirocyl">sirocyl</a><br>
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
        # TODO: replace this with a switch-case to add more tag types (markdown parser? data retrieval/display methods?)
        if split and split[:11] == "{{{INCLUDE ":
            if split[:12] == "{{{INCLUDE /":
                includepath = os.path.join("./", split[12:-3])
            else:
                includepath = os.path.join(path_in, split[11:-3])

            print("Including contents from " + includepath)
            try:
                with open(includepath, "r") as includefile:
                    outdata += includefile.read()
            except FileNotFoundError:
                print("warning: File missing at \'" + includepath + "\' - check " + fullname + " for correctness.")
                pass

        else:
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


def is_submodule(name="docs"):
    print("generate: checking if " + name + " is a submodule")
    with open(".gitmodules", "r") as gitsmfile:
        if '[submodule \"'+ name +'\"]' in gitsmfile.read():
            print("generate: " + name + " is a submodule.")
            return True

def preserve_submodule(name="docs"):
    print("generate: preserving " + name + " submodule git")
    try:
        shutil.move(name + "/.git", ".generator-git-" + name)
    except FileNotFoundError:
        print("generate: preserve_submodule: error 66: no .git in " + name + ".", file=sys.stderr)
        print("(did you remember to do `git submodule update --init`?)")
        raise SystemExit(os.EX_NOINPUT) # it's rare when a GNU errno and a Python errno both work :)

def restore_submodule(name="docs"):
    print("generate: restoring " + name + " submodule git")
    try:
        shutil.move(".generator-git-" + name, name + "/.git")
    except FileNotFoundError:
        print("generate: restore_submodule: nothing to restore from .generator-git-" + name)
        pass


def generate_docs(name="docs"):
    if is_submodule(name):
        preserve_submodule(name)

    print("generate: clearing " + name + " folder")
    try:
        if name is not None and name != "":
            shutil.rmtree("./output/" + name + "/")
    except FileNotFoundError:
        print("generate: " + name + ": nothing to clear")
        pass

    print("generate: copying static resources")
    staticpath = "base" if name == "docs" else name
    outpath = "output/" + staticpath
    print("generate: staticpath is " + staticpath + " and outpath is " + outpath + ".")
    shutil.copytree("static/common", "./" + outpath + "/", dirs_exist_ok=True)
    shutil.copytree("static/" + staticpath + "/", "./" + outpath + "/", dirs_exist_ok=True)

    restore_submodule(name)

    print("generate: begin processing " + name + " pages")
    pagepath = "pages/docs" if name == "docs" else "pages/" + name + "-pages"
    print("generate: pagepath is " + pagepath)
    print("generate: processing " + name + " pages")
    for root, dirs, files in os.walk("./" + pagepath):
        for file in files:
            if file.endswith(".page"):
                process(root, "output/" + staticpath + "/" + os.path.relpath(root, pagepath + "/"), file, file[:-5] + ".html")

    print("generate: finished processing " + name + " pages.")
    print("page output is in " + name + "/")



def main():
    generate_docs("docs")

    generate_docs("tor")

    generate_docs("flyer")

    generate_docs("toolbox")

    generate_docs("txt")

if __name__ == "__main__":
    main()
