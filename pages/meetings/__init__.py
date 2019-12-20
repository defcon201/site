#!/usr/bin/env python3

class MeetingDetails:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake.
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday, December 20th"
    def Title():		# Title of the meeting
        return "HoHoCon Part Deux"
    def Location():		# Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "SUBCULTURE Jersey City, 260 Newark Ave."
    def Notice():		# Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():	# A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-meet-up-december-2019-hohocon-part-deux-906ee4a1bee9"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "Medium:"
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
        Join #DEFCON201 at SubCulture (260 Newark Ave, Jersey City NJ) on Friday, December 20th from 7pm - 10pm to watch Mr. Robot, share gifts, listen to Hacker Rants, Nintendo Labo, justCTF, lockpicking and more!"""
    def Schedule():
        schedstruct = ['starttime', 'endtime', 'eventtype', 'title', 'speaker', 'summary']
        schedtable = []
        schedlist = []
        schedlist.append(['7:00PM', '7:55PM', 'Workshops', 'Meet &amp; Greet + Mr. Robot Screening', 'Open participation', 'Chat amongst friends and work together on projects, watch Mr. Robot Episode 405 Method Not Allowed, learn lockpicking, compete in justCTF and warm up for the talks!'])
        schedlist.append(['7:55PM', '8:00PM', 'A Sneak Peak Of DEFCON 201 In 2020',  'Sidepocket & GI Jack', 'DEFCON 201', 'In this talk, join our Co-Founders at a sneak peak into our bright feature and how the Dirty Jersey smell is about to embark it’s foul hacker stank nationwide!'])
        schedlist.append(['8:00PM', '8:10PM', '<em>Secret Hacker Santa Swap</em>',  'DEFCON 201 Attendees', 'DEFCON 201', 'Bring out your inexpensive ($15 or Under) hacker gifts for our first evenr Secret Hacker Santa Swap! It’s like a White Elephant or Yankie Swap…but with 1337 Haxxors!'])
        schedlist.append(['8:10PM', '9:55PM', '<em>The Hacker Rant To End All Hacker Rants</em>', 'NCommander', 'Talk', 'In this talk, we have given nearly two hours for our long time recurring speaker to rant about so many technology, community and Information Security topics that would take a novel to list!'])
        schedlist.append(['9:55PM', '10:00PM', 'Wrap-Up', 'Official end of meeting', 'Good night!', '<em>Note: SUBCULTURE closes at 10pm. Please make sure your belongings are together before closing time.'])
        schedlist.append(['10:00PM', 'zzz', 'Unofficial Ad-Hoc Hours', 'Downtown JC', 'Who\'s up?', 'We may decide to regroup at a local late night venue such as a diner or bar afterwards; this is ad-hoc and entirely unregulated airspace. Participate at your own risk! All participants of the justCTF will continue online until December 22nd at 4:00 AM.'])
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

