#!/usr/bin/env python3
# This is just a hack to get things working in time for deployment.

class PreviousMeetings:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake.
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday, October 19"
    def Title():		# Title of the meeting
        return "Hacktoberfest 2.0 Brew-Ha-Ha"
    def Location():		# Location of the meeting (usually "WHEAlTH at Journal Square")
        return "WHEALTH at Journal Square"
    def Notice():		# Any important notices about the meeting or the information.
#        return "<h5><strong>Note:</strong> <em>All the following information is TBD; a final version will be posted a week before the meeting.</em></h5>"
        return ""
    def CanonicalLink():	# A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-meet-up-october-2018-hacktoberfest-2-0-brew-ha-ha-d4ba4be0ba36"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "post on our Medium"
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
We had three conflicting themes for this upcoming meeting. On one hand, it’s Octoberfest and a lot of hackers love beer. On the other hand, it’s Hacktoberfest and a lot of hackers love improving code. Then you add in Halloween where we get to dress as a Prostitute Apple Newton and act like an ass-hat. So we decided…why not all three? Please join us for a stuffed to the brim meet up with activities such as drinking our first ever DEFCON 201 Homebrew beer, doing git pulls for FREE T-Shirts, work on your Halloween outfit and more!
"""
    def Schedule():
        schedstruct = ['starttime', 'endtime', 'eventtype', 'title', 'speaker', 'summary']
        schedtable = []
        schedlist = []
        schedlist.append(['7:00PM', '8:00PM', 'Intro', 'Meet &amp; Greet', 'DEFCON 201 members', 'Chat amongst friends, coordinate your public key portfolio, add cards to your Rolodex&trade;, and warm up for the talks!'])
        schedlist.append(['8:00PM', '8:20PM', 'Talk',  '$brew Open Source Beer: A Study Of Large Scale Projects', 'Sidepocket', 'In this talk, we\'ll go over how to brew your own beer, and how we brewed our own beer, and why that may not exactly be the same thing...'])
        schedlist.append(['8:20PM', '8:50PM', 'TBA', 'TBA', 'TBA', '<em>To be announced.</em>'])
        schedlist.append(['8:50PM', '9:00PM', 'Talk', 'Intro to Hacktoberfest', 'Sidepocket, GI Jack', ''])
        schedlist.append(['9:00PM', '9:55PM', 'Workshops', 'September 2018', 'Open participation', 'Workshops today are: Hacktoberfest, Open Source Show and Tell, and Halloween Costume Craftathon'])
        schedlist.append(['9:55PM', '10:00PM', 'Wrap-Up', 'Official end of meeting', 'Good night!', ''])
        for item in schedlist:
            schedtable.append( dict(zip(schedstruct, item)) )
        return schedtable

    def FormattedSchedule():
        schedule = MeetingDetails.Schedule()
        html = ""
        for item in schedule:
            html += "<h5>" + item["starttime"] + " - " + item["endtime"] + ": <em>" + item["eventtype"] + ": " + item["title"] + "</em> <span style=\"font-weight: 300;\">&nbsp;| " + item["speaker"] + "</span></h5>\n"
            html += "<p>" + item["summary"] + "</p>\n"
        return html
    def FormattedSchedule():
        schedule = PreviousMeetings.Schedule()
        html = ""
        for item in schedule:
            html += "<h5>" + item["starttime"] + " - " + item["endtime"] + ": <em>" + item["eventtype"] + ": " + item["title"] + "</em> <span style=\"font-weight: 300;\">&nbsp;| " + item["speaker"] + "</span></h5>\n"
            html += "<p>" + item["summary"] + "</p>\n"
        return html
