#!/usr/bin/env python3

class MeetingDetails:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake.
    from pages.meetings.previous import PreviousMeetings
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday, January 18"
    def Title():		# Title of the meeting
        return "Shmoo-zing Around"
    def Location():		# Location of the meeting (usually "WHEAlTH at Journal Square")
        return "WHEALTH at Journal Square"
    def Notice():		# Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():	# A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-january-2019-shmoo-zing-around-905955bcbf5a"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "post on our Medium"
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
Welcome to the first DEFCON 201 Meet Up of 2019! Despite a crazy schedule and a potential snowstorm, we are still meeting up today for some hacker shenanigans. In this installment, we are going to learn about WebPKI, live stream Shmoocon and share some good times together as we launch big workshops, projects and events February and beyond!
"""
    def Schedule():
        schedstruct = ['starttime', 'endtime', 'eventtype', 'title', 'speaker', 'summary']
        schedtable = []
        schedlist = []
        schedlist.append(['7:00PM', '8:00PM', 'Intro', 'Meet &amp; Greet + Shmoocon Live Stream', 'DEFCON 201 members', 'Chat amongst friends, coordinate your public key portfolio, add cards to your Rolodex&trade;, and warm up for the talks!'])
        schedlist.append(['8:00PM', '8:05PM', 'Talk',  'DEFCON 201: The First Half of 2019', 'Sidepocket', '<em>[Pending description]</em>'])
        schedlist.append(['8:05PM', '9:00PM', 'Talk',  'Understanding WebPKI', 'NCommander', '<em>[Pending description.]</em>'])
        schedlist.append(['8:50PM', '9:55PM', 'Workshops', 'January 2019', 'Open participation', 'During workshops, Shmoocon will be streamed in the background.'])
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

