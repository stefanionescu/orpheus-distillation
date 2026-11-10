"""Legal prompts: medium exclamations, then long opening statements, closing arguments, instructions, and testimony."""

from __future__ import annotations

TESTIMONY: list[str] = [
    # MEDIUM - EXCLAMATIONS
    "This is an outrage, Your Honor! My client's constitutional rights have been trampled upon!",
    "The prosecution is attempting to railroad an innocent man into prison for life!",
    "I have never seen such blatant prosecutorial misconduct in my thirty years of practice!",
    "This witness is lying under oath, and the prosecution knows it full well!",
    "The evidence clearly shows that my client is the victim here, not the perpetrator!",
    "Justice has been served today, and the community can finally begin to heal!",
    "This verdict is a travesty of justice that will haunt this court for years!",
    "The defendant's behavior in this courtroom has been absolutely contemptuous throughout!",
    "We finally have justice for the victim after ten long years of fighting!",
    "The corruption in this case goes all the way to the top of the department!",
    "My client has been vindicated after spending fifteen years in prison for a crime they didn't commit!",
    "This settlement is a victory for consumers everywhere who have been exploited by corporate greed!",
    "The jury saw through the prosecution's house of cards and delivered the right verdict!",
    "This precedent setting ruling will protect civil liberties for generations to come!",
    "After all these years, the families finally have the closure they so desperately needed!",
    # LONG - OPENING STATEMENTS
    (
        "Ladies and gentlemen of the jury, over the next several days you will hear evidence that proves beyond any "
        "shadow of doubt that the defendant committed cold blooded, premeditated murder."
    ),
    (
        "The prosecution will present DNA evidence, fingerprint analysis, eyewitness testimony, and surveillance "
        "footage that together form an unbreakable chain linking the defendant directly to this horrific crime scene."
    ),
    (
        "My client, a decorated war veteran with no prior criminal record, stands accused of a crime he did not "
        "commit, and we will prove his innocence through unimpeachable evidence."
    ),
    (
        "What you will learn is that the police focused on my client from day one, ignoring other suspects and "
        "evidence that pointed away from him because they needed a quick arrest."
    ),
    (
        "This is not a complicated case, despite what the defense will try to tell you; the defendant was caught red "
        "handed, and all the evidence points to one inescapable conclusion."
    ),
    (
        "The evidence will show that the defendant planned this crime for months, meticulously covering their tracks "
        "while systematically defrauding investors out of hundreds of millions of dollars."
    ),
    (
        "You will hear from the victim herself, who will describe in her own words the terror she experienced at the "
        "hands of the defendant on that fateful September evening."
    ),
    (
        "The defense will attempt to muddy the waters with technical objections and legal maneuvers, but don't be "
        "distracted; focus on the facts, and the truth will become clear."
    ),
    (
        "My client exercised her constitutional right to self defense when confronted by an armed intruder in her own "
        "home, and the prosecution's charges are nothing short of victim blaming."
    ),
    (
        "Over the course of this trial, you will come to know the victim not as a case number, but as a beloved "
        "daughter, sister, and friend who deserves justice."
    ),
    (
        "The prosecution's case relies entirely on circumstantial evidence and the testimony of witnesses who have "
        "every reason to lie to save themselves from prosecution for their own crimes."
    ),
    (
        "This case is about holding a powerful corporation accountable for knowingly selling a defective product that "
        "caused the deaths of one hundred and forty seven innocent people nationwide."
    ),
    (
        "The defendant sitting before you today is not a monster, but a human being who made a terrible mistake in a "
        "moment of passion that he has regretted every day since."
    ),
    (
        "What happened to the victim was tragic and heartbreaking, but tragedy alone does not prove guilt, and the "
        "prosecution must prove every element of this crime beyond reasonable doubt."
    ),
    (
        "The evidence will demonstrate a pattern of abuse spanning fifteen years, during which my client lived in "
        "constant fear for her life and the lives of her children."
    ),
    # LONG - CLOSING ARGUMENTS
    (
        "You have heard the evidence, you have seen the defendant's demeanor on the stand, and now you must deliver "
        "justice for a victim who can no longer speak for herself."
    ),
    (
        "The prosecution promised you a mountain of evidence and delivered a molehill; they have not proven their "
        "case, and you must acquit my client of all charges today."
    ),
    (
        "When you retire to deliberate, I ask you to consider: if it were you on trial, would you want a jury to "
        "convict on evidence this flimsy and circumstantial?"
    ),
    (
        "The defendant showed no remorse, no compassion, no humanity when committing these acts, and your verdict "
        "should reflect the severity of what he did to those innocent victims."
    ),
    (
        "Every piece of evidence the prosecution presented has been challenged, rebutted, and explained; what remains "
        "is insufficient to support a conviction under any standard of proof."
    ),
    (
        "Twelve citizens hold the power to tell this community that we will not tolerate violence against our most "
        "vulnerable members; exercise that power today with a guilty verdict."
    ),
    (
        "The defense has raised reasonable doubt at every turn, and if you have any lingering questions about my "
        "client's guilt, you are obligated by law to acquit him."
    ),
    (
        "This is your opportunity to send a message to corporate boardrooms everywhere that human lives matter more "
        "than profit margins and quarterly earnings reports to shareholders."
    ),
    (
        "Consider the weight of what you are about to do: convicting an innocent person is as much a miscarriage of "
        "justice as letting a guilty person go free."
    ),
    (
        "The defendant gambled that she could commit the perfect crime and never be caught, but thanks to dedicated "
        "investigators, she lost that bet and must now pay the price."
    ),
    (
        "I submit that the only verdict consistent with the evidence, with justice, and with your oath as jurors is a "
        "verdict of not guilty on all counts."
    ),
    (
        "The victim's family has waited four long years for this moment, and I ask you to give them the closure and "
        "justice they have been denied for so long."
    ),
    (
        "If you believe even one of the prosecution's witnesses was lying, and I've shown you they all were, then the "
        "entire case collapses like a house of cards."
    ),
    (
        "What the defendant did was not just illegal, it was evil, calculated, and deserving of the maximum punishment "
        "this court is authorized to impose under the law."
    ),
    (
        "The prosecution wants you to convict based on emotion rather than evidence, but your duty is to follow the "
        "law, even when it's difficult to do so."
    ),
    # LONG - JUDICIAL INSTRUCTIONS
    (
        "Members of the jury, you must decide this case based solely on the evidence presented in this courtroom, not "
        "on anything you may have seen or heard outside these walls."
    ),
    (
        "The defendant is presumed innocent unless and until the prosecution proves guilt beyond a reasonable doubt; "
        "the burden never shifts to the defendant to prove their innocence."
    ),
    (
        "Circumstantial evidence is not inherently less reliable than direct evidence, but you must be satisfied that "
        "the only reasonable inference from such evidence points to the defendant's guilt."
    ),
    (
        "You are the sole judges of witness credibility; consider their demeanor, their potential biases, their "
        "opportunity to observe, and whether their testimony makes sense in light of other evidence."
    ),
    (
        "If you find the defendant guilty of the charged offense, you must then determine whether the prosecution has "
        "also proven the special circumstances alleged in the charging document."
    ),
    (
        "The crime of first degree murder requires proof of premeditation and deliberation; if you find the killing "
        "was impulsive, you may consider the lesser included offense of second degree murder."
    ),
    (
        "You must consider each count separately and return a separate verdict for each; a finding of guilt on one "
        "count does not require a finding of guilt on others."
    ),
    (
        "Expert witnesses have offered their opinions based on specialized knowledge, but you are not required to "
        "accept their conclusions if you find them unpersuasive or unreliable."
    ),
    (
        "The defendant's decision not to testify cannot be held against them; every person has a constitutional right "
        "to remain silent, and no negative inference may be drawn from exercising it."
    ),
    (
        "If during deliberations you find that you cannot reach a unanimous verdict after thorough discussion, please "
        "notify the bailiff, and I will provide further instructions to assist you."
    ),
    (
        "Self defense requires that the defendant reasonably believed they faced imminent danger of death or great "
        "bodily harm and used only the force necessary to repel that threat."
    ),
    (
        "The law requires unanimity for any verdict; all twelve of you must agree before you can return a verdict of "
        "either guilty or not guilty on any count."
    ),
    (
        "You may not conduct your own investigation or research; do not visit the crime scene, search the internet, or "
        "discuss this case with anyone until deliberations are complete."
    ),
    (
        "Reasonable doubt is not a fanciful or imaginary doubt, but one based on reason and common sense after careful "
        "consideration of all the evidence presented."
    ),
    (
        "The punishment for any crimes is not your concern during deliberations; your only job is to determine whether "
        "the prosecution has met its burden of proof on each element."
    ),
    # LONG - WITNESS TESTIMONY
    (
        "I was standing at the bus stop when I heard a gunshot, turned around, and saw the defendant running from the "
        "alley with what looked like a handgun in their hand."
    ),
    (
        "As a forensic accountant, I examined the defendant's financial records and found a pattern of fraudulent "
        "transactions totaling approximately fourteen point seven million dollars over a three year period."
    ),
    (
        "The victim told me the defendant had threatened to kill her if she ever tried to leave, and she showed me "
        "bruises on her arms consistent with someone grabbing her forcefully."
    ),
    (
        "I performed the autopsy and determined the cause of death was blunt force trauma to the head; the injuries "
        "were consistent with being struck multiple times with a heavy object."
    ),
    (
        "When I arrived at the scene, the defendant was standing over the body holding a bloody knife; when I ordered "
        "them to drop it, they said 'I had to do it.'"
    ),
    (
        "I've been practicing psychiatry for thirty years, and in my professional opinion, the defendant was suffering "
        "from a severe psychotic episode and was unable to appreciate the wrongfulness of their actions."
    ),
    (
        "The security footage clearly shows the defendant entering the building at nine forty seven PM, proceeding "
        "directly to the victim's office, and leaving at ten twenty three PM carrying a large duffel bag."
    ),
    (
        "I ran ballistics on the bullet recovered from the victim's body and confirmed it was fired from the weapon "
        "registered to and recovered from the defendant's residence during the search."
    ),
    (
        "We had been married for twenty years before I discovered the defendant had been systematically transferring "
        "our joint assets into secret offshore accounts in preparation for abandoning our family."
    ),
    (
        "The defendant confided in me that they planned to quote unquote 'make the victim pay' for what happened, and "
        "two weeks later the victim was found dead in suspicious circumstances."
    ),
    (
        "I analyzed the blood spatter patterns at the scene, and they are consistent with the victim being attacked "
        "while standing and then falling to the ground where additional blows were inflicted."
    ),
    (
        "The defendant told me they needed an alibi for the night of the murder and offered me fifty thousand dollars "
        "in cash to testify that we were together, which we were not."
    ),
    (
        "As the responding paramedic, I observed that the victim was severely beaten and barely conscious; before "
        "losing consciousness, she whispered the defendant's name when I asked who did this."
    ),
    (
        "I examined the computer seized from the defendant's home and recovered deleted search history showing queries "
        "for 'how to get away with murder' and 'untraceable poisons' in the weeks before."
    ),
    (
        "The victim and I were best friends since childhood, and she confided in me that she was terrified of the "
        "defendant and believed he would eventually kill her if she stayed."
    ),
]
