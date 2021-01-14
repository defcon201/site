#!/usr/bin/env python3

class MeetingDetails:           # Any of these can be HTML formatted, but I'd recommend against it for semantics sake EXCEPT where triple quotes (""" like this """) appear.
    def Date():                 # Date of the meeting (Weekday, Month DD)
        return "Friday, January 15th"
    def Title():                # Title of the meeting
        return "Halt &amp; Catch Fire"
    def Location():             # Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "Online &mdash; Streaming Live"
    def Notice():               # Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():        # A link that refers to this meeting
        return "https://defcon201.medium.com/defcon-201-online-meet-up-january-2021-halt-catch-fire-e7d04eedd1d9"
    def LinkName():             # What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "post on our Medium"
    def Summary():              # Short, 1-2 sentences about this meeting.
        return """
So uh... normally we summarize what has been going on so far this month in the lead up to our meet up but... do we even have to? Have you been online? Have you seen the news?<br>
We are sadly past the 7-day trial for 2021 and are unable to get a refund so... fuck it!
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
            '5:30PM',
            '5:55PM',
            'Pre-show',
            'Don\'t Be a Sucker',
            'United States Department of War (From the archives, 1943)',
            """
Our PRE-SHOW will a public domain short film that is even more relevant now than it was back then.
            """
            ])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([
            '6:00PM',
            '6:30PM',
            'Talk',
            'From The Current State of DevOops',
            'Tillie Kottmann',
            """
A short overview on how source code and secrets can often be extracted from the most popular DevOps tools, followed by some details around recent leaks, how they were acquired and what you can find in them.
            """
            ])

        schedlist.append([
            '6:30PM',
            '7:00PM',
            'Workshop',
            'Internals of Conti Ransomware',
            'Nikhil Rathor',
            """
This talk will be dissecting this ransomware from writing the logic bomb in the macros of the office docs to the loading the malicious payload/executable execs run32dll.exe being deployed for the triage of targeted machines.
            """
            ])

        schedlist.append([
            '7:00PM',
            '7:30PM',
            'Talk',
            'Privacy After The Insurrection',
            'Albert Fox Cahn (S.T.O.P.)',
            """
In the aftermath of last week’s horrific attack on the Capitol, new questions are being raised about the role of surveillance in identifying insurrectionists and responding toe right-wing violence.<br>
Albert Fox Cahn of the Surveillance Technology Oversight Project (S.T.O.P.) will discuss the dangers of expanding surveillance in these challenging times.
            """
            ])

        schedlist.append([
            '7:30PM',
            '8:00PM',
            'Talk',
            'Cooking Out Of The Frying Pan with 1A Snake Oil',
            'Sidepocket',
            """
In this quick PSA, Sidepocket will go over these bad services past and present, present a methodology on how to identify a good or bad service and highlight some actual alternatives that will help make a more balanced internet.
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
