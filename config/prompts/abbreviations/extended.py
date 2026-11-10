"""Abbreviation prompts: long statements, questions, exclamations, and mixed contexts."""

from __future__ import annotations

EXTENDED: list[str] = [
    # ADDITIONAL LONG EXAMPLES - STATEMENTS
    (
        "The CEO announced a major restructuring of the company, and the CFO is preparing the financial reports for "
        "the board meeting next week."
    ),
    (
        "I've been studying for my MBA at night while working full time during the day, and it's been challenging but "
        "really rewarding."
    ),
    (
        "The IT department upgraded all our computers with new SSDs and more RAM, so everything should run much faster "
        "now."
    ),
    "She received her PhD in molecular biology from MIT, and now she's working on groundbreaking research at the NIH.",
    "Our VP of marketing wants us to update the SEO strategy by EOD, so we need to prioritize that task today.",
    "The FDA just approved a new treatment for diabetes, and the pharmaceutical company's stock went up significantly.",
    "I accidentally clicked on a suspicious URL and now I'm worried about malware, so the IT team is running a scan.",
    "The DNA test results came back, and the doctor said everything looks normal, which is such a relief.",
    (
        "He's been working at the NSA for fifteen years, and he can't talk about most of the projects he's been "
        "involved with."
    ),
    "The GPS in my car stopped working, so I had to use Google Maps on my phone instead to navigate.",
    "She works as a CPA during tax season and it's incredibly stressful, but the rest of the year is more manageable.",
    (
        "The HTML and CSS on this website need a complete overhaul because the design looks like it's from the early "
        "2000s."
    ),
    "Our CEO and COO are flying to London for the annual conference, and they'll be presenting our new product line.",
    "I just passed my LSAT exam, and I'm applying to law schools with the goal of getting my JD degree.",
    "The WiFi signal in this building is terrible, so I've been using my phone's hotspot instead for video calls.",
    (
        "The FBI opened an investigation after receiving multiple reports about the suspicious activity in the "
        "financial records."
    ),
    "She's an RN who specializes in oncology, and she's been working at the same hospital for over twenty years.",
    (
        "The MRI results showed no abnormalities, which was a huge relief after weeks of worrying about potential "
        "problems."
    ),
    (
        "Our CTO wants to implement a new API that will integrate all our systems and improve data sharing across "
        "departments."
    ),
    "I've been taking CBD oil for my anxiety, and it seems to help, but I'm still seeing my therapist regularly.",
    "The ATM near my house is always out of cash on weekends, so I usually have to drive to a different one.",
    (
        "He earned his MD from Johns Hopkins and completed his residency in neurosurgery at UCLA, which took almost "
        "ten years."
    ),
    (
        "The EPA released new guidelines for emissions, and our manufacturing plant will need to make significant "
        "changes to comply."
    ),
    "I sent the document as a PDF attachment, but apparently it didn't go through, so I'll resend it right away.",
    (
        "The HR department is implementing a new PTO policy that will give employees more flexibility with their "
        "vacation time."
    ),
    (
        "She's been diagnosed with PCOS and is working with her gynecologist to manage the symptoms through lifestyle "
        "changes."
    ),
    "The USB port on my laptop stopped working, so I had to buy a dongle to connect my external hard drive.",
    "Our PM wants to have a status update meeting every morning at nine, which I think is a bit excessive.",
    "The CDC issued a travel advisory for that region due to an outbreak, so we've postponed our trip indefinitely.",
    "He works in R&D developing new products, and his team just received a patent for their latest invention.",
    # ADDITIONAL LONG EXAMPLES - QUESTIONS
    "Did you hear that the CEO is stepping down next month, and do you have any idea who might be replacing them?",
    "Can you send me the PDF version of the report, because the DOC file isn't opening correctly on my computer?",
    "What time is the webinar that HR scheduled about the new health insurance options for full time employees?",
    (
        "Have you had a chance to review the API documentation, because I'm confused about how to authenticate the "
        "requests?"
    ),
    "Is the WiFi working in the conference room, or should we reschedule the video call with the remote team?",
    "Did you know that she has both an MBA and a JD, and she's now working as a consultant for tech startups?",
    (
        "Can you explain why the URL keeps redirecting to a different page, because I've checked the settings and "
        "everything looks correct?"
    ),
    "What does the FAQ say about refund policies, because I've been trying to return this item for over a week?",
    "Have you contacted the IT helpdesk about the VPN issues, or should I open a ticket on your behalf?",
    "Is it true that the CFO is leaving to join a competitor, and how do you think this will affect the company?",
    "What's the ETA for the delivery, because I've been waiting for two weeks and the tracking hasn't updated?",
    "Can you check if the DNS settings are correct, because the website has been down since yesterday morning?",
    "Did the doctor say anything about the MRI results, or do we need to schedule a follow up appointment?",
    "Have you RSVP'd to the company holiday party yet, and are you planning to bring a plus one this year?",
    "Why is the CPU usage so high on this server, and should we be concerned about performance issues?",
    "Do you know if the CEO's speech will be recorded, because I have a conflict and won't be able to attend live?",
    "What's the difference between HTTP and HTTPS, and why is it important for website security these days?",
    "Have you submitted your timesheet to HR yet, because the deadline is EOD and payroll is tomorrow?",
    "Is the ATM outside the building still working, or is it out of service like it was last week?",
    "Did the FDA approve that new medication yet, because my doctor mentioned it might be helpful for my condition?",
    "Can you send me the HTML source code, because I want to see how they implemented that animation effect?",
    "What time does the PM want us to meet tomorrow, and should I bring the updated project timeline?",
    "Have you seen the new iPhone that Apple announced, and are you thinking about upgrading from your current model?",
    "Is it possible to convert this JSON file to a CSV format, because Excel doesn't recognize the current format?",
    "Do you know which department the CTO reports to, because I need to escalate an issue about the IT infrastructure?",
    # ADDITIONAL LONG EXAMPLES - EXCLAMATIONS
    "I can't believe the CEO just announced we're getting bonuses this year, and I'm so excited about the news!",
    "The IT team finally fixed the WiFi issue that's been driving everyone crazy for the past month!",
    "OMG, did you hear that she passed her PhD defense with flying colors, and everyone is so proud of her!",
    "This API is absolutely amazing, and it's going to save us so much time on data integration projects!",
    "I'm so relieved that the MRI came back clear, because I was really worried about the test results!",
    "The new CEO is making so many positive changes, and the company culture has improved dramatically!",
    "Finally, someone explained what all these abbreviations mean, and now I understand the technical documentation!",
    "I can't believe how fast the SSD made my computer, and I should have upgraded years ago!",
    "The HR department announced unlimited PTO, and everyone in the office is absolutely thrilled about it!",
    (
        "Thank goodness the FDA approved that medication, because so many patients have been waiting for treatment "
        "options!"
    ),
    "The GPS saved us when we got lost in the mountains, and I'm so grateful we had signal!",
    "I'm so impressed that she earned her MBA while raising three kids, and that takes incredible dedication!",
    "The CFO's presentation at the quarterly meeting was outstanding, and everyone was blown away by the results!",
    "I finally understand how DNS works after watching that tutorial, and it makes so much more sense now!",
    "The VPN connection is working perfectly for the first time in weeks, and remote work is so much easier!",
    "NASA's latest discovery about exoplanets is absolutely fascinating, and I can't stop reading about it!",
    "The CDC guidelines have been updated, and it's such a relief to have clear information about safety protocols!",
    "I'm amazed at how much data you can store on a USB drive these days compared to just a few years ago!",
    "The HTML and CSS on this website are so beautifully designed, and I want to learn how they did it!",
    "Our CTO just won an innovation award, and the whole company is celebrating this incredible achievement!",
    # ADDITIONAL LONG EXAMPLES - MIXED CONTEXTS
    (
        "Working at NASA must be incredible, because every day you're contributing to humanity's understanding of the "
        "universe."
    ),
    "I sent the RSVP last week but never received a confirmation email, so I'm worried it didn't go through properly.",
    "The doctor recommended an EKG to check my heart rhythm, and the results should be available within a few days.",
    "She transitioned from being a CPA to working as a CFO for a Fortune 500 company, which is quite impressive.",
    "The JSON file contains all the user data we need, but we'll have to write a script to parse it correctly.",
    "He's been dealing with PTSD since returning from deployment, and he's finally getting the support he needs.",
    "Our company just partnered with IBM to develop new cloud computing solutions for enterprise clients.",
    "The XML document wasn't formatted correctly, so the parser kept throwing errors until we fixed the syntax.",
    "She works at the CDC studying infectious diseases, and her research has been cited in major medical journals.",
    "I need to update my LinkedIn profile with my new MBA credentials before I start applying for new positions.",
    "The QA team found several bugs in the latest build, so we'll have to delay the release until they're fixed.",
    "He was promoted to SVP after leading the most successful product launch in the company's history.",
    "The IRS sent me a letter about my tax return, and I'm not sure if I should be worried or not.",
    "She uses both Android and iOS devices for testing, which helps her understand different user experiences.",
    (
        "The RAM upgrade made a huge difference in performance, especially when running multiple applications "
        "simultaneously."
    ),
    "Our PR team is preparing a statement about the merger, and it should be released to the media by EOD.",
    "The DEA investigation uncovered a major trafficking operation, and several arrests were made last week.",
    "I finally got my ADHD diagnosis as an adult, and it explains so much about my experiences growing up.",
    "The GPU in this computer is powerful enough to handle video editing and 3D rendering without any issues.",
    "She completed her residency in emergency medicine and now works as an attending physician in the ER.",
]
