"""Abbreviation prompts: longer sentences with company, technical, medical, brand, and government abbreviations."""

from __future__ import annotations

SENTENCES: list[str] = [
    # LONGER - STATEMENTS
    "I need you to send that report ASAP, because the deadline is tomorrow and we can't afford any delays.",
    (
        "FYI, the meeting has been moved to next week, so make sure to update your calendar and let everyone know "
        "about the change."
    ),
    (
        "Please RSVP by Friday if you're planning to attend the event, because we need to give the caterer a final "
        "headcount."
    ),
    "BTW, I saw that article you mentioned, and I think it's really interesting how they're approaching that problem.",
    (
        "I'll send you the document EOD, which means you should have it in your inbox by the end of the business day "
        "today."
    ),
    "The location for the conference is still TBD, but we're hoping to finalize it by the end of this week.",
    (
        "Before you ask me any questions, please check the FAQ section on our website, because most common questions "
        "are answered there."
    ),
    "I decided to do it DIY instead of hiring someone, because I wanted to save money and learn how to do it myself.",
    (
        "I've been managing my ADHD with medication and therapy, and it's made a huge difference in my daily life and "
        "productivity."
    ),
    (
        "She just completed her PhD in neuroscience, and she's planning to do postdoctoral research at a prestigious "
        "university."
    ),
    # LONGER - QUESTIONS
    (
        "Can you send me that file ASAP, because I need it for the presentation tomorrow morning and I don't want to "
        "be scrambling at the last minute?"
    ),
    (
        "FYI, did you know that the meeting has been rescheduled, and I wanted to make sure you were aware of the new "
        "time and location?"
    ),
    (
        "Have you RSVP'd to the event yet, because I'm trying to figure out if we should carpool together or meet "
        "there separately?"
    ),
    (
        "BTW, did you see that news article about the company merger, and what do you think it means for our "
        "department and our jobs?"
    ),
    (
        "Can you get that report to me EOD, because I have a meeting first thing tomorrow morning where I need to "
        "present those findings?"
    ),
    (
        "Is the venue still TBD for the conference, because I'm trying to book my hotel and flights and I need to know "
        "the location?"
    ),
    (
        "Have you checked the FAQ section on the website, because I'm getting a lot of questions that are already "
        "answered there and it would save everyone time?"
    ),
    (
        "Are you planning to do it DIY or hire a professional, because I've done similar projects before and I could "
        "give you some advice either way?"
    ),
    (
        "How have you been managing your ADHD, because I know someone who was recently diagnosed and they're looking "
        "for strategies and support?"
    ),
    (
        "What was her PhD dissertation about, because I'm really interested in neuroscience and I'd love to learn more "
        "about her research?"
    ),
    # LONGER - WITH COMPANIES
    (
        "I've been working at IBM for the past five years, and I really enjoy the challenging projects and the "
        "collaborative work environment."
    ),
    (
        "She works for NASA as a research scientist, and she's currently involved in a mission to study the atmosphere "
        "of Mars."
    ),
    "He's been with the FBI for over a decade, and he specializes in cybercrime investigations and digital forensics.",
    (
        "They work at the CIA analyzing intelligence reports, and their work is classified so they can't discuss the "
        "details with anyone."
    ),
    "I saw the breaking news on CNN this morning, and it's really concerning how quickly the situation is developing.",
    (
        "Check BBC News for the latest updates, because they have excellent international coverage and reliable "
        "reporting on global events."
    ),
    (
        "It's going to be on ABC tonight at eight o'clock, and I've been looking forward to watching this documentary "
        "for weeks."
    ),
    (
        "Watch NBC tonight for the special report, because they're doing an in depth investigation into the story "
        "that's been making headlines."
    ),
    (
        "I use Google for almost everything, from searching for information to managing my email and calendar, and "
        "it's become essential to my daily routine."
    ),
    "She has an iPhone and she loves how seamlessly it integrates with all her other Apple devices and the ecosystem.",
    # LONGER - TECHNICAL
    (
        "The API is currently down for maintenance, so we won't be able to process any requests until they finish "
        "updating the system."
    ),
    (
        "Check the URL first to make sure it's correct, because if there's a typo in the address it won't load the "
        "page you're looking for."
    ),
    (
        "Make sure the website is using HTTPS instead of HTTP, because that ensures your connection is secure and your "
        "data is encrypted."
    ),
    (
        "The HTML looks good overall, but we might need to make some adjustments to the CSS to improve the styling and "
        "layout."
    ),
    (
        "Update the CSS to match the new design specifications, and make sure all the colors and fonts are consistent "
        "throughout the site."
    ),
    (
        "Check the DNS settings to see if there's an issue with the domain name resolution, because that could be why "
        "the site isn't loading."
    ),
    (
        "The IP address you provided is incorrect, so the server can't establish a connection and that's why the "
        "transfer failed."
    ),
    (
        "It's a JSON file that contains all the configuration data, and you'll need to parse it to extract the "
        "information you need."
    ),
    (
        "Send it as a PDF so everyone can open it regardless of what software they're using, and it will preserve the "
        "formatting."
    ),
    (
        "Open the DOC file in Microsoft Word, and make sure you have the latest version so all the features work "
        "correctly."
    ),
    # LONGER - MEDICAL
    (
        "I've been managing my ADHD with a combination of medication and therapy, and it's made such a difference in "
        "my ability to focus and stay organized."
    ),
    (
        "She was diagnosed with PTSD after serving in the military, and she's been working with a therapist to process "
        "the trauma and develop coping strategies."
    ),
    (
        "He's been dealing with OCD for most of his life, and he's found that cognitive behavioral therapy has been "
        "really helpful in managing his symptoms."
    ),
    (
        "They tested positive for COVID last week, so they're isolating at home and monitoring their symptoms while "
        "they wait for the results to improve."
    ),
    (
        "Check your BMI to see if you're in a healthy range, but remember that it's just one indicator and doesn't "
        "tell the whole story about your health."
    ),
    (
        "The ER is really busy tonight, so if it's not an emergency you might want to consider going to an urgent care "
        "center instead."
    ),
    (
        "Go to the ICU immediately if his condition worsens, because they have the specialized equipment and staff "
        "needed to provide intensive care."
    ),
    (
        "She's an RN who works in the pediatric unit, and she's really passionate about helping children and their "
        "families during difficult times."
    ),
    (
        "He's a doctor with an MD degree, and he specializes in cardiology so he focuses on heart related conditions "
        "and treatments."
    ),
    (
        "They work at the CDC tracking disease outbreaks, and their research helps inform public health policies and "
        "recommendations."
    ),
    # EXCLAMATIONS - LONGER
    "Send it ASAP, because this is urgent and we can't afford to wait any longer!",
    "FYI, that's absolutely incredible news, and I'm so excited to hear about your promotion!",
    "OMG, did you see what happened on the news, because I can't believe how quickly things are changing!",
    "LOL, that's the funniest thing I've heard all week, and I'm still laughing about it!",
    "BTW, that's an amazing idea, and I think we should definitely pursue it!",
    "Wow, NASA is doing such incredible work, and I'm so inspired by what they're accomplishing!",
    "Amazing, it's using HTTPS now, which means the connection is secure and your data is protected!",
    "Great, send it EOD, and I'll make sure to review it first thing tomorrow morning!",
    "Perfect, check the FAQ first, because that will save you time and answer most of your questions!",
    "Awesome, it's DIY, which means you'll learn a lot and save money at the same time!",
    # MIXED ABBREVIATIONS IN SENTENCES
    "Send the PDF ASAP to the CEO via email.",
    "FYI, the CFO needs the report EOD.",
    "RSVP to the event and check the FAQ.",
    "BTW, the API is down, so use HTTPS.",
    "The CEO and CFO are meeting with the CTO.",
    "She has a PhD and works at NASA.",
    "He's an MD with ADHD, working in the ER.",
    "Check the URL, it should be HTTPS, not HTTP.",
    "The HTML and CSS need updates for the API.",
    "Send it as a PDF or DOC file ASAP.",
    "The CEO at IBM has an MBA from Harvard.",
    "She's an RN working in the ICU at the CDC.",
    "Check the DNS and IP address for the API.",
    "The CPU and GPU are overheating in the PC.",
    "Use WiFi or Bluetooth to connect to the API.",
    "The FDA and CDC are monitoring COVID cases.",
    "She has PTSD and works as a CPA.",
    "He's the VP of R&D at the tech company.",
    "The FAQ says to use HTTPS, not HTTP.",
    "RSVP ASAP and check the URL for details.",
    # BRAND NAMES / PRODUCTS
    "I use Google Chrome.",
    "He uses Microsoft Windows.",
    "She drives a Tesla.",
    "He uses Facebook.",
    "They watch Netflix.",
    "I stream on Spotify.",
    "She uses YouTube.",
    "He shops at Target.",
    "They use Apple products.",
    "I have a Samsung phone.",
    "She uses Adobe software.",
    "He works for Intel.",
    "They use IBM systems.",
    "I watch HBO.",
    "She uses Instagram.",
    "He has a MacBook.",
    "They use Android.",
    # QUESTIONS WITH BRANDS
    "Do you use Google Chrome?",
    "Is he using Microsoft Windows?",
    "Does she drive a Tesla?",
    "Is he using Facebook?",
    "Do they watch Netflix?",
    "Are you streaming on Spotify?",
    "Does she use YouTube?",
    "Do you shop at Target?",
    "Are they using Apple products?",
    "Do you have a Samsung phone?",
    "Does she use Adobe software?",
    "Is he working for Intel?",
    "Do they use IBM systems?",
    "Are you watching HBO?",
    "Does she use Instagram?",
    "Does he have a MacBook?",
    "Are they using Android?",
    # GOVERNMENT / MILITARY ABBREVIATIONS
    "He's in the FBI.",
    "She works for the CIA.",
    "They're with NASA.",
    "He's in the USMC.",
    "She's in the USAF.",
    "They're in the USN.",
    "He's in the USCG.",
    "She's in the USARMY.",
    "It's from the EPA.",
    "She works at the IRS.",
    "He's with the DEA.",
    "They're at the ATF.",
    "Check the NSA website.",
    "It's from the DOD.",
    # INTERNET / SOCIAL MEDIA ABBREVIATIONS
    "Send me a DM.",
    "Send it via email.",
    "Check the FAQ.",
    "It's a PDF.",
    "The URL is broken.",
    "Check the HTML.",
    "Use HTTPS, not HTTP.",
]
