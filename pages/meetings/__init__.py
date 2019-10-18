#!/usr/bin/env python3

class MeetingDetails:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake.
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday, October 18th"
    def Title():		# Title of the meeting
        return "Hacktoberfest 3.0"
    def Location():		# Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "SUBCULTURE Jersey City, 260 Newark Ave."
    def Notice():		# Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():	# A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-meet-up-october-2019-hacktoberfest-3-0-92960ca339"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "Medium:"
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
        Join #DEFCON201 at SubCulture (260 Newark Ave, Jersey City NJ) on Friday, October 18th from 7pm - 10pm to learn about SSH Hardening, Hacktoberfest Github Pull Requests, Free Swag, Pumpcon Prep and more DC201 goodness!
"""
    def Schedule():
        schedstruct = ['starttime', 'endtime', 'eventtype', 'title', 'speaker', 'summary']
        schedtable = []
        schedlist = []
        schedlist.append(['7:00PM', '8:05PM', 'Intro', 'Meet &amp; Greet', 'DEFCON 201 members', 'Chat amongst friends, coordinate your public key portfolio, add cards to your Rolodex&trade;, and warm up for the talks!'])
        schedlist.append(['8:00PM', '8:35PM', 'Locking Down Production Access at Startup Scale',  'Liz Fong-Jones', 'DEFCON 201', 'Learn about what lessons translated when going from Google to a 25-person startup, and how a modicum of effort can better secure user data and access to production.'])
        schedlist.append(['8:35PM', '8:40PM', '<em>Hacktoberfest: The Stupid Content Tracker</em>',  'sirocyl', 'DEFCON 201', 'In this quick primer, you will learn how to navigate GitHub, how Git works, how to log into the Hacktoberfest website, how to do a Pull Request and what you need to do to earn your FREE T-Shirt and swag!'])
        schedlist.append(['8:40PM', '9:55PM', 'Workshops + Hacktoberfest 2019', 'June 2019', 'Open participation', 'Talk about and work together on projects! Do GitHub Pull Requests for Digital Ocean`s Hacktoberfest to win exclusive swag and prizes!'])
        schedlist.append(['9:55PM', '10:00PM', 'Wrap-Up', 'Official end of meeting', 'Good night!', '<em>Note: SUBCULTURE closes at 10pm. Please make sure your belongings are together before closing time.'])
        schedlist.append(['10:00PM', 'zzz', 'Pumpcon + Unofficial Ad-Hoc Hours', 'Downtown JC', 'Who\'s up?', 'A chunk of us will be heading to Pumpcon (https://www.pumpcon.org) in Philly! We also may decide to regroup at a local late night venue such as a diner or bar afterwards; this is ad-hoc and entirely unregulated airspace. Participate at your own risk.'])
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

