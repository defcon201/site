#!/usr/bin/env python3

class MeetingDetails:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake EXCEPT where triple quotes (""" like this """) appear.
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday, May 15th"
    def Title():		# Title of the meeting
        return "Mind Games"
    def Location():		# Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "Online &mdash; Streaming Live"
    def Notice():		# Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():	# A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-online-meet-up-may-2020-mind-games-d3ff267c3b5f"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "post on our Medium"
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
        May is Mental Health Awareness Month. This month, we're focusing on mental health,
        something that has been getting DDoSed since the start of this Coronavirus pandemic,
        and offering a jam packed meeting with everything from phone phreaking, blue teaming on Wikipedia,
        Capture The Flag challenges and more!
        """
        # Default summary is:
        """<b>More information about this month's meeting is coming soon.</b><br>
        Meeting details are usually confirmed one week in advance of the scheduled meeting date."""


    def Schedule():
        schedstruct = [
            'starttime',	# The scheduled begin time (for example "6:00 PM") or None if no scheduled time (will put "Ending at [time]" if endtime isn't None)
            'endtime',		# The scheduled end time (same format) or None if no scheduled time (will put "Starting at [time]" if starttime isn't None)
            'eventtype',	# The type of event (example choices are: "Intro", "Talk", "Workshop", "Project", "Wrap-Up", "<em>TBA</em>", "Unofficial Ad-Hoc Hours" or something flavorful, or None)
            'title',		# The title of the event in the schedule, or None.
            'speaker',		# The speaker or the subject of the event.
            """summary"""]      # A long-form summary of the event.

        schedtable = []
        schedlist = []

        '''
    Copy the following template to add a new event, filling in the spaces where necessary.

        schedlist.append([
            '12:00AM',
            '12:00AM',
            'Event Type',
            'Event Title',
            'Event Speaker or Subject',
            """This is a summary of the event in question.
            It can span multiple lines"""
            ])

    The following line adds a spacer to the schedule box:
        schedlist.append([None, None, None, None, None, None])

    To add a bold-faced general announcement to the schedule, use this template before the first entry:
        schedlist.append([None, None, None, "Announcement here", None, None])

    To add a notice after a schedule item, use this template after the entry you wish to add a notice to:
        schedlist.append([None, None, None, None, "Notice here", None])

    To add a footnote after the end of the schedule, use this template after the last entry:
        schedlist.append([None, None, None, None, None,
                          """Footnotes and other important information appear here."""])

        '''

        schedlist.append([None, None, None, "DEFCON 201 is now streaming online.", None, "Live Streams are available at:"])
        schedlist.append([None, None, None, None, "Twitch",  '<a href="https://www.twitch.tv/defcon201live">https://www.twitch.tv/defcon201live</a><br>'])
        schedlist.append([None, None, None, None, "dLive",   '<a href="https://dlive.tv/defcon201">https://dlive.tv/defcon201</a><br>'])
        schedlist.append([None, None, None, None, "YouTube", '<a href="https://www.youtube.com/channel/UCYDQaOHbK5trRU2CDgb0qSg">https://www.youtube.com/channel/UCYDQaOHbK5trRU2CDgb0qSg</a><br>'])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([
            '6:15PM',
            '7:00PM',
            'Pre-show',
            'Stalkerware: Solutions for Mitigating its Impact on Privacy and Security',
            'Black Hat Webcast Series',
            """With the sudden and massive shift to users working remotely,
            individuals and businesses are exposed to privacy and security vulnerabilities more than ever.
            Nefarious applications such as stalkerware and spouseware are putting people and enterprises increasingly at risk.<br>

            In this webcast, EFF’s Director of Cybersecurity, Eva Galperin examines her research into the market in stalkerware,
            spouseware, and other nefarious applications that are being deployed to attack our sense of privacy and security.<br>
            
            She will reveal possible activist, technical, and legal approaches to fighting stalkerware
            and give an overview of how the fight is going so far."""
            ])
        schedlist.append([
            '7:00PM',
            '7:05PM',
            'DEFCON 201',
            'Announcements &amp; Code of Conduct review',
            'Sidepocket, GI Jack',
            """DEFCON 201 will start with various updates about our activities in early 2020,
            our post Corona Virus Pandemic measures and an overview of the Code of Conduct linked on our website."""
            ])
        schedlist.append([
            '7:05PM',
            '7:30PM',
            'Talk',
            'Mental Health Hackers: Contents Under Pressure',
            'Amanda Berlin',
            """
            <a href="https://www.mentalhealthhackers.org/">Mental Health Hackers</a> are a group of information security
            professionals passionate about helping others.<br>
            
            Their mission is to educate tech professionals about the unique mental health risks faced by those in our field &mdash;
            and often by the people who we share our lives with &mdash; and provide guidance on reducing their effects
            and better manage the triggering causes.<br>
            
            They also aim at providing support services to those who may be susceptible to related mental health issues
            such as anxiety, depression, social isolation, eating disorders, etc.<br>
            
            In this talk they will explain how they foster conversations about mental health problems in the InfoSec community,
            how they provide support and information to how to recognize, manage, and conquer mental illness, the unique challenges
            and situations faced by the hacker community’s social and work enviroments,
            and how mental health is being exastrubated with the COVID-19 Pandemic."""
            ])
        schedlist.append([
            '7:30PM',
            '7:40PM',
            'Talk',
            'WikiLoop Battlefield',
            'Xinbenlv',
            """
            Originated from Google, Project WikiLoop is an umbrella program for a series of technical projects
            intended to contribute datasets and toolings from the technical industry back to the open knowledge world.<br>
            
            WikiLoop Battlefield is an open-source, crowd-sourced counter vandalism tool for Wikipedia and Wikidata.org.
            Built on web technology, WikiLoop Battlefield allows a quick launch from either desktop or mobile phone without
            needing to install resident software. Its objective is to reduce the barrier for Wikipedians wishing to assist
            in patrolling Wikipedia revisions.<br>
            
            In this DEFCON Group meetup, we will present the WikiLoop Battlefield and give a brief introduction to the
            roadmap of Project WikiLoop overall."""
            ])
        schedlist.append([
            '7:40PM',
            '8:00PM',
            'Mini-Workshop',
            'Hardening Your Face Against COVID-19 With DYI Face Masks',
            'Kira Waszak, Atomic Penguin',
            """
            Thanks to mass panic buying, proper PPE equiment mainly face masks for both medical and civilian personel
            have become harder to find. In this COVID-19 crisis, many are forced to create their own.<br>
            
            In this short video and show & tell, two amazing seamstresses will show off how they made their own
            home made masks that meet PPE standards, one with carbon filters and one that works as a barrier for
            air particles, and how you can obtain them or build them yourself."""
            ])
        schedlist.append([
            '8:00PM',
            '8:30PM',
            'Mini-Workshop',
            'Phreaking Out The Northern Pacific Switched Telecommunications Network',
            'DC4US',
            """
            The Northern Pacific Switched Telecommunications Network is a peer-to-peer VoIP network started in 2018,
            based purely on previous Bell System standards and practices.<br>
            
            It is a very well structured network with real live 24/7 operators and tons of trunks where you can blue box
            till you are blue in the face.<br>
            
            Conceived as an alternative and supplement to C*NET, NPSTN today is a fully-fledged VOIP telephone network for
            phone phreaks and telephone collectors with over 80 members in 10 countries.<br>
            
            This talk will go into detail on how NPSTN is able to connect network-operated coin telephones without
            any major hardware modification to the phone itself, other than just a zip-tie on the coin relay to make
            coins fall straight into the vault instead of waiting in the hopper.<br>
            
            This includes the development of the special asterisk code to detect coin-denomination tones that allows
            anyone to get their payphone on NPSTN to just connect it to a channel bank or VoIP ATA set a few settings on the ATA.<br>
            
            This presentation will conclude into the Open Project segment with a live demo of the NPSTN Coin toll
            ticketing system."""
            ])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([
            '8:30PM',
            None,
            None,
            'Projects &amp; Workshops',
            'Open Participation',
            """Join us online for some neat projects, experiments and workshops by DEFCON 201 members!"""
            ])
        schedlist.append([
            None,
            None,
            'Open Presentation',
            'Hacker Show &amp; Tell',
            None,
            """
            DEFCON 201 members will be given the section immediately after the Lightning Talks to show off
            the various projects that they have been working on.<br>
            
            We have had heads up on some awesome stuff being worked on that will be showing up for the very first time
            so you don’t want to miss this on live-stream!"""
            ])
        schedlist.append([
            None,
            None,
            'Project',
            'Folding@Home VS Coronavirus',
            None,
            """
            Folding@home (FAH or F@h) is a distributed computing project for simulating protein dynamics,
            including the process of protein folding and the movements of proteins implicated in a variety of diseases.<br>
            
            Currently F@h is simulating the dynamics of COVID-19 proteins to hunt for new therapeutic opportunities.
            We want to contribute and you can help! Join the DEFCON 201 Folding@Home Team: 241960"""
            ])
        schedlist.append([
            None,
            None,
            'Project',
            'DEF CON CTF Qualifier 2020',
            None,
            """
            This Friday, starting on May 15th at 8:00 PM EST, we invite all DEFCON 201 Members, Attendees and Fans
            to help us hack the DEF CON CTF Qualifier 2020!<br>
            
            If you are new to Online CTF, we will help you get set up and walk you thorugh some of the challenges.<br>
            
            To learn more about the CTF, please follow this <a href="https://medium.com/@defcon201/defcon-201-online-ctf-practice-challenge-def-con-ctf-2020-qualifier-may-15th-may-17th-8d93c7d49c6d">link.</a>"""
            ])
        schedlist.append([
            None,
            None,
            'Online Games',
            'Jackbox Party Pack 3',
            None,
            """
            During our live-stream, we will be offering to join us in various online games in Jackbox Party Pack 3!<br>
            
            The threequel to the party game phenomenon features the deadly quiz show Trivia Murder Party,
            the say-anything sequel Quiplash 2, the surprising survey game Guesspionage, the t-shirt slugfest Tee K.O.,
            and the sneaky trickster game Fakin’ It.<br>
            
            Use your phones or tablets as controllers, and play with up to 8 players, plus an audience of up to 10,000!"""
            ])

        
        """
        schedlist.append([
            '7:00PM',
            '10:00PM',
            None,
            'DEFCON 201 Meeting',
            None,
            None
            ])
        """
#        schedlist.append([None, None, None, None, "Schedule, speakers and participants are to be determined.", None])

        schedlist.append([None, None, None, None, None, None])
        schedlist.append([None, None, "COVID-19 Notice", "Keep an eye out for your fellow hacker. Whether you're social or anti-social, practice distancing.", None, None])


        for item in schedlist:
            schedtable.append( dict(zip(schedstruct, item)) )
        return schedtable

    def FormattedSchedule():
        schedule = MeetingDetails.Schedule()
        html = ""

        for item in schedule:

            html += "<h5>"

            if item["starttime"] is not None or item["endtime"] is not None:
                if item["starttime"] is not None:
                    if item["endtime"] is None:
                        html += "Starting at "
                    html += item["starttime"]
                if item["starttime"] is not None and item["endtime"] is not None:
                    html += " - "
                if item["endtime"] is not None:
                    if item["starttime"] is None:
                        html += "Ending at "
                    html += item["endtime"]
                html += ": "

            html += "<em>"

            if item["eventtype"] is not None:
                html += item["eventtype"] + ": "

            if item["title"] is not None:
                html += item["title"]

            html += "</em>"

            if item["speaker"] is not None:
                html += " <span style=\"font-weight: 300;\">&nbsp;| " + item["speaker"] + "</span>"

            html += "</h5>\n"

            if item["summary"] is not None:
                html += "<p>" + item["summary"] + "</p>\n"
            else:
                html += "<br>"

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
