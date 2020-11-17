#!/usr/bin/env python3

class MeetingDetails:           # Any of these can be HTML formatted, but I'd recommend against it for semantics sake EXCEPT where triple quotes (""" like this """) appear.
    def Date():                 # Date of the meeting (Weekday, Month DD)
        return "Friday, November 20th"
    def Title():                # Title of the meeting
        return "BackOrifice 2020"
    def Location():             # Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "Online &mdash; Streaming Live"
    def Notice():               # Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():        # A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-online-meet-up-november-2020-back-orifice-2020-19296967cac4"
    def LinkName():             # What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "post on our Medium"
    def Summary():              # Short, 1-2 sentences about this meeting.
        return """
To get our freak on, we decided after high demand to revisit virually one of our favorite meeting subjects of all time back in 2017 when we started out. Hacking Sex. Wet ware meets hardware. Dicks, Dongles and The Internet Of Thongs.
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

        schedlist.append([None, None, None, "DEFCON 201 is streaming online.", None, "Live Streams are available at:"])
        schedlist.append([None, None, None, None, "Twitch",  '<a href="https://www.twitch.tv/defcon201live">https://www.twitch.tv/defcon201live</a><br>'])
        schedlist.append([None, None, None, None, "dLive",   '<a href="https://dlive.tv/defcon201">https://dlive.tv/defcon201</a><br>'])
        schedlist.append([None, None, None, None, "YouTube", '<a href="https://www.youtube.com/channel/UCYDQaOHbK5trRU2CDgb0qSg">https://www.youtube.com/channel/UCYDQaOHbK5trRU2CDgb0qSg</a><br>'])
        schedlist.append([None, None, None, None, "Chaturbate", '<em>Link to our Chaturbate stream will be announced soon.</em>'])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([None, None, "This month's charity fundraiser is", """<a href="https://www.rainn.org/">RAINN</a>""", "the Rape, Abuse &amp Incest National Network", """
RAINN is the nation’s largest anti-sexual violence organization.<br>
RAINN created and operates the National Sexual Assault Hotline (800.656.HOPE, online.rainn.org y rainn.org/es) in partnership with more than 1,000 local sexual assault service providers across the country,<br>
and operates the DoD Safe Helpline for the Department of Defense. RAINN also carries out programs to prevent sexual violence, help survivors, and ensure that perpetrators are brought to justice.<br><br>

This month until November 30th, DEFCON 201 are proud to try to raise a minimum goal of <b>$400</b> for RAINN via Tiltify to protect all humans around the world from the horrors of sexual abuse.<br>
We will offer a wide range of programming from our shows (HACK + ALT + NCOMMANDER, The Master Of Unlocking, Archvile: A Linux Perspective & Crypto Barons) plus special programming including this meeting
on our LIVE Stream platforms to entertain people to donate to the cause!
"""])
        schedlist.append([None, None, None, "If you want to donate at any time, do so through the following link:", """<a href="https://tiltify.com/@defcon201live/defcon-201-makes-it-rainn-november-charity">Tiltify: DEFCON 201 Makes It RAINN November Charity</a>""", None])



        schedlist.append([
            '6:00PM',
            '6:25PM',
            'Pre-show',
            'Pwn All the Mobile Porn Apps',
            'Ben Actis',
            """A talk from <a href="https://www.bsideslv.org/">BSides Las Vegas 2017</a>.
               It will examine egregious security vulnerabilities found in adult content mobile applications.
               Highlights include: lack of HTTPS usage, code execution in update mechanisms, and less then stellar vendor responses."""
            ])

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([
            '6:30PM',
            '6:50PM',
            'Talk',
            'The Privacy of Online Dating & Teledildonics',
            'Alex Lomas',
            """Many dating applications use location to match you up with people in the local area, but this led to the leakage of million’s of people’s exact location.
               We’ll look at some of the problems we found last year, what has changed, and what you can do to protect yourself."""
            ])

        schedlist.append([
            '6:50PM',
            '7:00PM',
            'Brief',
            'B!tch Picking: Designing A Lockpick Set For Sex Workers',
            'Sidepocket',
            """In this short presentation, a member of <a href="https://toool.us/">TOOOL</a> will pitch a concept of an all-in-one case and set design
               that would satisfy the needs for the safety of sex workers out in the field."""
            ])

        schedlist.append([
            '7:00PM',
            '7:30PM',
            'Talk',
            'Naked &amp; Unafraid: The Basics Of Securing Your Nudes',
            'Allie Barnes',
            """This talk aims to give you some basic information on revenge porn, some basic technical information on
               privacy when it comes to media storage and sharing, how to protect yourself when sharing intimate material,
               and finally — what your options are if your material DOES get leaked."""
            ])

        schedlist.append([
            '7:30PM',
            '7:50PM',
            'Talk',
            'Aliases, Branding, and Consent: The ABCs of Sex Work and Digital Security',
            'Luna Sylum',
            """Let’s define your model of acceptable risk, when it comes to social media and information security, if you maintain more than one identity online."""
            ])

        schedlist.append([
            '7:50PM',
            '8:00PM',
            'Breaking News Brief',
            '<em>To be announced.</em>',
            None,
            ""
           ])

        schedlist.append([
            '8:00PM',
            '8:30PM',
            'Talk',
            'The Internet Of Thongs: Virtualization Of Sexual Intimacy',
            'Andre Shakti, Inferno',
            """We look at two organizations, The Sanctuary Club and NYC INFERNO, as they talked about the challenges of
               transforming their intimate spaces into the virtual world."""
            ])

        schedlist.append([
            '8:30PM',
            '10:00PM',
            'Roundtable',
            'UN-EARN IT: The Domino Effect Of Internet Censorship',
            'Sex Workers Roundtable (Participants TBA)',
            """Join a panel of sex workers and activist on the front lines about the censorship of sex work on the internet
               and how it will and has emboldened other forms internet censorship that affects us all."""
            ])


        schedlist.append([None, None, None, None, None, None])

        schedlist.append([
            None,
            '12:00 at the latest',
            'Sign-Off',
            'Good night!',
            'End of program.',
            '<em>Note: Twitch Viewers will Raid another Stream, dLive Watchers will earn LEMONS!</em>'])

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
                html += "<u>" + item["eventtype"] + ":</u> "

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
