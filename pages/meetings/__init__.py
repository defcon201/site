#!/usr/bin/env python3

class MeetingDetails:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake.
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday,May 17"
    def Title():		# Title of the meeting
        return "The System Is Down"
    def Location():		# Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "SUBCULTURE Jersey City, 260 Newark Ave."
    def Notice():		# Any important notices about the meeting or the information.
        return "<h3>Note! Meeting location changed!</h3><p style=\"font-size: larger\">The May meeting, and all following meetings for the foreseeable future, will be held at SUBCULTURE Jersey City.</p><h4>Do not arrive at WHEALTH!</h4>"
    def CanonicalLink():	# A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-meet-up-may-2019-the-system-is-down-a80646eda075"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "View our Medium Blog Post..."
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
Join us in a continued celebration of our new venue and find out what is up ahead for DEFCON 201 from June to September!
"""
    def Schedule():
        schedstruct = ['starttime', 'endtime', 'eventtype', 'title', 'speaker', 'summary']
        schedtable = []
        schedlist = []
        schedlist.append(['7:00PM', '8:00PM', 'Intro', 'Meet &amp; Greet + Digital Detox', 'DEFCON 201 members', 'Chat amongst friends, coordinate your public key portfolio, add cards to your Rolodex&trade;, and warm up for the talks!'])
        schedlist.append(['8:00PM', '8:10PM', 'Lightning Talk',  'Configuring Privoxy & JonDo', 'n0ctilucient', '<em>[Pending description]</em>'])
        schedlist.append(['8:10PM', '8:40PM', 'Talk',  'TBA', 'NCommander', '<em>[Pending description.]</em>'])
        schedlist.append(['8:40PM', '8:50PM', 'Lightning Talk', 'Vintage Computer Festival East 2019: A Recap and Show & Tell', 'sirocyl', '<em>In this short talk, our presenter will go over the Vintage Computer Festival (VCF) East including a show and tell of the COMPAQ SLT 286 he bought at the festival.</em>'])
        schedlist.append(['8:50PM', '9:55PM', 'Workshops', 'JMay 2019', 'Open participation', 'Talk about and work together on projects!'])
        schedlist.append(['9:55PM', '10:00PM', 'Wrap-Up', 'Official end of meeting', 'Good night!', '<em>Note: SUBCULTURE closes at 10pm. Please make sure your belongings are together before closing time.'])
        schedlist.append(['10:00PM', 'zzz', 'Unofficial Ad-Hoc Hours', 'Downtown JC', 'Who\'s up?', 'We may decide to regroup at a local late night venue such as a diner or bar afterwards; this is ad-hoc and entirely unregulated airspace. Participate at your own risk.'])
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

