#!/usr/bin/env python3

class MeetingDetails:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake.
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday, January 17th"
    def Title():		# Title of the meeting
        return "Winter & Construction"
    def Location():		# Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "SUBCULTURE Jersey City, 260 Newark Ave."
    def Notice():		# Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():	# A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-meet-up-january-2020-winter-construction-98be3bef7566"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "Medium:"
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
        Join #DEFCON201 at SubCulture (260 Newark Ave, Jersey City NJ) on Friday, December 20th from 7pm - 10pm to watch Mr. Robot, share gifts, listen to Hacker Rants, Nintendo Labo, justCTF, lockpicking and more!"""
    def Schedule():
        schedstruct = ['starttime', 'endtime', 'eventtype', 'title', 'speaker', 'summary']
        schedtable = []
        schedlist = []
        schedlist.append(['7:00PM', '7:20PM', 'Intro', 'Meet &amp; Greet', 'DEFCON 201 members', 'Chat amongst friends, coordinate your public key portfolio, add cards to your Rolodex&trade;, and warm up for the talks!'])
        schedlist.append(['7:20PM', '7:50PM', 'An Introduction to Antivirus Evasion',  'Black Cipher', 'DEFCON 201', 'This presentation will provide an introduction to the concept of antivirus evasion techniques. It will cover the Who and Why of Antivirus Evasion, common Antivirus Evasion techniques such as obfuscation, abuse of whitelisted apps, packers, ect. This will conclude with a few demos showing AV evasion in action.'])
        schedlist.append(['7:50PM', '8:00PM', '<em>Windows DEFCON 201 Updates & Code of Conduct</em>',  'GI Jack', 'DEFCON 201', 'DEFCON 201 will start with various updates about our activities in early 2020 and an overview of the Code of Conduct linked on our website. This will conclude with HUGE ANNOUCEMENTS of DEFCON 201 activities that will start in February that you will only hear first in person at this meet up!'])
        schedlist.append(['8:00PM', '8:10PM', '<em>Wards, Decoders and Disk Detainers OH MY!</em>',  'Sidepocket', 'DEFCON 201', 'In this quick overview, we will go over new additional tools and techniques in our kit which includes: combination wheel decoding, Warded locks, Wafer systems and Disk Detainer mechanics.'])
        schedlist.append(['8:10PM', '9:55PM', 'Workshops + Hackathon', 'June 2019', 'Open participation', 'Talk about and work together on projects! Open Projects include Lockpicking, PWNagotchi, and Nintendo LABO VR Kits!'])
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

