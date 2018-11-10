#!/usr/bin/env python3

class MeetingDetails:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake.
    from pages.meetings.previous import PreviousMeetings
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday, November 16"
    def Title():		# Title of the meeting
        return "Hacksgiving"
    def Location():		# Location of the meeting (usually "WHEAlTH at Journal Square")
        return "WHEALTH at Journal Square"
    def Notice():		# Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():	# A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-meet-up-november-2018-hacksgiving-8acb789dfeb5"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "post on our Medium"
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
Come down to DEFCON 201 where we will have some cool WebSec centric lightning talks, a Hacksgiving homemade potluck and planning out chaotic-good projects to launch in early 2019!
"""
    def Schedule():
        schedstruct = ['starttime', 'endtime', 'eventtype', 'title', 'speaker', 'summary']
        schedtable = []
        schedlist = []
        schedlist.append(['7:00PM', '8:00PM', 'Intro', 'Meet &amp; Greet + GPG Keysigning', 'DEFCON 201 members', 'Chat amongst friends, coordinate your public key portfolio, add cards to your Rolodex&trade;, and warm up for the talks!'])
        schedlist.append(['8:00PM', '8:30PM', 'Talk',  'An In-Depth Look At the Domain Name System; the Yellow Pages of the Internet', 'NCommander', '<em>[Pending description]</em>'])
        schedlist.append(['8:30PM', '8:40PM', 'Talk', 'Password “Alternatives”: Causing More Problems Than They Solve', 'Sidepocket', '<em>[Pending description.]</em>'])
        schedlist.append(['8:40PM', '8:50PM', 'Show &amp; Tell', 'Hacksgiving Potluck', 'Open participation', 'Bring in tasty food!'])
        schedlist.append(['8:50PM', '9:55PM', 'Workshops', 'November 2018', 'Open participation', 'Workshops today are: Hackgiving Potluck Sampling'])
        schedlist.append(['9:30PM', '9:55PM', 'Project', 'DEFCON 201 Video Filming', 'GI Jack, Sidepocket, Xio', 'DEFCON 201 is going to be filming a short, public intro-duck-chin to what we are, as a DEFCON Group, and how we contribute to the local community, as well as the <span style="text-decoration: line-through">global hacker conspiracy</span> broader mission and spirit of hacking.'])
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

