#!/usr/bin/env python3

class MeetingDetails:           # Any of these can be HTML formatted, but I'd recommend against it for semantics sake EXCEPT where triple quotes (""" like this """) appear.
    def Date():                 # Date of the meeting (Weekday, Month DD)
        return "Friday, October 16th"
    def Title():                # Title of the meeting
        return "Revenge Of Hacktoberfest"
    def Location():             # Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "Online &mdash; Streaming Live</em>"
    def Notice():               # Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():        # A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-online-meet-up-october-2020-revenge-of-hacktoberfest-aaf37809bc3f?source=friends_link&sk=9ee628ebc06bf40d357d8a046298ac24"
    def LinkName():             # What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "post on our Medium"
    def Summary():              # Short, 1-2 sentences about this meeting.
        return """Calling all hackers for a spooky meet up with the Hacktoberfest hackathon, CTF and an amazing all witchy speaker line up!"""

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
        schedlist.append([None, None, None, None, "YouTube", '<a href="https://www.youtube.com/channel/UCYDQaOHbK5trRU2CDgb0qSg">https://www.youtube.com/channel/UCYDQaOHbK5trRU2CDgb0qSg</a><br>'])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([
            '6:00PM',
            '6:30PM',
            '(Online) Pre-show',
            'Spoopy Pre-Show + DEFCON 201 Announcements',
            'Nexpo &amp; DEFCON 201 Staff',
            """Enjoy this 20 minute video of spooky hacker entertainment followed by community announcements and updates from DEFCON 201 Staff with some casual chat with our audience."""
            ])

        schedlist.append([
            '6:30PM',
            '7:00PM',
            'Talk',
            'The Horrors Of Voting In The US Election System',
            'BiaSciLab &amp; Margaret E. MacAlpine',
            """In this double hitter starts with BiaSciLab on how Mail In Voting works and the myths of its security issues debunked. Then a live Q&A with a representative of the DEF CON Voting Machine Hacking Village on current issues with election security."""
            ])

        schedlist.append([
            '7:00PM',
            '8:00PM',
            'Talk',
            'Cyber Collective Interview',
            'Tazin Khan',
            """We at DEFCON 201 are honored to feature a representative of The Cyber Collective, a community-centered organization that hosts events to understand the ways data and privacy impact consumers."""
            ])

        schedlist.append([
            '8:00PM',
            '9:00PM',
            'Workshop',
            'Spy For A Day: Caesar’s Code C++ Workshop for BeginnersAbusing & Securing XPC in macOS Apps',
            'vvvalentina',
            """This is a beginner / intermediate c++ workshop on how to create a cipher using Caesar’s code. This is a lesson on encryption, decryption and how to compile your code through the terminal."""
            ])

        schedlist.append([
            '9:00PM',
            '9:10PM',
            'Workshop',
            'Beginners Guide To CTF',
            'phoenixfyrefly',
            """Long time friend of DEFCON 201 phoenixfyrefly will go over what a CTF (Capture The Flag)game is, what hardware and software you should run, how to submit a Flag point and getting prepared for the Hacktober CTF in the Open Workshop! <a href="https://medium.com/@defcon201/defcon-201-online-ctf-hacktoberfest-ctf-oct-16th-17th-6d69b2c07ee0?source=friends_link&sk=23d1acbe1d7381acb1322d8889157ef9">Click Here for Hacktoberfest CTF (Oct 16th 10AM — Oct 17th 10PM) Medium Blog Details</a>."""
            ])

        schedlist.append([
            '9:10PM',
            '9:45PM',
            'Lightning Talks',
            'Hacktoberfest Primer',
            'sidepocket',
            """At 9:10 PM EST we will begin our LIVE Stream portion of Hacktoberfest featuring an Intro to Hacktoberfest 2020 by Sidepocket, What Is Open Source by GI Jack, A Workshop On How To Use Git by sirocyl, a demo of Hacktoberfest Open Source Projects and Introduction to all partcipating hacker!"""
            ])

        schedlist.append([
            '9:45PM',
            '11:59PM',
            'Workshop',
            'Hacktoberfest 2020 Hackathon',
            'xio',
            """Hacktoberfest — brought to you by DigitalOcean in partnership with Dev & Intel — is a month-long celebration of open source software. First, sign up on the Hacktoberfest site at https://hacktoberfest.digitalocean.com. To qualify for the official limited edition Hacktoberfest shirt, you must register and make four pull requests between October 1–31. Sign Up at <a href="https://organize.mlh.io/participants/events/4435-defcon-201-return-of-hacktoberfest">Major League Hacking</a> for updates and Join Us on the <a href="https://discord.gg/PGgPNEF">DC201 Discord</a> to interact and be on our LIVE Stream!"""
            ])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([
            None,
            '12:00 MIDNIGHT',
            '(Online) Sign-Off',
            'End of programmed content on DEFCON 201 Live.',
            'Good night!',
            '<em>Note: Twitch Viewers will Raid another Stream, dLive Watchers will earn LEMONS!</em>'])

        
        schedlist.append([None, None, None, None, None, None])
        schedlist.append([None, None, "COVID-19 Notice", "Keep an eye out for your fellow hacker. Whether you're social or anti-social, practice distancing.", None, None])


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
                        html += "Starting at "
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
                html += item["eventtype"] + ": "

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
