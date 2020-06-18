#!/usr/bin/env python3

class MeetingDetails:		# Any of these can be HTML formatted, but I'd recommend against it for semantics sake EXCEPT where triple quotes (""" like this """) appear.
    def Date():			# Date of the meeting (Weekday, Month DD)
        return "Friday, June 19th"
    def Title():		# Title of the meeting
        return "Rainbow tables"
    def Location():		# Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "Online &mdash; Streaming Live"
    def Notice():		# Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():	# A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-online-meet-up-june-2020-rainbow-tables-d78aecfcf8cb?source=friends_link&sk=4f7e34c946c60e79b85ccc217f77713d"
    def LinkName():		# What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "post on our Medium"
    def Summary():		# Short, 1-2 sentences about this meeting.
        return """
        Join Us for the newly declaired DEFCON 201 ANTONMOUS ZONE on Juneteenth as we celebrate Pride as it originally was, a riot!
        We have a great number of talks and special guests representing the LGBTQ+ community, featuring those who are
        hackers that identify as queer. This will also include the usual DEFCON 201 insanity of hacking, drinking,
        eating and being in New Jersey.
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
            '6:00PM',
            '7:00PM',
            'Pre-show',
            'Q&A for Coded Bias',
            'Joy Buolamwini',
            """Coded Bias asks two key questions: what is the impact of Artificial Intelligence’s increasing role in governing 
            our liberties? And what are the consequences for people stuck in the crosshairs due to their race, color, and gender?"""
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
            '7:10PM',
            'Talk',
            'LGBTQIA+ Spotlight:',
            'Tech Learning Collective',
            """
            DEFCON 201 will hilight fellow EFA group, Tech Leanring Collective. They will describe what their operations 
            are like and give a preview of their classes such as their command line workshops, how to use Signal without 
            a phone number, their upcoming Mr. Robot Happy Hacker Hour and adding even lower price tier for attendance to 
            their next “Signal and Surveillance” webinar workshop for People of Color."""
            ])
        schedlist.append([
            '7:10PM',
            '7:50PM',
            'Talk',
            'The Basics of Live Sound: Setup, Acoustical Considerations, EQ and Feedback',
            'Queensiñera',
            """This discussion will cover the basics of a live sound setup and dive into more specifics relating to EQ and 
            Feedback prevention. Practical applications of EQ within examples of confined and non confined spaces go hand in 
            hand with feedback prevention in terms of noting the acoustic design of a given room."""
            ])
        schedlist.append([
            '7:50PM',
            '8:10PM',
            'Talk',
            'Gender Transition As Biohacking',
            'chosystemname',
            """
            A brief look at the biohacking techniques used in gender transition. This will be a Safe For Work talk."""
            ])
        schedlist.append([
            '8:10PM',
            '8:40PM',
            'Talk',
            'Yiff In Hack: DEFCON Furs Presents Fursuits & LEDs',
            'DEFCON Furs, mBlade, SincX',
            """<a href = "https://2020.dcfurs.com/">DEFCON Furs</a> presents two talented Furry Hackers, mBlade & SincX, will talk about how theyadds LEDs and 
            electronics to fursuits. What components he uses and techniques. mBlade will also tell a few stories from 
            his experience at DC26 and what he has planned for the future."""
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
