#!/usr/bin/env python3

class MeetingDetails:           # Any of these can be HTML formatted, but I'd recommend against it for semantics sake EXCEPT where triple quotes (""" like this """) appear.
    def Date():                 # Date of the meeting (Weekday, Month DD)
        return "Friday, May 21st"
    def Title():                # Title of the meeting
        return "Virtual Light"
    def Location():             # Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "Online &mdash; Streaming &amp; on NOWHERE VR"
    def Notice():               # Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():        # A link that refers to this meeting
        return "https://defcon201.medium.com/dcg-201-online-meet-up-may-2021-virtual-light-d858732751d0"
    def LinkName():             # What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "post on our Medium"
    def Summary():              # Short, 1-2 sentences about this meeting.
        return """
Join us for a special, entirely Virtual Reality online meet up broadcasted out of the DCG 201 LIVE Streams,
 where we look at VR’s past mistakes, security, privacy, development and how it can be used for both good and evil.
"""


        # Default summary is:
        """<b>More information about this month's meeting is coming soon.</b><br>
        Meeting details are usually confirmed one week in advance of the scheduled meeting date."""


    def Schedule():
        schedstruct = [
            'starttime',	# The scheduled begin time (for example "6:00 PM") or None if no scheduled time (will put "Ending at [time]" if endtime isn't None)
            'endtime',		# The scheduled end time (same format) or None if no scheduled time (will put "Starting at [time]" if starttime isn't None)
            'eventtype',	# The type of event (example choices are: "Intro", "Talk", "Workshop", "Project", "Wrap-Up", "<em>TBA</em>", "Unofficial Ad-Hoc Hours" or something flavorful, or None)
            'title',		# The title of the event in the schedule, or None.
            'speaker',		# The speaker or the subject of the event.
            """summary"""]      # A long-form summary of the event.

        schedtable = []
        schedlist = []

        '''
    Copy the following template to add a new event, filling in the spaces where necessary.

        schedlist.append([
            '12:00AM',
            '12:00AM',
            'Event Type',
            'Event Title',
            'Event Speaker or Subject',
            """This is a summary of the event in question.
            It can span multiple lines"""
            ])

    The following line adds a spacer to the schedule box:
        schedlist.append([None, None, None, None, None, None])

    To add a bold-faced general announcement to the schedule, use this template before the first entry:
        schedlist.append([None, None, None, "Announcement here", None, None])

    To add a notice after a schedule item, use this template after the entry you wish to add a notice to:
        schedlist.append([None, None, None, None, "Notice here", None])

    To add a footnote after the end of the schedule, use this template after the last entry:
        schedlist.append([None, None, None, None, None,
                          """Footnotes and other important information appear here."""])

        '''

        schedlist.append([None, None, None, "DCG 201 is streaming online.", None, "Live Streams are available at:"])
        schedlist.append([None, None, None, None, "Twitch",  '<a href="https://www.twitch.tv/defcon201live">https://www.twitch.tv/defcon201live</a><br>'])
        schedlist.append([None, None, None, None, "dLive",   '<a href="https://dlive.tv/defcon201">https://dlive.tv/defcon201</a><br>'])
        schedlist.append([None, None, None, None, "YouTube", '<a href="https://www.youtube.com/c/defcon201">https://www.youtube.com/c/defcon201</a><br>'])
        schedlist.append([None, None, None, None, "NOWHERE VR", '<em>Link coming soon.</em><br>'])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([
            '5:00PM',
            'Link will be posted',
            'VR Lounge',
            'NOWHERE Virtual Reality Hacker Hangout',
            'DCG 201',
            """
Come meet us in the Virtual World of NOWHERE, a new social and events platform that revolutionizes online gathering by offering face-to-face interaction
in beautifully designed three-dimensional spaces! Hang out, talk on your mic, turn on video to show off your hacker shit and watch the LIVE Stream through
the virtual world followed by an after party featuring amazing music!
            """
            ])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([
            '5:30PM',
            '5:55PM',
            'Pre-show',
            'Beyond the Looking Glass (1993)',
            '<a href="http://www.jaronlanier.com/">Jaron Lanier</a>',
            """
A great time capsule on what VR technology was like in the early 1990’s and what their hopes were for the future of the technology.
            """
            ])

        schedlist.append([
            '6:00PM',
            '7:00PM',
            'Talk',
            'XRSI: The Reality Of Securing Virtual Worlds',
            '<a href="https://twitter.com/KavyaPearlman">Kayva Pearlman</a>',
            """
Kavya Pearlman, founder of XR Safety Initiative is busy building processes, standards and finding novel cyberattacks
to stay ahead of the bad guys that are coming for this rising new domain of Virtual Reality.
            """
            ])

        schedlist.append([
            '7:00PM',
            '7:30PM',
            'Talk',
            'LÖVR: What’s happening in the world of one Open Source VR Library',
            '<a href="https://twitter.com/mcclure111">Andi McClure</a>',
            """
LÖVR is a cross-platform, open-source VR engine created by Bjorn Swenson, an alternative to Unreal or Unity that lets you create a VR game or app in just a few lines of Lua.
We’ll have Andi McClure by to talk about VR development in general, give a demo of LÖVR, and show off her LÖVR-based commercial game “SKATEGIRL DESTROYS THE UNIVERSE”.
            """
            ])

        schedlist.append([
            '7:30PM',
            '8:00PM',
            'Workshop',
            'Alloverse: Free & Open Source Virtual Reality',
            'Nevyn Bengtsson',
            """
Continuing from the LÖVR talk, we will air a video presentation by Nevyn Bengtsson showing off his project Alloverse, a LÖVR-based metaverse.
Come watch if you’re curious about LÖVR or just want to see one nonstandard approach to VR dev.
            """
            ])

        schedlist.append([
            '8:00PM',
            '8:20PM',
            'Talk',
            'Spot the Surveillance: A VR Experience for Keeping an Eye on Big Brother',
            'Rory, and <a href="http://schatzkin.com/">Artemis Schatzkin</a> (<a href="https://eff.org">EFF</a>)',
            """
Spot the Surveillance is an open-source educational Virtual Reality (VR) tool to help people recognize and understand the types of surveillance technology
that police deploy in their communities.
This talk will be how it was built and what is the future of this edu-virtual tech.
            """
            ])

        schedlist.append([
            '8:20PM',
            '9:00PM',
            'Talk',
            'Surfing The 90’s Virtual Reality Internet With VRML',
            'Sidepocket',
            """
Our DCG 201 Co-Founder has once again used his digital archeology skills to unearth another piece of virtual technology that the internet has forgotten about.
We will go over the VRML language, try to create a .wrl WORLD from scratch and trace its lineage to a shocking conclusion!
            """
            ])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append(["after the main content", None, "Special Features", None, None, ""])

        schedlist.append([
            '9:00 PM',
            None,
            'VR After-Party',
            'Virtual Reality Concert @ DCG 201 NOWHERE Virtual Reality Hacker Hangout',
            'DJ Vulp',
            """
We will be having an awesome DJ set by a virtual DJ while we party the night away and talk about 1337 haxxs!
This will both be on our LIVE Streams as well as in our NOWHERE virtual world!
            """
            ])




