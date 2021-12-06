#!/usr/bin/env python3

class MeetingDetails:           # Any of these can be HTML formatted, but I'd recommend against it for semantics sake EXCEPT where triple quotes (""" like this """) appear.
    def Date():                 # Date of the meeting (Weekday, Month DD)
        return "Friday, December 18th"
    def Title():                # Title of the meeting
        return "XmasCon"
    def Location():             # Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "Online &mdash; Streaming Live"
    def Notice():               # Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():        # A link that refers to this meeting
        return "https://defcon201.medium.com/defcon-201-online-meet-up-december-2020-xmascon-2df1b72da8b7"
    def LinkName():             # What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "post on our Medium"
    def Summary():              # Short, 1-2 sentences about this meeting.
        return """
Can it be? Is it finally here? The final stretch to the END of 2020 is upon us!? This might be the best present we get this year!
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
        schedlist.append([None, None, None, None, "YouTube", '<a href="https://www.youtube.com/channel/UCYDQaOHbK5trRU2CDgb0qSg">https://www.youtube.com/channel/UCYDQaOHbK5trRU2CDgb0qSg</a><br>'])
        schedlist.append([None, None, None, None, "Chaturbate", '<em>Link to our Chaturbate stream will be announced soon.</em>'])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([None, None, "This month's charity fundraiser is", """<a href="http://www.childsplaycharity.org/">Child's Play</a>""", None, """
Child’s Play was born in 2003 after Mike Krahulik and Jerry Holkins of Penny Arcade, in response to how video games were portrayed negatively by the media, challenged their fans to help support Seattle Children’s Hospital. An Amazon Wishlist was set up and in less than one month, the charity raised over $250,000 in cash and toys for Seattle Children’s hospital.

"""])
        schedlist.append([None, None, None, "If you want to donate at any time, do so through the following link:", """<a href="https://donate.tiltify.com/@defcon201live/spirit-of-hohocon-childs-play-charity">Tiltify: DC201 Spirit Of HoHoCon Child’s Play Charity</a>""", None])



        schedlist.append([
            '6:00PM',
            '6:50PM',
            'Pre-show',
            '1993 B.C.: Get Off my LAN! (Hacking in the Olden Days)',
            'J0hnnyXm4s',
            """
Here, Johnny Xmas will deliver one of his famous “When I Was Your Age” rants, this time aimed at the 1990’s and the Rise of the Internet, and the explosion of the hacker community that happened back then, just as it is happening now.
            """
            ])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([
            '7:00PM',
            '8:00PM',
            'Interview',
            'From Stuxnet to Solar Winds',
            'Kim Zetter',
            """
We at DEFCON 201 are proud to interview cyber-journalist Kim Zetter! Topics will include the state of cybersecurity journalism, how journalist disclose sensitive hacks, hackers relationship with journalism, Governments VS Reporting, and her legendary work documenting Stuxnet and the current cutting-edge state of the Solar Winds breach.
            """
            ])

        schedlist.append([
            '8:00PM',
            '8:30PM',
            'Workshop',
            'Ninja Forge &mdash; Next Generation: Now With More GUI',
            'GI Jack',
            """
ninjaforge-ng is a tool for burning Ninja OS to USB sticks using the purpose created <em>.liveos.zip</em> format. This is part of an overhaul to make the Ninja OS more user friendly, consistent, and secure. The format is documented in a text file, and is freely available for use. This talk will go over the tool and format.
            """
            ])

        schedlist.append([
            '8:30PM',
            '9:00PM',
            'Talk',
            'SNAFU@Internet.mil',
            'sirocyl',
            """
sirocyl takes a look at an interesting case-study in network architecture, where a laptop’s mobile network somehow got DHCP-assigned to an IP address located squarely in the Pentagon.
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
