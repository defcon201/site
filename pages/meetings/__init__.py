#!/usr/bin/env python3

class MeetingDetails:           # Any of these can be HTML formatted, but I'd recommend against it for semantics sake EXCEPT where triple quotes (""" like this """) appear.
    def Date():                 # Date of the meeting (Weekday, Month DD)
        return "Friday, April 16th"
    def Title():                # Title of the meeting
        return "Application Is Meditating"
    def Location():             # Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "Online &mdash; Streaming Live"
    def Notice():               # Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():        # A link that refers to this meeting
        return "https://defcon201.medium.com/defcon-201-online-meet-up-april-2021-application-is-meditating-a2f717cb6ee3"
    def LinkName():             # What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "post on our Medium"
    def Summary():              # Short, 1-2 sentences about this meeting.
        return """
Join us for this month's meet up as we deep dive into more traditional hacker AF topics from hardware maniuplation, exploits, digital archiving and more!
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

        schedlist.append([None, None, None, "DEFCON 201 is streaming online.", None, "Live Streams are available at:"])
        schedlist.append([None, None, None, None, "Twitch",  '<a href="https://www.twitch.tv/defcon201live">https://www.twitch.tv/defcon201live</a><br>'])
        schedlist.append([None, None, None, None, "dLive",   '<a href="https://dlive.tv/defcon201">https://dlive.tv/defcon201</a><br>'])
        schedlist.append([None, None, None, None, "YouTube", '<a href="https://www.youtube.com/c/defcon201">https://www.youtube.com/c/defcon201</a><br>'])

        schedlist.append([None, None, None, None, None, None])


        schedlist.append([
            '7:00PM',
            '8:00PM',
            'Pre-show',
            'It\'s not FINished: The Evolving Maturity in Ransomware Operations',
            'Mitchell Clarke, Tom Hall, Joe Slowik (Black Hat Webcast Series)',
            """
Our PRE-SHOW will feature a relevant talk from the Black Hat Webinar series! Synopsis from their description below:<br>
<blockquote style="font-size: 9pt; border-left: solid 1px #666; padding-left: 0.5em;">
Ransom demands are becoming larger, attackers smarter, and intrusions longer.
We will be sharing tradecraft we've seen ransomware threat actors employ across Europe in 2020.
Not only are intrusion tactics improving, but attackers are also transitioning and developing sleek ransomware-as-a-service platforms.
Threat actors are professionalising and streamlining their platforms.
These platforms are being used by threat actors to generate malware, to communicate and negotiate with victims, and in some cases, for payment processing and decryption utility delivery.</blockquote>
            """
            ])

        schedlist.append([
            '8:00PM',
            '8:30PM',
            'Talk',
            'Detecting At-Risk Software Infrastructure',
            'Kaylea Champion',
            """
Software serves as infrastructure, and it can suffer from a lack of maintenance. We want to understand how to detect this kind of risk in Free/Libre Open Source Software infrastructure before major failures occur.
            """
            ])

        schedlist.append([
            '8:30PM',
            '9:00PM',
            'Workshop',
            'The Joycon Symphonic Orchestra',
            'sirocyl',
            """
In this talk DCG 201 Member sirocyl will look at a program that allows Nintendo Switch Joy-Cons to play .midi files. This will be followed by a mini-jam session that might extend to the hang out portion of the meet up!
            """
            ])

        schedlist.append([
            '9:00PM',
            '10:00PM',
            'Talk',
            'npm\'s Gone Wild: The undefined Edition (CVE-2021-28918)',
            'SickCodes, John Hacking, Kaoudis, Koroeskohr, Tensor_Bodega',
            """
How we copped a decade old 0-day, while fixing another one. Randomly assembled global team of then strangers. The power of dropping research on a Sunday.
            """
            ])

        schedlist.append([None, None, None, None, None, None])
        schedlist.append(["after the main content", None, "Special Features", None, None, ""])

        schedlist.append([
            None,
            None,
            'Workshop',
            'Hacker Show &amp; Tell',
            None,
            """
After our lightning talks DEFCON 201 members will be given an opportunity to show off the various projects that they have been working on.
You can join in any time as we chat and some things we might be showing off for the first time so you don’t want to miss this on the LIVE Stream!
            """
            ])

        schedlist.append([
            "5PM EST April 16",
            None,
            'Workshop',
            '<a href=\"https://plaidctf.com/\">PlaidCTF 2021</a>',
            'To join the CTF, see: <a href=\"https://www.meetup.com/DEFCON201/events/277538780/\">https://www.meetup.com/DEFCON201/events/277538780/</a>',
            """
This Friday, starting on April 16th at 5:00 PM EST, we invite all DEFCON 201 Members, Attendees and Fans to help us hack the PlaidCTF 2021!
If you are new to Online CTF, we will help you get set up and walk you through some of the challenges.
Then you can log in anytime after until April 17th 5:00 PM EST to continue our CTF conquest!<br><br>
What To Bring: Any laptop will do. Ideally you want to load it full of Information Security Red Team and Blue Team tools, look at Kali Linux, Parrot OS, Pentoo or Black Arch for ideas. To participate online, you will need a Discord Account and to join our Discord at this link: <a href=\"https://discord.gg/PGgPNEF\">https://discord.gg/PGgPNEF</a><br><br>

To learn more about the CTF, please follow the link above!
            """
            ])

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
