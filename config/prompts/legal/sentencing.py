"""Legal prompts: long arguments, sentencing, questions, and exclamations, then Latin terms and court personnel."""

from __future__ import annotations

SENTENCING: list[str] = [
    # LONG - LEGAL ARGUMENTS
    (
        "Your Honor, the Fourth Amendment clearly prohibits warrantless searches absent exigent circumstances, and the "
        "prosecution has failed to articulate any legitimate exception that would justify the search of my client's "
        "home."
    ),
    (
        "The precedent established in Miranda v Arizona requires suppression of any statements made during custodial "
        "interrogation when the defendant was not properly advised of their constitutional rights beforehand."
    ),
    (
        "We submit that the statute under which my client has been charged is unconstitutionally vague and fails to "
        "provide adequate notice of what conduct is prohibited under the law."
    ),
    (
        "The prosecution's expert witness should be excluded under the Daubert standard because the methodology "
        "underlying their conclusions has not been subjected to peer review or general acceptance in the field."
    ),
    (
        "Your Honor, the doctrine of collateral estoppel bars relitigation of this issue because it was already "
        "decided adversely to the prosecution in the prior proceeding involving the same defendant."
    ),
    (
        "The defendant's Sixth Amendment right to confrontation has been violated by the admission of testimonial "
        "hearsay from a declarant who was not produced for cross examination at this trial."
    ),
    (
        "We move for judgment as a matter of law because no reasonable jury could find beyond a reasonable doubt that "
        "my client committed the acts alleged based on this evidence."
    ),
    (
        "The search warrant was obtained based on information from an informant whose reliability had never been "
        "established, rendering the warrant and all evidence derived therefrom fruit of the poisonous tree."
    ),
    (
        "Your Honor, imposing the death penalty in this case would violate the Eighth Amendment prohibition against "
        "cruel and unusual punishment given the defendant's documented intellectual disability and diminished capacity."
    ),
    (
        "The prosecution's failure to disclose exculpatory evidence in a timely manner constitutes a Brady violation "
        "requiring dismissal of the charges or, at minimum, a new trial for my client."
    ),
    (
        "Under the felony murder rule, the defendant is liable for the death that occurred during commission of the "
        "robbery, even though a co conspirator actually pulled the trigger that night."
    ),
    (
        "The statute of limitations has run on this offense, and the prosecution's attempt to resurrect these stale "
        "charges based on newly discovered evidence does not toll the limitations period."
    ),
    (
        "Your Honor, the proposed class members share common questions of law and fact, and class certification is "
        "appropriate because individual adjudication would be impractical and inefficient for all parties."
    ),
    (
        "The defendant's waiver of Miranda rights was not knowing, intelligent, and voluntary because it was obtained "
        "during a twelve hour interrogation without food, water, or access to counsel."
    ),
    (
        "We argue that the mandatory minimum sentence prescribed by this statute violates the separation of powers by "
        "removing sentencing discretion that properly belongs to the judicial branch."
    ),
    # LONG - SENTENCING STATEMENTS
    (
        "Your Honor, my client accepts full responsibility for his actions and has taken concrete steps toward "
        "rehabilitation, including completing substance abuse treatment and maintaining steady employment for the past "
        "eighteen months."
    ),
    (
        "The defendant has shown no remorse, no empathy for the victims, and poses an ongoing danger to the community; "
        "the People request the maximum sentence permitted under the law."
    ),
    (
        "My client is a first time offender who made a terrible mistake under circumstances unlikely to ever recur; we "
        "ask the court to consider probation with conditions rather than incarceration."
    ),
    (
        "The victim impact statements you have heard today barely scratch the surface of the devastation the "
        "defendant's actions have caused to multiple families who will never fully recover."
    ),
    (
        "Your Honor, the prosecution's sentencing recommendation fails to account for my client's troubled childhood, "
        "history of abuse, and lack of prior criminal history before this isolated incident."
    ),
    (
        "The defendant systematically preyed on elderly victims, stealing their life savings through an elaborate "
        "fraud scheme; this court should impose consecutive sentences on all seventeen counts."
    ),
    (
        "My client has been a model prisoner during pretrial detention, has earned his GED, and has a job offer "
        "waiting upon release; we request credit for time served."
    ),
    (
        "The court must consider the defendant's role as the sole caregiver for three minor children who would be "
        "placed in foster care if their mother receives a lengthy sentence."
    ),
    (
        "This defendant has been before this court four times previously, and leniency has done nothing to deter "
        "future criminal conduct; only meaningful incarceration will protect the public safety."
    ),
    (
        "Your Honor, under the federal sentencing guidelines, the applicable range is ninety seven to one hundred "
        "twenty one months, but we submit that a downward departure is warranted here."
    ),
    (
        "The defendant's cooperation with authorities led to the conviction of twelve co conspirators and the recovery "
        "of millions in stolen assets; substantial assistance warrants a reduced sentence."
    ),
    (
        "My client's mental health struggles, which have been extensively documented by treating physicians, provide "
        "important context for understanding how this offense came to occur under these circumstances."
    ),
    (
        "The defendant expressed no remorse during allocution and instead blamed the victims for their own "
        "victimization; such callousness should be reflected in the severity of the sentence."
    ),
    (
        "We ask the court to impose a sentence that emphasizes rehabilitation rather than retribution, one that gives "
        "my client the opportunity to become a productive member of society again."
    ),
    (
        "The totality of circumstances, including the heinous nature of the offense, the vulnerability of the victims, "
        "and the defendant's criminal history, justifies imposition of the maximum statutory penalty."
    ),
    # LONG - QUESTIONS
    (
        "If the prosecution's timeline is accurate, how do they explain the fact that the defendant was captured on "
        "surveillance video thirty miles away just fifteen minutes before the crime?"
    ),
    (
        "How can the jury be expected to credit testimony from a witness who has changed their story four times and is "
        "testifying under a cooperation agreement to avoid prison?"
    ),
    (
        "If my client truly intended to commit murder, why would he have called nine one one immediately afterward and "
        "waited at the scene for police to arrive and arrest him?"
    ),
    (
        "Your Honor, how is it possible that the prosecution failed to preserve this critical evidence when they knew "
        "from the beginning that it was central to the defendant's case?"
    ),
    (
        "Can the prosecution explain why none of the defendant's DNA was found at the crime scene despite their theory "
        "that he spent over two hours there committing these acts?"
    ),
    (
        "If the confession was truly voluntary, why does the interrogation video show my client asking for a lawyer "
        "six times before detectives finally obtained the statement they wanted?"
    ),
    (
        "How does the defense reconcile their alibi theory with the eyewitness testimony from three independent "
        "witnesses who all positively identified the defendant as the perpetrator at trial?"
    ),
    (
        "Your Honor, is it not fundamentally unfair to proceed with this trial when the prosecution has refused to "
        "disclose the identity of its confidential informant to the defense?"
    ),
    (
        "If the defendant acted in self defense as claimed, why did she retrieve a weapon from another room rather "
        "than simply fleeing the residence through the open front door?"
    ),
    (
        "How can the state seek the death penalty when there are so many unanswered questions about the reliability of "
        "the forensic evidence used to obtain this conviction?"
    ),
    (
        "Does the prosecution truly expect this jury to believe that my client, a ninety three pound woman, "
        "overpowered and killed a two hundred forty pound man without any weapon or assistance?"
    ),
    (
        "Your Honor, given the extensive pretrial publicity in this case, how can the defendant possibly receive a "
        "fair trial from an impartial jury in this jurisdiction?"
    ),
    (
        "If the police investigation was as thorough as the prosecution claims, why did detectives fail to interview "
        "any of the five witnesses identified by the defense early on?"
    ),
    (
        "How is it possible that the chain of custody documentation is missing for the most critical piece of evidence "
        "in this case, the alleged murder weapon itself?"
    ),
    (
        "Can the prosecution point to a single piece of physical evidence tying my client to this crime that has not "
        "been challenged or undermined by the defense experts?"
    ),
    # LONG - EXCLAMATIONS
    (
        "Your Honor, this is nothing short of prosecutorial persecution! My client has been targeted, harassed, and "
        "now charged with a crime based on nothing but speculation and innuendo!"
    ),
    (
        "After forty years, DNA evidence has finally exonerated my client, proving what he has maintained from day "
        "one: he is innocent and the real killer remains at large!"
    ),
    (
        "The corruption exposed in this case goes to the very heart of our justice system, and those responsible must "
        "be held accountable for the lives they have destroyed!"
    ),
    (
        "This verdict sends a clear message to victims everywhere: come forward, speak your truth, and the justice "
        "system will believe you and hold your abusers accountable!"
    ),
    (
        "My client has spent the best years of his life behind bars for a crime he did not commit, and no amount of "
        "compensation can ever make that right!"
    ),
    (
        "The defendant's attorneys should be ashamed of themselves for putting the victim through a second trauma with "
        "their victim blaming tactics and character assassination throughout this trial!"
    ),
    (
        "This is the largest financial fraud in the history of this state, and the defendant's greed and arrogance "
        "have devastated thousands of hardworking families who trusted him!"
    ),
    (
        "Justice has finally been served after a decade long fight, and we hope this verdict brings some measure of "
        "peace to all those who lost loved ones!"
    ),
    (
        "The misconduct by law enforcement in this case is absolutely shocking, and every conviction obtained by these "
        "officers must now be reviewed for similar constitutional violations!"
    ),
    (
        "My client stood up against a powerful corporation that put profits over people, and today's verdict proves "
        "that no company is too big to be held accountable!"
    ),
    (
        "This wrongful conviction demonstrates everything that is broken about our criminal justice system, from "
        "tunnel vision policing to inadequate defense resources for indigent defendants!"
    ),
    (
        "The defendant showed absolutely no mercy to his victims, terrorizing an entire community for years, and the "
        "maximum sentence is the only appropriate response to such cruelty!"
    ),
    (
        "After everything this family has been through, they finally have answers, and while nothing can bring their "
        "daughter back, at least her killer will face justice!"
    ),
    (
        "This precedent setting verdict will change how corporations are held accountable for environmental crimes and "
        "represents a victory for communities fighting pollution across the entire country!"
    ),
    (
        "My client has been completely vindicated, and we will be pursuing civil action against every individual and "
        "agency responsible for this malicious and baseless prosecution!"
    ),
    # ADDITIONAL - LEGAL LATIN TERMS (short)
    "The doctrine of stare decisis applies.",
    "Pro bono representation was provided.",
    "The evidence is prima facie sufficient.",
    "Acting in loco parentis status.",
    "The contract is void ab initio.",
    "Filing a habeas corpus petition.",
    "The defendant acted mens rea.",
    "Establishing corpus delicti first.",
    "The in camera review concluded.",
    "Amicus curiae brief submitted.",
    "The nolo contendere plea entered.",
    "Certiorari was granted by the court.",
    "Subpoena duces tecum was served.",
    "The doctrine of res ipsa loquitur.",
    "Pro se representation is permitted.",
    "Per curiam opinion was issued.",
    "De novo review is required.",
    "Guardian ad litem was appointed.",
    "Quid pro quo was established.",
    "Ex parte communication prohibited.",
    # ADDITIONAL - COURT PERSONNEL (short)
    "The stenographer recorded everything verbatim.",
    "The court interpreter translated accurately.",
    "The jury foreman delivered the verdict.",
    "The court administrator scheduled the hearing.",
    "The probation officer filed the report.",
    "The mediator facilitated the settlement.",
    "The special master reviewed the documents.",
    "The court appointed psychiatrist testified.",
    "The expert witness was cross examined.",
    "The character witness spoke favorably.",
    "The coroner determined cause of death.",
    "The forensic specialist analyzed the evidence.",
    "The handwriting expert authenticated the signature.",
    "The court clerk filed the motion.",
    "The victim advocate provided support.",
]
