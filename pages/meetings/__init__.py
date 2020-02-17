#!/usr/bin/env python3

class MeetingDetails:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake.
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday, February 21st"
    def Title():		# Title of the meeting
        return "Hackers Lonely Hearts Club"
    def Location():		# Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "SUBCULTURE Jersey City, 260 Newark Ave."
    def Notice():		# Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():	# A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-meet-up-february-2020-hackers-lonely-hearts-club-1edbe21f6de0"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "Medium:"
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
        Join #DEFCON201 at SubCulture (260 Newark Ave, Jersey City NJ) on Friday, February 21st from 7pm - 10pm to learn Software Defined Radio, hack IoT devices, build a Pi-Hole, share stories of Shmoocon, lockpicking and more!"""
    def Schedule():
        schedstruct = ['starttime', 'endtime', 'eventtype', 'title', 'speaker', 'summary']
        schedtable = []
        schedlist = []
        schedlist.append(['7:00PM', '7:45PM', 'Intro', 'Meet &amp; Greet', 'DEFCON 201 members', 'Chat amongst friends, coordinate your public key portfolio, add cards to your Rolodex&trade;, and warm up for the talks!'])
        schedlist.append(['7:45PM', '7:50PM', 'DEFCON 201 Annoucements & Code of Conduct',  'GI Jack & Sidpocket', 'DEFCON 201', 'DEFCON 201 will start with various updates about our activities in early 2020 and an overview of the Code of Conduct linked on our website.'])
        schedlist.append(['7:50PM', '8:00PM', '<em>Why Pick Up “Artists” Are A Scam; A Social Engineer’s Perspective</em>',  'Sidepocket', 'DEFCON 201', 'In this talk, our speaker with disect various Pick Up Artist techniques and demonstrate why these techinques do not work, the pyschological damage they cause, the bizzaro culture around this study and who it’s actually designed to social engineer. This talk will be prefaced by a TRIGGER WARNING as topics such as sexual harassment and stalking will be touched upon.'])
        schedlist.append(['8:00PM', '8:45PM', '<em>An Introduction to Iot Pentetration Testing</em>',  'Libertyunix', 'DEFCON 201', 'In this talk we will explore the basic principles of IoT PenTesting, how to build an effective toolset, reverse engineering, and analyzing wireless signals with software defined radio.'])
        schedlist.append(['8:45PM', '9:55PM', 'Workshops + Projects', 'Feburary 2020', 'Open participation', 'Talk about and work together on projects! Open Projects include Lockpicking, PWNagotchi, Pi-Hole, and preparing for PAX East! We also encourage to bring your own!'])
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

