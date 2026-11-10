"""Occupation prompts of short and medium length by field, then long medical and healthcare prompts."""

from __future__ import annotations

ROLES: list[str] = [
    # ULTRA SHORT - MEDICAL/HEALTHCARE
    "Surgeon operating now.",
    "Nurse checking vitals.",
    "Dentist drilling carefully.",
    "Pharmacist filling prescriptions.",
    "Paramedic on scene.",
    "Psychiatrist listening intently.",
    "Radiologist reading scans.",
    "Pediatrician with children.",
    "Cardiologist checking hearts.",
    "Dermatologist examining skin.",
    # ULTRA SHORT - TRADES/SKILLED LABOR
    "Plumber fixing pipes.",
    "Electrician wiring safely.",
    "Carpenter building cabinets.",
    "Mechanic under hood.",
    "Welder sparks flying.",
    "Mason laying bricks.",
    "Roofer up high.",
    "Locksmith picking locks.",
    "HVAC technician repairing.",
    "Crane operator lifting.",
    # ULTRA SHORT - FOOD/HOSPITALITY
    "Chef plating beautifully.",
    "Barista steaming milk.",
    "Bartender mixing drinks.",
    "Sommelier selecting wine.",
    "Baker kneading dough.",
    "Butcher cutting meat.",
    "Caterer setting tables.",
    "Pastry chef decorating.",
    "Dishwasher working hard.",
    "Waiter taking orders.",
    # ULTRA SHORT - CREATIVE/ARTS
    "Artist painting canvas.",
    "Sculptor chiseling marble.",
    "Photographer capturing moments.",
    "Director yelling cut.",
    "Actor delivering lines.",
    "Musician playing guitar.",
    "Dancer leaping gracefully.",
    "Choreographer designing moves.",
    "Composer writing notes.",
    "Animator drawing frames.",
    # ULTRA SHORT - TECHNOLOGY
    "Programmer debugging code.",
    "Developer pushing commits.",
    "Data scientist analyzing.",
    "Cybersecurity analyst monitoring.",
    "Network administrator configuring.",
    "UX designer prototyping.",
    "Product manager prioritizing.",
    "DevOps engineer deploying.",
    "Cloud architect designing.",
    "AI researcher training models.",
    # ULTRA SHORT - VARIOUS FIELDS
    "Lawyer presenting case.",
    "Judge making ruling.",
    "Teacher grading papers.",
    "Professor lecturing students.",
    "Scientist running experiments.",
    "Architect drafting blueprints.",
    "Police officer patrolling.",
    "Firefighter battling flames.",
    "Pilot landing safely.",
    "Astronaut floating weightless.",
    # SHORT - MEDICAL VARIETY
    "The anesthesiologist prepared the patient for surgery.",
    "Neurologist examined the brain scans carefully.",
    "Oncologist discussed treatment options with family.",
    "Orthopedist set the broken bone precisely.",
    "Gynecologist performed the routine checkup.",
    "Urologist reviewed the test results thoroughly.",
    "Podiatrist treated the foot condition.",
    "Chiropractor adjusted the spine alignment.",
    "Physical therapist guided the rehabilitation exercises.",
    "Occupational therapist helped with daily activities.",
    "Speech therapist worked on pronunciation skills.",
    "Nutritionist created a balanced meal plan.",
    "Midwife delivered the baby safely.",
    "Veterinarian vaccinated the puppy.",
    "Phlebotomist drew blood expertly.",
    # SHORT - TRADES VARIETY
    "The glazier installed the window glass.",
    "Pipefitter connected the industrial pipes.",
    "Ironworker assembled the steel beams.",
    "Machinist operated the lathe precisely.",
    "Millwright installed the heavy machinery.",
    "Boilermaker repaired the steam boiler.",
    "Sheet metal worker bent the aluminum.",
    "Tile setter grouted the bathroom floor.",
    "Flooring installer laid the hardwood.",
    "Drywall installer hung the sheetrock.",
    "Insulator wrapped the pipes carefully.",
    "Elevator technician fixed the lift.",
    "Foreman supervised the construction crew.",
    "Surveyor measured the property lines.",
    "Inspector checked the building codes.",
    # SHORT - BUSINESS/FINANCE VARIETY
    "The accountant balanced the quarterly books.",
    "Auditor reviewed the financial statements.",
    "Broker executed the stock trade.",
    "Trader watched the market fluctuations.",
    "Analyst prepared the investment report.",
    "Economist forecasted the growth trends.",
    "Actuary calculated the insurance risks.",
    "Underwriter assessed the loan application.",
    "Financial advisor recommended the portfolio.",
    "Investment banker closed the merger deal.",
    "Venture capitalist funded the startup.",
    "Entrepreneur pitched the business idea.",
    "CEO addressed the shareholders meeting.",
    "Consultant delivered the strategic recommendations.",
    "Recruiter interviewed the candidates.",
    # SHORT - SCIENCE/RESEARCH VARIETY
    "The biologist studied cell division.",
    "Chemist mixed the compounds carefully.",
    "Physicist calculated the particle trajectories.",
    "Geologist examined the rock formations.",
    "Astronomer observed the distant galaxies.",
    "Marine biologist tagged the whale.",
    "Botanist classified the rare plant.",
    "Zoologist tracked the animal migration.",
    "Geneticist sequenced the DNA strand.",
    "Microbiologist cultured the bacteria.",
    "Ecologist measured the ecosystem health.",
    "Meteorologist predicted the storm path.",
    "Archaeologist uncovered the ancient artifacts.",
    "Paleontologist excavated the dinosaur bones.",
    "Anthropologist documented the tribal customs.",
    # SHORT - ENGINEERING VARIETY
    "The civil engineer designed the bridge.",
    "Mechanical engineer tested the engine.",
    "Electrical engineer wired the circuit.",
    "Chemical engineer optimized the process.",
    "Aerospace engineer built the rocket.",
    "Environmental engineer cleaned the water.",
    "Biomedical engineer developed the prosthetic.",
    "Structural engineer reinforced the foundation.",
    "Industrial engineer improved the workflow.",
    "Nuclear engineer monitored the reactor.",
    "Petroleum engineer drilled the well.",
    "Software engineer refactored the code.",
    "Systems engineer integrated the components.",
    "Quality engineer inspected the products.",
    "Robotics engineer programmed the arm.",
    # SHORT - PUBLIC SERVICE/TRANSPORTATION
    "The detective investigated the crime scene.",
    "FBI agent analyzed the evidence.",
    "Border patrol stopped the vehicle.",
    "Park ranger protected the wildlife.",
    "Lifeguard rescued the swimmer.",
    "Security guard monitored the cameras.",
    "Correctional officer supervised the inmates.",
    "Flight attendant served the passengers.",
    "Air traffic controller guided the plane.",
    "Ship captain navigated the waters.",
    "Truck driver delivered the cargo.",
    "Bus driver picked up passengers.",
    "Train conductor checked the tickets.",
    "Dispatcher coordinated the emergency response.",
    "Logistics coordinator tracked the shipment.",
    # MEDIUM - MIXED OCCUPATIONS
    (
        "The surgeon carefully sutured the wound, while the anesthesiologist monitored the patient's vital signs "
        "throughout the delicate procedure."
    ),
    (
        "Barista crafted the perfect latte art, while the pastry chef arranged croissants in the display case for "
        "morning customers."
    ),
    (
        "Architect presented the building design to the client, while the structural engineer reviewed the foundation "
        "specifications carefully."
    ),
    (
        "Firefighter climbed the ladder to rescue the family, while the paramedic prepared the ambulance for emergency "
        "transport."
    ),
    (
        "Software engineer debugged the critical bug, while the product manager updated the sprint backlog for the "
        "development team."
    ),
    (
        "Veterinarian performed surgery on the injured dog, while the veterinary technician prepared the medications "
        "and monitored recovery."
    ),
    (
        "Journalist interviewed the politician about the scandal, while the photographer captured candid moments "
        "during the press conference."
    ),
    (
        "Chef prepared the tasting menu for critics, while the sommelier selected the perfect wine pairings for each "
        "course."
    ),
    (
        "Electrician rewired the old house completely, while the plumber installed new copper pipes throughout the "
        "basement level."
    ),
    (
        "Professor delivered the keynote lecture, while the teaching assistant distributed handouts and managed the "
        "student questions."
    ),
    (
        "Lawyer cross examined the witness, while the paralegal organized the evidence files for the defense team "
        "presentation."
    ),
    (
        "Pilot navigated through the turbulent weather, while the flight attendant calmed the nervous passengers with "
        "reassurance."
    ),
    (
        "Director blocked the emotional scene, while the cinematographer adjusted the lighting for the perfect "
        "dramatic effect."
    ),
    (
        "Dentist performed the root canal procedure, while the dental hygienist prepared the instruments and assisted "
        "throughout."
    ),
    "Real estate agent showed the property, while the appraiser calculated the fair market value for the buyers.",
    # MEDIUM - QUESTIONS
    "Did the plumber fix the leak, or does the homeowner need to call the contractor for major repairs?",
    (
        "Will the surgeon perform the operation tomorrow, or should the anesthesiologist prepare for an emergency "
        "procedure instead?"
    ),
    (
        "Can the architect revise the blueprints, while the civil engineer recalculates the structural load "
        "requirements today?"
    ),
    "Should the barista train the new employee, or does the manager prefer to handle orientation personally?",
    "Has the detective solved the case, or does the FBI agent need to take over the investigation?",
    "Would the chef accept the catering job, while the pastry chef prepares desserts for the wedding?",
    "Is the programmer ready to deploy the code, or should the DevOps engineer review it first?",
    "Did the teacher grade all the exams, while the principal reviewed the curriculum changes for approval?",
    "Can the veterinarian see the emergency patient, or should the technician stabilize the animal first?",
    "Should the accountant file the taxes, or does the auditor need to complete the review first?",
    # MEDIUM - EXCLAMATIONS
    (
        "The surgeon saved three lives today, and the entire surgical team celebrated the successful marathon of "
        "operations!"
    ),
    "That barista makes the best espresso in the city, and the cafe owner just promoted her to manager!",
    (
        "The architect won the prestigious design award, and the construction company immediately offered a "
        "partnership deal!"
    ),
    (
        "Firefighters rescued everyone from the burning building, and the mayor personally thanked the entire brave "
        "department!"
    ),
    "The programmer fixed the bug that crashed production, and the CTO gave the entire team a bonus!",
    "That veterinarian saved our beloved pet, and we are forever grateful for the compassionate emergency care!",
    "The journalist broke the biggest story of the year, and the editor offered a senior correspondent position!",
    (
        "Chef's restaurant received three Michelin stars, and reservations are now booked six months in advance "
        "everywhere!"
    ),
    "The electrician prevented what could have been a fire, and the homeowner thanked them profusely for spotting it!",
    (
        "Professor's research paper changed the field, and universities worldwide are now teaching the groundbreaking "
        "methodology!"
    ),
    # LONG - MEDICAL/HEALTHCARE
    (
        "The surgeon performed the delicate heart transplant, while the anesthesiologist carefully monitored the "
        "patient's vital signs and the surgical nurses prepared instruments with precision throughout the procedure."
    ),
    (
        "Pediatrician explained the vaccination schedule to worried parents, while the nurse prepared the injections "
        "and the receptionist scheduled the follow up appointment for the following month."
    ),
    (
        "Psychiatrist conducted the therapy session with empathy, while the psychologist reviewed the assessment "
        "results and the social worker coordinated community support resources for the patient."
    ),
    (
        "Radiologist analyzed the MRI scans for abnormalities, while the technician positioned the next patient and "
        "the oncologist waited anxiously for the diagnostic results to discuss treatment."
    ),
    (
        "Physical therapist guided the patient through rehabilitation exercises, while the occupational therapist "
        "assessed daily living skills and the speech therapist worked on communication recovery techniques."
    ),
    (
        "Dentist performed the complex root canal procedure, while the dental hygienist assisted with suction and the "
        "orthodontist reviewed the patient's braces adjustment scheduled for next week."
    ),
    (
        "Pharmacist carefully verified the prescription dosages, while the technician counted pills and the delivery "
        "driver prepared to transport medications to elderly patients at their homes."
    ),
    (
        "Cardiologist interpreted the echocardiogram results carefully, while the nurse practitioner updated the "
        "patient's records and the medical assistant scheduled the stress test for the following day."
    ),
    (
        "Dermatologist examined the suspicious mole closely, while the pathologist prepared the biopsy slides and the "
        "oncologist reviewed the patient's family history for cancer risk factors."
    ),
    (
        "Neurologist conducted the comprehensive neurological exam, while the EEG technician prepared the equipment "
        "and the rehabilitation specialist planned the stroke recovery therapy program for the patient."
    ),
]
