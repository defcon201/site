#!/usr/bin/env python3

class MeetingDetails:           # Any of these can be HTML formatted, but I'd recommend against it for semantics sake EXCEPT where triple quotes (""" like this """) appear.
    def Date():                 # Date of the meeting (Weekday, Month DD)
        return "Friday, September 18th"
    def Title():                # Title of the meeting
        return "Egg Freckles"
    def Location():             # Location of the meeting (as of spring 2019, "SUBCULTURE Jersey City, 260 Newark Ave.")
        return "Online &mdash; Streaming Live + <em>Limited seating</em> @ SubCulture, 260 Newark Ave., Jersey City"
    def Notice():               # Any important notices about the meeting or the information.
        return ""
    def CanonicalLink():        # A link that refers to this meeting
        return "https://medium.com/@defcon201/defcon-201-online-meet-up-september-2020-egg-freckles-a369f0d3a02b"
    def LinkName():             # What this link refers to (for instance "post on our Medium", "forum post", "tweet", "Meetup event")
        return "post on our Medium"
    def Summary():              # Short, 1-2 sentences about this meeting.
        return """We have decided to take this golden oprotunity to have a DCG 201 meeting theme we have wanted to do for a very long time: Hacking Apple."""

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

        schedlist.append([None, None, None, None, None, None])

        schedlist.append([
            '4:00PM',
            '4:50PM',
            '(Online) Pre-show',
            'Steve Wozniak Keynote (2004)',
            'at The Fifth HOPE Conference',
            """Lets take a trip back down memory lane with a limited reairing of the
            historic (yet forgotten about) keynote from The Fifth HOPE (Hackers On Planet Earth)
            with Apple Co-Founder and guy who actually did all the work; The Wonderful Wizard Of Woz!"""
            ])

        schedlist.append([
            '4:00PM',
            '4:50PM',
            '(IRL) Intro',
            'Meet &amp Greet',
            'DEFCON 201 members',
            """Chat amongst friends, coordinate your public key portfolio, add cards to your Rolodex&trade;, and warm up for the talks!"""
            ])

        schedlist.append([
            '4:50PM',
            '5:00PM',
            'Lightning Talk',
            'A Marathon Of Mac Gaming',
            'MrMacRight',
            """In this talk, MrMacRight will go over how Apple is pushing AAA gaming on their platforms and improving In-App purchases."""
            ])

        schedlist.append([
            '5:00PM',
            '6:00PM',
            'Talk',
            'The Rise Of Mac Malware',
            'Thomas Reed',
            """Join me for a journey through time, as we look at past Mac malware, focusing on when certain behaviors first emerged.
            Then fast forward through time, where we’ll see what today’s Mac threat landscape looks like, and what behaviors we’re seeing from Mac threats in the wild."""
            ])

        schedlist.append([
            '6:00PM',
            '7:00PM',
            'Talk',
            'Abusing & Securing XPC in macOS Apps',
            'Wojciech',
            """XPC is a well-known interprocess communication mechanism used on Apple devices.
            Abusing XPC led to many severe bugs, including those used in jailbreaks.
            While the XPC bugs in Apple’s components are harder and harder to exploit, did we look at non-Apple apps on macOS?
            As it turns out, vulnerable apps are everywhere — Anti Viruses, Messengers, Privacy tools, Firewalls, and more."""
            ])

        schedlist.append([
            '7:00PM',
            '7:30PM',
            'Workshop',
            'macintosh.js',
            'Ncommander',
            """Macintosh.js is an Electron app which emulates a 1991 Macintosh Quadra 900 running Mac OS 8.1.
            In this brief overview, NCommander of HACK + ALT + NCOMMANDER fame will do what he does best;
            dissect this retro operating system and point out the quirks and WTF-ness of this unholy emulated beast."""
            ])

        schedlist.append([
            '7:30PM',
            '8:00PM',
            'Workshop',
            'A Kinky Hack To Sideload iOS Applications',
            'sidepocket',
            """we will walk through how the kink and fetish scene had exploited the development mode of iOS and XCode to inject their own software,
            bypassing Apple’s insular storefront. Then we will quickly go over how this blew a giant wall in Apple’s iOS software approval proccess."""
            ])

        schedlist.append([
            '8:00PM',
            None,
            'Finishing remarks',
            'Old Man Yells At iCloud',
            'xio',
            """This rant on Apple products past and present will be so long and so foul that it will end and only end when Sub Culture
            shuts the place down and our livestream ends! Plus, comments from the peanut gallery will cause this digital caveman to go
            into cardiac arrest before the #FailFactory he works at does!"""
            ])
        schedlist.append([
            None,
            '9:00PM',
            '(IRL) Wrap-Up',
            'Official end of in-person meeting',
            'Good night!',
            '<em>Note: SUBCULTURE closes early due to COVID-19 regulations. Please make sure your belongings are together before closing time.</em>'])

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
