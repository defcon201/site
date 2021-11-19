#!/usr/bin/env python3

class MeetingDetails:           # Any of these can be HTML formatted, but I'd recommend against it for semantics sake EXCEPT where triple quotes (""" like this """) appear.
    def Date():                 # Date of the meeting (Weekday, Month DD)
        return "Friday, November 19th"
    def Title():                # Title of the meeting
        return "No Net November"
    def Location():             # Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "<a href=\"https://www.subculturejc.com/\">Sub Culture</a> (260 Newark Ave. Jersey City)"
    def Notice():               # Any important notices about the meeting or the information.
        return "" # "<h5>This meeting will also have an online/streaming component.</h5>"
    def CanonicalLink():        # A link that refers to this meeting
        return "https://defcon201.org/meetings/meetings.html"
    def LinkName():             # What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "meeting page"
    def Summary():              # Short, 1-2 sentences about this meeting.
        return """
Planning? We don't need no stinkin' planning!
"""
    def LongSummary():
        # return Summary()
        return """

<h2>This month's <span style="font-size: smaller;" class="dc201-wordmark">DCG<span class="xicon-201bell"></span>201</span> meeting has been...</h2> dare I say it &mdash; <h2><em>"cancelled".</em></h2><br>
<br>
<h4>Streaming:</h4><br>
For those of you near and far, anticipating a streaming show at the usual time and date: We'll see you next month, for the December meeting, on 12/17.<br>
<strong>There is no streaming component, this time.</strong> Other streaming programming for the rest of the month may continue as scheduled.<br><br>

<h4>In-person at Subculture:</h4><br>
While the actual DCG201 meeting agenda is cancelled for this month, due to the last-minute nature of this cancellation, we may anticipate people to possibly show up anyway.<br>
To that end &mdash; and we cannot guarantee this, but &mdash; there may be at least one DCG201 member present.<br>
We shall continue to host an abridged DCG201 session, as an impromptu hacker gathering, not unlike the 2600 meets &mdash; with no formal agenda or scheduled talks at this time.<br><br>

The location remains at Sub Culture, 260 Newark Ave., Jersey City. Order a sandwich and chat amongst yourselves. :)<br>
Finally, while the start time will remain as usual, this meeting <em>may</em> end early if there is low turnout.

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

        '''
        schedlist.append([None, None, None, "<h4>For information about our planned schedule, both online and off, please check the <a href=\"" + MeetingDetails.CanonicalLink() + "\">" + MeetingDetails.LinkName() + "</a>.</h4>", None, None])

        schedlist.append([None, None, None, "DCG 201 will also be streaming online.", None, "Live Streams are available at:"])
        schedlist.append([None, None, None, None, "Twitch",  '<a href="https://www.twitch.tv/defcon201live">https://www.twitch.tv/defcon201live</a><br>'])
        schedlist.append([None, None, None, None, "dLive",   '<a href="https://dlive.tv/defcon201">https://dlive.tv/defcon201</a><br>'])
        schedlist.append([None, None, None, None, "YouTube", '<a href="https://www.youtube.com/c/defcon201">https://www.youtube.com/c/defcon201</a><br>'])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([None, None, None, None, None, None])
        '''
        schedlist.append([None, None, None, """

<h2>This month's <span style="font-size: smaller;" class="dc201-wordmark">DCG<span class="xicon-201bell"></span>201</span> meeting has been...</h2> dare I say it &mdash; <h2><em>"cancelled".</em></h2><br>
<br>
<h4>Streaming:</h4><br>
For those of you near and far, anticipating a streaming show at the usual time and date: We'll see you next month, for the December meeting, on 12/17.<br>
<strong>There is no streaming component, this time.</strong> Other streaming programming for the rest of the month may continue as scheduled.<br><br>

<h4>In-person at Subculture:</h4><br>
While the actual DCG201 meeting agenda is cancelled for this month, due to the last-minute nature of this cancellation, we may anticipate people to possibly show up anyway.<br>
To that end &mdash; and we cannot guarantee this, but &mdash; there may be at least one DCG201 member present.<br>
We shall continue to host an abridged DCG201 session, as an impromptu hacker gathering, not unlike the 2600 meets &mdash; with no formal agenda or scheduled talks at this time.<br><br>

The location remains at Sub Culture, 260 Newark Ave., Jersey City. Order a sandwich and chat amongst yourselves. :)<br>
Finally, while the start time will remain as usual, this meeting <em>may</em> end early if there is low turnout.

        """, None, None])
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
