#!/usr/bin/env python3

class MeetingDetails:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake.
    from pages.meetings.previous import PreviousMeetings
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday, April 19"
    def Title():		# Title of the meeting
        return "#Moonstruck"
    def Location():		# Location of the meeting (usually "WHEAlTH at Journal Square")
        return "WHEALTH at Journal Square"
    def Notice():		# Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():	# A link that refers to this meeting
        return "https://www.meetup.com/DEFCON201/events/259623485/"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "Meetup event"
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
#Moonstruck is the new day of reckoning in a distracted world. No digital. No screens. All analog. Welcome to the Real World.
"""
    def Schedule():
        schedstruct = ['starttime', 'endtime', 'eventtype', 'title', 'speaker', 'summary']
        schedtable = []
        schedlist = []
        schedlist.append(['7:00PM', '8:00PM', 'Intro', 'Meet &amp; Greet + Digital Detox', 'DEFCON 201 members', 'Chat amongst friends, coordinate your public key portfolio, add cards to your Rolodex&trade;, and warm up for the talks!'])
        schedlist.append(['8:00PM', '8:05PM', 'Lightning Talk',  '#Moonstruck', 'Adbusters c/o Sidepocket', '<em>[Pending description]</em>'])
        schedlist.append(['8:05PM', '8:25PM', 'Talk',  'Ham Radio talk', 'ARRL', '<em>[Pending description.]</em>'])
        schedlist.append(['8:25PM', '8:50PM', 'Talk', '\'Fone\'s broke? I\'ll just call a repairman!', 'Sidepocket', '<em>[Pending description]</em>'])
        schedlist.append(['8:50PM', '9:00PM', 'Talk',  'Introduction to Lockpicking', 'TOOOL', '<em>[Pending description.]</em>'])
        schedlist.append(['9:00PM', '9:55PM', 'Workshops', 'January 2019', 'Open participation', 'Talk about and work together on projects!'])
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

