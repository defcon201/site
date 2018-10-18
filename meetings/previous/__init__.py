#!/usr/bin/env python3
# This is just a hack to get things working in time for deployment.


class PreviousMeetings:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake.
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Error"
    def Title():		# Title of the meeting
        return "Previous meeting data unavailable."
    def Location():		# Location of the meeting (usually "WHEALTH at Journal Square")
        return "at /meetings/previous.html"
    def Notice():		# Any important notices about the meeting or the information.
        return "<h5>Error <strong>201-0404</strong> <em>previous.data missing</em></h5>"
    def CanonicalLink():	# A link that refers to this meeting
        return "https://github.com/defcon201/site"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "documentation"
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
"""
    def Schedule():
        schedstruct = ['starttime', 'endtime', 'eventtype', 'title', 'speaker', 'summary']
        schedtable = []
        schedlist = []
        schedlist.append(['24', '7', 'Debugging', 'the site', 'mainly <a href="https://twitter.com/sirocyl">sirocyl</a>', 'Bear with us as we try to correct this error.'])
        for item in schedlist:
            schedtable.append( dict(zip(schedstruct, item)) )
        return schedtable

    def FormattedSchedule():
        schedule = PreviousMeetings.Schedule()
        html = ""
        for item in schedule:
            html += "<h5>" + item["starttime"] + " - " + item["endtime"] + ": <em>" + item["eventtype"] + ": " + item["title"] + "</em> <span style=\"font-weight: 300;\">&nbsp;| " + item["speaker"] + "</span></h5>\n"
            html += "<p>" + item["summary"] + "</p>\n"
        return html

if __name__ == "__main__":
    main()