#        schedlist.append([
#            None,
#            None,
#            'Workshop',
#            'Hacker Show &amp; Tell',
#            None,
#            """
#After our lightning talks DCG 201 members will be given an opportunity to show off the various projects that they have been working on.
#You can join in any time as we chat and some things we might be showing off for the first time so you don’t want to miss this on the LIVE Stream!
#            """
#            ])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([
            None,
            '12:00 at the latest',
            'Sign-Off',
            'Good night!',
            'End of program.',
            '<em>Note: Twitch Viewers will Raid another Stream, dLive Watchers will earn LEMONS!</em>'])

        schedlist.append([None, None, None, None, None, None])
        schedlist.append([None, None, "COVID-19 Notice", "Keep an eye out for your fellow hacker.", "<strong><a href=\"https://covid19.nj.gov/vaccine\">GET YOUR VAX. They\'re available. Schedule it today.</a></strong>", "And finally, Whether you're social or anti-social, practice distancing."])


        for item in schedlist:
            schedtable.append( dict(zip(schedstruct, item)) )
        return schedtable

    def FormattedSchedule():
        schedule = MeetingDetails.Schedule()
        html = ""

        for item in schedule:

            html += "<h5>"

            if item["starttime"] is not None or item["endtime"] is not None:
                if item["starttime"] is not None:
                    if item["endtime"] is None:
                        html += "Starting "
                    html += item["starttime"]
                if item["starttime"] is not None and item["endtime"] is not None:
                    html += " - "
                if item["endtime"] is not None:
                    if item["starttime"] is None:
                        html += "Ending at "
                    html += item["endtime"]
                html += ": "

            html += "<em>"

            if item["eventtype"] is not None:
                html += "<u>" + item["eventtype"] + ":</u> "

            if item["title"] is not None:
                html += item["title"]

            html += "</em>"

            if item["speaker"] is not None:
                html += " <span style=\"font-weight: 300;\">&nbsp;| " + item["speaker"] + "</span>"

            html += "</h5>\n"

            if item["summary"] is not None:
                html += "<p>" + item["summary"] + "</p>\n"
            else:
                html += "<br>"

        return html

def main():
    ret =  "This month's meetup:\n"
    ret += MeetingDetails.Date() + ": " + MeetingDetails.Title() + "\n"
    ret += MeetingDetails.Location() + "\n"
    ret += MeetingDetails.Notice() + "\n"
    ret += "For more detailed information, see the " + MeetingDetails.LinkName() + " at " + MeetingDetails.CanonicalLink() + ".\n"
    ret += "\n"
    ret += MeetingDetails.Summary() + "\n"
    ret += "\nDEBUG: schedlist\n\n"
    ret += str(MeetingDetails.Schedule())
    ret += "\nDEBUG: html\n\n"
    ret += str(MeetingDetails.FormattedSchedule())
    ret += "\n\nEND DEBUG\n"
    print(ret)

if __name__ == "__main__":
    main()
