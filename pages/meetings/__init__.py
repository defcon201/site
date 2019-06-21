#!/usr/bin/env python3

class MeetingDetails:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake.
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday, June 21st"
    def Title():		# Title of the meeting
        return "PEBKAC"
    def Location():		# Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "SUBCULTURE Jersey City, 260 Newark Ave."
    def Notice():		# Any important notices about the meeting or the information.
        return "<h3>Note! Meeting location changed!</h3><p style=\"font-size: larger\">The June meeting, and all following meetings for the foreseeable future, will be held at SUBCULTURE Jersey City.</p><h4>Do not arrive at WHEALTH!</h4>"
    def CanonicalLink():	# A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-meet-up-june-2019-pebkac-55e9148a616c"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "View our Medium Blog Post..."
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
Join us for membership annoucements, Nintendo Switch Hacking, Facebook Libra and Mainframe Password Hardening!
"""
    def Schedule():
        schedstruct = ['starttime', 'endtime', 'eventtype', 'title', 'speaker', 'summary']
        schedtable = []
        schedlist = []
        schedlist.append(['7:00PM', '8:00PM', 'Intro', 'Meet &amp; Greet + Digital Detox', 'DEFCON 201 members', 'Chat amongst friends, coordinate your public key portfolio, add cards to your Rolodex&trade;, and warm up for the talks!'])
        schedlist.append(['8:00PM', '8:10PM', 'Lightning Talk',  'Configuring Privoxy & JonDo', 'n0ctilucient', '<em>[Pending description]</em>'])
        schedlist.append(['8:10PM', '8:20PM', 'Lightning Talk',  'Joy Con-ning The Nintendo Switch Hardware & Accessories', 'sirocyl', '<em>[Pending description.]</em>'])
        schedlist.append(['8:20PM', '8:40PM', 'Talk', 'Learning About Libra and Why Facebook’s Cryptocurrency is Pure High Octane Nightmare Fuel', 'Sidepocket', '<em>In this talk, DEFCON 201 Co-Founder Sidepocket will go over the Libra platform, what makes it tick and why this whole initiative by Facebook is a horrible idea including privacy concerns and evil open source hacks.</em>'])
        schedlist.append(['8:40PM', '9:55PM', 'Workshops', 'June 2019', 'Open participation', 'Talk about and work together on projects!'])
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

