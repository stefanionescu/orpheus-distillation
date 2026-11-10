"""Email prompts: short statements and questions, work, school, and government addresses, and domains."""

from __future__ import annotations

ADDRESSES: list[str] = [
    # SHORT / SIMPLE STATEMENTS
    "My email is john at gmail dot com.",
    "Contact me at sarah at yahoo dot com.",
    "Send it to mike at hotmail dot com.",
    "Email me at emma at outlook dot com.",
    "My address is david at aol dot com.",
    "It's sophia at gmail dot com.",
    "Use james at yahoo dot com.",
    "Send to olivia at hotmail dot com.",
    "Email at william at outlook dot com.",
    "Contact isabella at gmail dot com.",
    "My email is benjamin at yahoo dot com.",
    "Send it to mia at hotmail dot com.",
    "Email lucas at outlook dot com.",
    "Contact charlotte at gmail dot com.",
    "My address is henry at yahoo dot com.",
    "It's amelia at hotmail dot com.",
    "Use alexander at outlook dot com.",
    "Send to harper at gmail dot com.",
    "Email mason at yahoo dot com.",
    "Contact evelyn at hotmail dot com.",
    # QUESTIONS
    "What's your email address?",
    "Can you send me your email?",
    "What email should I use?",
    "Is your email john at gmail dot com?",
    "Do you have an email address?",
    "Can I email you at sarah at yahoo dot com?",
    "What's the email for this?",
    "Should I send it to mike at hotmail dot com?",
    "Is emma at outlook dot com correct?",
    "What's your work email?",
    "Can you confirm your email address?",
    "Is david at aol dot com still active?",
    "What email did you use?",
    "Can I contact you via email?",
    "What's the best email to reach you?",
    "Is sophia at gmail dot com your email?",
    "Do you check james at yahoo dot com?",
    "What's your personal email?",
    "Can you send it to olivia at hotmail dot com?",
    "Is william at outlook dot com correct?",
    # PROFESSIONAL / WORK EMAILS
    "My work email is john dot smith at company dot com.",
    "Send the report to sarah dot jones at business dot co dot uk.",
    "Contact me at michael dot brown at corporate dot org.",
    "Email the team at info at startup dot io.",
    "My professional email is emma dot wilson at tech dot net.",
    "Send it to david dot davis at enterprise dot com.",
    "Contact us at support at service dot co dot uk.",
    "My business email is sophia dot martinez at firm dot org.",
    "Email me at james dot anderson at office dot com.",
    "Send to olivia dot taylor at workplace dot net.",
    "Contact at william dot thomas at company dot io.",
    "My corporate email is isabella dot garcia at business dot com.",
    "Send it to benjamin dot lee at corporate dot co dot uk.",
    "Email mia dot white at professional dot org.",
    "Contact charlotte dot harris at firm dot net.",
    "My work address is henry dot clark at office dot io.",
    "Send to amelia dot lewis at company dot com.",
    "Email alexander dot walker at business dot co dot uk.",
    "Contact harper dot hall at corporate dot org.",
    "My professional email is mason dot allen at tech dot net.",
    # EDUCATIONAL EMAILS
    "My school email is student at university dot edu.",
    "Contact the professor at prof dot smith at college dot edu.",
    "Send it to admin at school dot edu.",
    "Email admissions at university dot co dot uk.",
    "My university email is john dot doe at state dot edu.",
    "Contact the department at dept at college dot edu.",
    "Send to registrar at university dot edu.",
    "Email financial aid at school dot edu.",
    "My college email is sarah dot jones at campus dot edu.",
    "Contact research at university dot co dot uk.",
    "Send it to library at college dot edu.",
    "Email student services at university dot edu.",
    "My academic email is mike dot brown at institute dot edu.",
    "Contact faculty at college dot edu.",
    "Send to graduate at university dot edu.",
    "Email undergraduate at school dot edu.",
    "My student email is emma dot wilson at university dot co dot uk.",
    "Contact alumni at college dot edu.",
    "Send it to career services at university dot edu.",
    "Email housing at school dot edu.",
    # GOVERNMENT / OFFICIAL EMAILS
    "Contact the office at info at government dot gov.",
    "Send it to public at agency dot gov.",
    "Email inquiries at department dot gov dot uk.",
    "My official email is citizen at service dot gov.",
    "Contact support at agency dot gov.",
    "Send to contact at department dot gov dot uk.",
    "Email help at government dot gov.",
    "My government email is official at agency dot gov.",
    "Contact information at department dot gov dot uk.",
    "Send it to public service at government dot gov.",
    "Email citizen services at agency dot gov dot uk.",
    "My agency email is contact at department dot gov.",
    "Send to public information at government dot gov dot uk.",
    "Email services at agency dot gov.",
    "Contact the department at info at government dot gov dot uk.",
    # VARIOUS DOMAINS - .COM
    "Email me at john at example dot com.",
    "Send it to sarah at test dot com.",
    "Contact mike at sample dot com.",
    "My email is emma at demo dot com.",
    "Use david at website dot com.",
    "Send to sophia at online dot com.",
    "Email james at internet dot com.",
    "Contact olivia at web dot com.",
    "My address is william at site dot com.",
    "Send it to isabella at portal dot com.",
    # VARIOUS DOMAINS - .CO.UK
    "My email is john at example dot co dot uk.",
    "Contact me at sarah at business dot co dot uk.",
    "Send it to mike at service dot co dot uk.",
    "Email emma at company dot co dot uk.",
    "My address is david at office dot co dot uk.",
    "Send to sophia at professional dot co dot uk.",
    "Contact james at corporate dot co dot uk.",
    "Email olivia at enterprise dot co dot uk.",
    "My email is william at firm dot co dot uk.",
    "Send it to isabella at organization dot co dot uk.",
    # VARIOUS DOMAINS - .ORG
    "Contact us at info at nonprofit dot org.",
    "Send it to support at charity dot org.",
    "Email contact at foundation dot org.",
    "My email is john at organization dot org.",
    "Send to sarah at association dot org.",
    "Contact mike at society dot org.",
    "Email emma at institute dot org.",
    "My address is david at group dot org.",
    "Send it to sophia at network dot org.",
    "Contact james at alliance dot org.",
    # VARIOUS DOMAINS - .NET
    "My email is john at example dot net.",
    "Contact me at sarah at service dot net.",
    "Send it to mike at network dot net.",
    "Email emma at online dot net.",
    "My address is david at internet dot net.",
    "Send to sophia at web dot net.",
    "Contact james at portal dot net.",
    "Email olivia at site dot net.",
    "My email is william at platform dot net.",
    "Send it to isabella at system dot net.",
    # VARIOUS DOMAINS - .IO
    "Email me at john at startup dot io.",
    "Send it to sarah at tech dot io.",
    "Contact mike at app dot io.",
    "My email is emma at digital dot io.",
    "Use david at cloud dot io.",
    "Send to sophia at data dot io.",
    "Email james at code dot io.",
    "Contact olivia at dev dot io.",
    "My address is william at software dot io.",
    "Send it to isabella at platform dot io.",
    # VARIOUS DOMAINS - .EDU
    "My school email is john at university dot edu.",
    "Contact me at sarah at college dot edu.",
    "Send it to mike at school dot edu.",
    "Email emma at institute dot edu.",
    "My address is david at academy dot edu.",
    "Send to sophia at campus dot edu.",
    "Contact james at education dot edu.",
    "Email olivia at learning dot edu.",
    "My email is william at academic dot edu.",
    "Send it to isabella at student dot edu.",
    # VARIOUS DOMAINS - .GOV / .GOV.UK
    "Contact the office at info at agency dot gov.",
    "Send it to public at department dot gov dot uk.",
    "Email inquiries at service dot gov.",
    "My official email is citizen at agency dot gov dot uk.",
    "Contact support at government dot gov.",
    "Email help at agency dot gov.",
    "My government email is official at service dot gov dot uk.",
    "Contact information at department dot gov.",
    "Send it to public service at agency dot gov dot uk.",
    # VARIOUS DOMAINS - OTHER EXTENSIONS
    "My email is john at example dot ca.",
    "Contact me at sarah at business dot au.",
    "Send it to mike at company dot de.",
    "Email emma at service dot fr.",
    "My address is david at office dot jp.",
    "Send to sophia at tech dot in.",
    "Contact james at corporate dot br.",
    "Email olivia at firm dot mx.",
    "My email is william at company dot sg.",
    "Send it to isabella at business dot nz.",
    "Contact mike at service dot se.",
    "Email emma at office dot no.",
    "My address is david at tech dot dk.",
    "Send to sophia at company dot fi.",
    "Contact james at business dot nl.",
    # LONGER - STATEMENTS
    (
        "You can reach me at my personal email address, which is john dot smith at gmail dot com, and I usually check "
        "it several times throughout the day."
    ),
    (
        "If you need to contact me for business matters, please send an email to sarah dot jones at company dot co dot "
        "uk, and I'll get back to you within twenty four hours."
    ),
    (
        "My work email address is michael dot brown at corporate dot org, and that's the best way to reach me during "
        "business hours from Monday through Friday."
    ),
    (
        "Feel free to email me at emma dot wilson at tech dot net if you have any questions about the project, and "
        "I'll do my best to respond as quickly as possible."
    ),
    (
        "You can send the documents to david dot davis at enterprise dot com, and make sure to include your name and "
        "reference number in the subject line."
    ),
    (
        "If you're interested in learning more about our services, please contact us at info at startup dot io, and "
        "one of our team members will get back to you soon."
    ),
    (
        "My professional email address is sophia dot martinez at firm dot org, and I'm available to answer any "
        "questions you might have about our consulting services."
    ),
    (
        "You can reach the customer service team by sending an email to support at service dot co dot uk, and they "
        "typically respond within a few hours during business days."
    ),
    (
        "If you need to get in touch with me urgently, my email is james dot anderson at office dot com, and I'll make "
        "sure to prioritize your message."
    ),
    (
        "Please send all conference related inquiries to olivia dot taylor at workplace dot net, and we'll make sure "
        "to include you in all the important updates."
    ),
    # LONGER - QUESTIONS
    (
        "Can you send me your email address so I can add you to the distribution list for our weekly newsletter and "
        "project updates?"
    ),
    (
        "What email address should I use to send you the contract documents, and do you prefer to receive them as "
        "attachments or through a secure file sharing service?"
    ),
    (
        "Is john dot smith at gmail dot com still your current email address, or have you switched to a different one "
        "since we last communicated?"
    ),
    (
        "Could you please confirm which email address you'd like me to use for official correspondence, because I want "
        "to make sure I'm sending everything to the right place?"
    ),
    (
        "Do you have a work email address that I should use for business related matters, or would you prefer I "
        "contact you at your personal email instead?"
    ),
    (
        "What's the best email address to reach you at, and what time of day do you typically check your messages so I "
        "know when to expect a response?"
    ),
    (
        "Can I email you at sarah at yahoo dot com with the details about the meeting, or would you prefer I use a "
        "different email address for this communication?"
    ),
    (
        "Is mike at hotmail dot com the correct email address for sending you the invoice, and should I also send a "
        "copy to your accounting department?"
    ),
    (
        "What email address should I use to send you the presentation slides, and do you need them in a specific "
        "format or can I send them as a PDF attachment?"
    ),
    (
        "Could you provide me with your email address so I can forward you the information about the upcoming event "
        "and add you to our guest list?"
    ),
]
