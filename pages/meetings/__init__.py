#!/usr/bin/env python3

class MeetingDetails:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake.
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday, April 17th"
    def Title():		# Title of the meeting
        return "Compile Farm"
    def Location():		# Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "ONLINE [SEE LINK]"
    def Notice():		# Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():	# A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-online-meet-up-april-2020-compile-farm-ad1e07acb6f5?sk=44919e5c5c42f768ef66fe49ab72de4f"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "Medium:"
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
        Join DEFCON 201 Online via Zoom or broacasted on Twitch, dLive or youtube on Friday, April 17th starting at 7:00 PM EST [6:30 PM EST PRE-SHOW] to learn about agricultural and environmentally friendly hacking techniques! <h2><a href="https://stats.foldingathome.org/team/241960">Join the DEFCON 201 Folding@Home Team: 241960</a></h2>"""
    def Schedule():
        schedstruct = ['starttime', 'endtime', 'eventtype', 'title', 'speaker', 'summary']
        schedtable = []
        schedlist = []
        schedlist.append(['6:20PM', '7:00PM', 'PRE-MEETING HACKER EDUTAINMENT', 'Online Que', 'DEFCON 201 Members', 'To give time to make sure everyone is watching our LiveStream and logging into our LiveStream chat, DEFCON 201 will be showing various videos that relates to our meeting theme.'])
        schedlist.append(['7:00PM', '7:05PM', 'DEFCON 201 Annoucements & Code of Conduct',  'GI Jack & Sidpocket', 'DEFCON 201', 'DEFCON 201 will start with various updates about our activities in early 2020 and an overview of the Code of Conduct linked on our website.'])
        schedlist.append(['7:05PM', '7:15PM', 'Empowering a New Local Food System in Urban Environments',  'Mary Wetherill & Electra Jarvis', 'Mary and Electra of Green Food Solutions, will discuss how they are empowering a new local food system, and how you can grow food practically anywhere that has access to electricity and water. They will also give a live demo of their home growing Tower.'])
        schedlist.append(['7:15PM', '7:25PM', 'Printing Green: An Ecological Cryptocurrency Future',  'BitGreen Foundation', 'Workshop', 'In this talk, the BitGreen Foundation will go over their future goals on the BitGreen project to fund energy efficient and tech activism, how their Proof Of Stake mining method differs from other cryptocurrencies and how to set up your own Master Node directly from the BitGreen Wallet to mine BitGreen on any hardware.'])
        schedlist.append(['7:25PM', '7:30PM', 'About Rural Tech Fund', 'Chris Sanders', 'Charity PSA', 'The Rural Technology Fund (RTF) recognizes the very real “digital divide” between rural and non-rural areas.'])
        schedlist.append(['7:30PM', '???', 'Open Workshops Projects', 'Drinking + Games', 'Open participation', 'Join us in the Zoom Chat (email us for access) for our Hacker Show & Tell, Jackbox Party Games, Drinking Alcohol and Juice and 1337 converstations while we lose our minds in isolation!'])
        schedlist.append(['Bonus', 'CTF', 'April 17th - April 19th', 'PladCTF', 'https://discord.gg/PGgPNEF', 'If you are new to Online CTF, we will help you get set up and walk you thorugh some of the challenges: https://plaidctf.com/'])
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

