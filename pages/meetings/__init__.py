#!/usr/bin/env python3

class MeetingDetails:           # Any of these can be HTML formatted, but I'd recommend against it for semantics sake EXCEPT where triple quotes (""" like this """) appear.
    def Date():                 # Date of the meeting (Weekday, Month DD)
        return "Friday, March 19th"
    def Title():                # Title of the meeting
        return "FOUR F&amp;amp;&bull;&raquo;&mdash;ING YEARS"
    def Location():             # Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "Online &mdash; Streaming Live"
    def Notice():               # Any important notices about the meeting or the information.
        return "Big Blue Button link will be posted <strong>on March 19th at 5PM EST.</strong>"
    def CanonicalLink():        # A link that refers to this meeting
        return "https://defcon201.medium.com/defcon-201-online-meet-up-march-2021-four-f-king-years-c7dbb46543b3"
    def LinkName():             # What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "post on our Medium"
    def Summary():              # Short, 1-2 sentences about this meeting.
        return """
We are going to party like it’s 1995, because now that we know that there is a plague out there &mdash; unlike last time &mdash; in the immortal words of a moron, "WE'LL DO IT LIVE!" on the DEFCON 201 LIVE Stream!
This month we are going to make YOU the focus of the event along with special guests from all over the hacker world to drink, play, and hack our way into a new year of Dirty Jersey!
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

        schedlist.append([None, None, None, None, None, None])


        schedlist.append([
            None,
            '6:30PM',
            '<em>Pre</em>-pre-show',
            'This is New Jersey',
            'New Jersey Bell Telephone Company (From the archives, 1956)',
            """
This Technicolor film was produced in 1956 for the New Jersey Bell Telephone Company, and based on a 1953 John T. Cunningham book <em>This is New Jersey</em>.
            """
            ])

        schedlist.append([
            '6:30PM',
            '7:00PM',
            'Pre-show',
            '&#x1F3B5; Hacker Tunes',
            '<a href="https://twitter.com/djjackalope">miss jackalope</a>',
            """
We at DEFCON 201 are honored to have the reigning queen of hacker beats, Miss DJ Jackalope, to do a 30 minute music set for our anniversary!
            """
            ])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([
            '7:05PM',
            '7:30PM',
            'Talk',
            'Slipping A Mickey: The Strange OSINT Iceberg of The Walt Disney Corporation',
            'Sidepocket',
            """
In this talk, we will go through a select history of Disney technologies, from the scrapped EPCOT future city, to the innovative People Movers, the ill-fated Go.com domain and the Magic Band RFID badges that are being used today! And of course, how to hack all of them!
            """
            ])

        schedlist.append([
            '7:30PM',
            None,
            '&#x1F973; Party!',
            'DEFCON 201 Anniversary Party',
            None,
            """
Hang out in our Big Blue Button Senfcall instance where you can chat about 1337 haxxs (and drink)!
Various notorious hackers from all over the net will join us including some special guests that YOU DON’T WANT TO MISS!
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
            None,
            None,
            'Workshop',
            'DEFCON 201 VidHug',
            'Link will be posted <em>March 18</em> on our Medium, Twitter, and here.',
            """
Sadly some of our favorite people won’t be able to make it live, including many of you.
So after we share it to some of our personal folks, we will be posting publicly the link to our <a href="https://www.vidhug.com/">VidHug</a> to record a massive pre-recorded Anniversary video!
You can record yourself wishing us a happy 4 years, show off 1337 skills and shout HACK THE PLANET in Zero Cool style!
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
