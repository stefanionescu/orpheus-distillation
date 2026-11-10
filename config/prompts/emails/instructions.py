"""Email prompts: instructions, formatted addresses, confirmations, and long statements and questions."""

from __future__ import annotations

INSTRUCTIONS: list[str] = [
    # LONGER - INSTRUCTIONS
    (
        "When you send the email, make sure to use my work address which is emma at outlook dot com, and please "
        "include the project reference number in the subject line."
    ),
    (
        "If you need to contact me about the proposal, please send an email to david at aol dot com with all the "
        "relevant details, and I'll review it as soon as possible."
    ),
    (
        "You should send your application to the email address info at university dot edu, and make sure to include "
        "all required documents as attachments before the deadline."
    ),
    (
        "When contacting customer support, please send your email to support at service dot co dot uk, and include "
        "your account number and a description of the issue you're experiencing."
    ),
    (
        "If you want to schedule a meeting, please email me at sophia at gmail dot com with your availability, and "
        "I'll check my calendar and get back to you with some options."
    ),
    (
        "Make sure to send the report to james at yahoo dot com by the end of the week, and copy olivia at hotmail dot "
        "com so she's also in the loop."
    ),
    (
        "When you're ready to submit your proposal, send it to william at outlook dot com, and I'll make sure it gets "
        "reviewed by the appropriate committee members."
    ),
    (
        "If you have any questions about the process, feel free to email me at isabella at gmail dot com, and I'll do "
        "my best to provide you with clear and helpful answers."
    ),
    (
        "Please send all payment related inquiries to benjamin at yahoo dot com, and include your invoice number so we "
        "can process your request more efficiently."
    ),
    (
        "When contacting the technical support team, use the email address tech at company dot io, and describe the "
        "problem you're experiencing in as much detail as possible."
    ),
    # EXCLAMATIONS / CASUAL
    "Oh, just email me at john at gmail dot com!",
    "Yeah, send it to sarah at yahoo dot com!",
    "Sure, my email is mike at hotmail dot com!",
    "Just shoot me an email at emma at outlook dot com!",
    "Yeah, it's david at aol dot com!",
    "Perfect, send it to sophia at gmail dot com!",
    "Cool, email me at james at yahoo dot com!",
    "Great, my email is olivia at hotmail dot com!",
    "Awesome, send it to william at outlook dot com!",
    "Yeah, contact me at isabella at gmail dot com!",
    # WITH NAMES / PERSONALIZATION
    "Hi, my email is john dot smith at gmail dot com.",
    "Hello, you can reach me at sarah dot jones at yahoo dot com.",
    "Hey, send it to mike dot brown at hotmail dot com.",
    "Hi there, my email address is emma dot wilson at outlook dot com.",
    "Hello, contact me at david dot davis at aol dot com.",
    "Hey, my email is sophia dot martinez at gmail dot com.",
    "Hi, send it to james dot anderson at yahoo dot com.",
    "Hello there, my email is olivia dot taylor at hotmail dot com.",
    "Hey, contact me at william dot thomas at outlook dot com.",
    "Hi, my address is isabella dot garcia at gmail dot com.",
    # WITH CONTEXT / PURPOSE
    "For job applications, send your resume to careers at company dot com.",
    "If you need technical support, email tech at service dot co dot uk.",
    "For billing questions, contact billing at business dot org.",
    "To report a problem, send an email to support at help dot net.",
    "For media inquiries, contact press at company dot io.",
    "If you want to unsubscribe, email unsubscribe at newsletter dot com.",
    "For partnership opportunities, reach out to partners at business dot co dot uk.",
    "To schedule an appointment, email appointments at service dot org.",
    "For general information, contact info at company dot net.",
    "If you have feedback, send it to feedback at service dot io.",
    "For sales inquiries, email sales at company dot com.",
    "To contact the legal department, send to legal at business dot co dot uk.",
    "For human resources, email hr at company dot org.",
    "If you need help with your account, contact account at service dot net.",
    "For product information, email products at company dot io.",
    # NUMBERS IN EMAILS
    "My email is john123 at gmail dot com.",
    "Send it to sarah2024 at yahoo dot com.",
    "Contact me at mike99 at hotmail dot com.",
    "Email emma456 at outlook dot com.",
    "My address is david789 at aol dot com.",
    "Send to sophia2023 at gmail dot com.",
    "Contact james007 at yahoo dot com.",
    "Email olivia88 at hotmail dot com.",
    "My email is william42 at outlook dot com.",
    "Send it to isabella2024 at gmail dot com.",
    # UNDERSCORES / SPECIAL CHARACTERS
    "My email is john_smith at gmail dot com.",
    "Send it to sarah_jones at yahoo dot com.",
    "Contact mike_brown at hotmail dot com.",
    "Email emma_wilson at outlook dot com.",
    "My address is david_davis at aol dot com.",
    "Send to sophia_martinez at gmail dot com.",
    "Contact james_anderson at yahoo dot com.",
    "Email olivia_taylor at hotmail dot com.",
    "My email is william_thomas at outlook dot com.",
    "Send it to isabella_garcia at gmail dot com.",
    # HYPHENS IN EMAILS
    "My email is john smith at gmail dot com.",
    "Send it to sarah jones at yahoo dot com.",
    "Contact mike brown at hotmail dot com.",
    "Email emma wilson at outlook dot com.",
    "My address is david davis at aol dot com.",
    "Send to sophia martinez at gmail dot com.",
    "Contact james anderson at yahoo dot com.",
    "Email olivia taylor at hotmail dot com.",
    "My email is william thomas at outlook dot com.",
    "Send it to isabella garcia at gmail dot com.",
    # MIXED FORMATS / COMPLEX
    "You can email me at john dot smith dot 2024 at gmail dot com.",
    "Send it to sarah underscore jones at yahoo dot co dot uk.",
    "Contact me at mike dash brown at hotmail dot com.",
    "My email is emma dot wilson underscore 2024 at outlook dot com.",
    "Send to david dot davis dash 99 at aol dot com.",
    "Email sophia underscore martinez dot 2023 at gmail dot com.",
    "Contact james dot anderson dash 007 at yahoo dot com.",
    "My address is olivia underscore taylor dot 88 at hotmail dot com.",
    "Send it to william dot thomas dash 42 at outlook dot com.",
    "Email isabella underscore garcia dot 2024 at gmail dot com.",
    # VERIFICATION / CONFIRMATION
    "Can you confirm that john at gmail dot com is correct?",
    "Is sarah at yahoo dot com the right email address?",
    "Please verify that mike at hotmail dot com is accurate.",
    "Can you double check that emma at outlook dot com is correct?",
    "Is david at aol dot com still your active email?",
    "Can you confirm sophia at gmail dot com for me?",
    "Is james at yahoo dot com the email I should use?",
    "Please verify olivia at hotmail dot com is correct.",
    "Can you confirm william at outlook dot com?",
    "Is isabella at gmail dot com the right address?",
    # URGENT / IMPORTANT
    "Please send this urgently to john at gmail dot com.",
    "This is important, email sarah at yahoo dot com immediately.",
    "Urgent: send to mike at hotmail dot com right away.",
    "This is time sensitive, email emma at outlook dot com now.",
    "Please send this as soon as possible to david at aol dot com.",
    "Urgent matter: contact sophia at gmail dot com immediately.",
    "This is critical, send to james at yahoo dot com right now.",
    "Please email olivia at hotmail dot com urgently.",
    "This is important, contact william at outlook dot com immediately.",
    "Urgent: send to isabella at gmail dot com right away.",
    # ADDITIONAL LONG EXAMPLES - STATEMENTS
    (
        "I've been trying to reach you at jennifer at protonmail dot com for the past week, but my emails keep "
        "bouncing back."
    ),
    (
        "The recruiter asked me to send my updated resume to hiring at techcompany dot io along with a cover letter "
        "and references."
    ),
    (
        "My old email address was compromised, so I've switched to using christopher at fastmail dot com for all my "
        "communications now."
    ),
    (
        "The conference organizers sent the schedule to all attendees at their registered email addresses, so check "
        "your inbox at your work email."
    ),
    (
        "I accidentally sent the confidential document to the wrong email address, so please delete anything you "
        "receive from matthew at company dot org."
    ),
    (
        "The university requires all students to use their official email addresses for academic correspondence, which "
        "ends in dot edu."
    ),
    (
        "I've set up a separate email account for newsletters and promotions so my main inbox at amanda at gmail dot "
        "com stays organized."
    ),
    (
        "The client prefers to communicate via email rather than phone calls, so please send all project updates to "
        "client at business dot com."
    ),
    (
        "My company recently changed email providers, so my new work email is now brandon at newdomain dot io instead "
        "of the old one."
    ),
    (
        "The IT department is migrating all employee email accounts to the cloud, so there might be some disruption to "
        "stephanie at company dot org."
    ),
    (
        "I created a shared email address for the team at projectteam at organization dot com so everyone can access "
        "important messages."
    ),
    (
        "The newsletter subscription confirmation was sent to your email address, so please check your inbox and spam "
        "folder for the verification link."
    ),
    (
        "My personal email is completely different from my work email, so make sure you're sending this to the right "
        "address at victoria dot smith at gmail dot com."
    ),
    (
        "The customer service representative asked me to forward the complaint to escalations at support dot com for "
        "further investigation."
    ),
    (
        "I've been getting a lot of spam emails lately, so I'm considering switching to a more secure email provider "
        "for my personal communications."
    ),
    # ADDITIONAL LONG EXAMPLES - QUESTIONS
    (
        "Could you please confirm whether marketing at company dot com is the correct email address for submitting "
        "press releases and media inquiries?"
    ),
    (
        "Did you receive my email that I sent to your address at robert at yahoo dot com yesterday, or should I resend "
        "it to a different address?"
    ),
    (
        "What email address should I use to contact the department head about the internship program, is it "
        "internships at university dot edu?"
    ),
    (
        "Have you checked your spam folder at your address linda at outlook dot com, because my previous messages "
        "might have been filtered there?"
    ),
    (
        "Is it better to email you at your work address or your personal email at charles dot wilson at gmail dot com "
        "for informal communications?"
    ),
    (
        "Did the confirmation email arrive at your address steven at icloud dot com, or do we need to troubleshoot the "
        "account settings?"
    ),
    (
        "What is the correct format for the company email addresses, is it first name dot last name at company dot com "
        "or something else?"
    ),
    (
        "Could you forward the meeting invitation to everyone on the team, including those who aren't on the usual "
        "distribution list at team at project dot org?"
    ),
    (
        "Did the IT department ever fix the issue with your email account at george at company dot com, or are you "
        "still having trouble receiving messages?"
    ),
    (
        "What email provider do you recommend for business use, and is it more secure than the free options like Gmail "
        "or Yahoo?"
    ),
    (
        "Have you updated your contact information with HR so they have your new email address at helen at newprovider "
        "dot com on file?"
    ),
    (
        "Is the general inquiry email at info at organization dot org monitored regularly, or should I contact a "
        "specific person directly?"
    ),
    (
        "Did you receive the attachment I sent to your email at kevin at company dot net, or was the file too large to "
        "go through?"
    ),
    (
        "What happens to emails sent to my old address at former dot employee at company dot com after I leave the "
        "organization?"
    ),
    (
        "Could you add me to the mailing list at newsletter at community dot org so I can receive updates about "
        "upcoming events?"
    ),
]
