#!/usr/bin/env python3

class MeetingDetails:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake.
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday, November 15th"
    def Title():		# Title of the meeting
        return "No NAT November"
    def Location():		# Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "SUBCULTURE Jersey City, 260 Newark Ave."
    def Notice():		# Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():	# A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-meet-up-november-2019-no-network-address-translation-november-b7a0cdf4a407"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "Medium:"
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
        Join #DEFCON201 at SubCulture (260 Newark Ave, Jersey City NJ) on Friday, November 15th from 7pm - 10pm to learn about Web Browser Privacy & Security, live booting Windows, PWNagotchi, lockpicking and more!"""
    def Schedule():
        schedstruct = ['starttime', 'endtime', 'eventtype', 'title', 'speaker', 'summary']
        schedtable = []
        schedlist = []
        schedlist.append(['7:00PM', '8:05PM', 'Intro', 'Meet &amp; Greet', 'DEFCON 201 members', 'Chat amongst friends, coordinate your public key portfolio, add cards to your Rolodex&trade;, and warm up for the talks!'])
        schedlist.append(['8:00PM', '8:30PM', 'Browsing The Internet Privately & Securely',  'Sidepocket', 'DEFCON 201', 'In this talk, we will help you navigate the confusing world of Web Browser Privacy & Security aimed for everyone but ideally for beginners.'])
        schedlist.append(['8:30PM', '8:35PM', '<em>Windows When You Need ’em, Walls When You Don’t</em>',  'sirocyl', 'DEFCON 201', 'At MAGFest this year, sirocyl will be doing a workshop on a program called FamiTracker which is Windows-only, doesn’t work in WINE or ReactOS and will need to run on people’s own laptops; including those running Linux or something else.'])
        schedlist.append(['8:35PM', '9:55PM', 'Workshops + Hackathon', 'June 2019', 'Open participation', 'Talk about and work together on projects! Open Projects Include Lockpicking, PWNagotchi, Live Booting Windows and Nintendo LABO VR Kits!'])
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

