"""Politics prompts about democracy, legislation, institutions, and authoritarianism."""

from __future__ import annotations

DEMOCRACY: list[str] = [
    # DEMOCRACY AND VOTING - SHORT
    "My vote was cast this morning.",
    "Already submitted my ballot yesterday.",
    "We trust the democratic process here.",
    "Our district elected a new representative.",
    "Just registered to vote last week.",
    "Polls close at eight tonight apparently.",
    "Volunteering at the precinct this weekend.",
    "Democracy depends entirely on participation.",
    "Majority rule matters most to me.",
    "That recount changed absolutely nothing.",
    "Universal suffrage deserves our support.",
    "Every single citizen deserves a vote.",
    "Witnessing voter suppression changed my perspective.",
    "Turnout was historically low this cycle.",
    "Electoral reform has been my passion.",
    # DEMOCRACY AND VOTING - MEDIUM
    "Proportional representation would better reflect our diverse population honestly.",
    "Abolishing the electoral college would finally embrace direct democracy here.",
    "Standing in line for three hours just to cast a ballot felt absurd.",
    "Gerrymandering in this district has made most votes nearly meaningless.",
    "Ranked choice voting would eliminate the spoiler effect entirely.",
    "Our democratic institutions are being tested like never before now.",
    "Witnessing the peaceful transfer of power felt genuinely moving.",
    "Referendum results surprised everyone, including the pollsters themselves.",
    "Advocating for automatic voter registration has been my focus for years.",
    "Primary system reform must happen before the next election cycle.",
    "Civic engagement starts with simply showing up at town halls.",
    "Constitutional republics require informed and active citizens to function properly.",
    "Watching the debates still left me undecided between candidates.",
    "Supermajority thresholds make passing amendments nearly impossible here.",
    "Compulsory voting would transform our political landscape completely.",
    # DEMOCRACY AND VOTING - LONG
    (
        "Expanding early voting access and implementing same-day registration would dramatically increase civic "
        "participation among working-class families who struggle to take time off work."
    ),
    (
        "No functioning democracy exists when partisan redistricting allows politicians to essentially choose their "
        "own voters rather than the other way around."
    ),
    (
        "Spending my entire career fighting for voting rights, watching these new restrictions pass feels like "
        "witnessing decades of progress being systematically dismantled."
    ),
    (
        "Initiative and referendum processes give ordinary citizens a direct voice in policymaking that representative "
        "democracy alone simply cannot provide."
    ),
    (
        "Low voter turnout isn't just apathy but a rational response to a system where money and special interests "
        "seem to matter more than individual votes."
    ),
    (
        "Our founders established a republic, not a pure democracy, because they understood the dangers of unchecked "
        "majority rule trampling minority rights."
    ),
    (
        "Instant runoff voting would not only save taxpayer money on separate primary elections but also encourage "
        "candidates to build broader coalitions."
    ),
    (
        "Filibusters have transformed the Senate from a deliberative body into a legislative graveyard where popular "
        "legislation goes to die."
    ),
    (
        "Participating in the constitutional convention showed firsthand how compromise and negotiation can produce "
        "lasting frameworks for governance."
    ),
    (
        "Independent redistricting commissions are essential because allowing legislators to draw their own district "
        "lines is like letting foxes design the henhouse."
    ),
    # LEGISLATION AND POLICY - SHORT
    "Finally, the bill passed today.",
    "Opposing this proposed amendment completely.",
    "Comprehensive reform is needed immediately.",
    "That veto was overridden successfully.",
    "Lobbied my representative just yesterday.",
    "This policy affects millions directly.",
    "Legislation stalled in committee again.",
    "Bipartisan compromise deserves our support.",
    "Riders killed the entire bill.",
    "Drafting new regulations tonight actually.",
    "Testifying before the subcommittee was intense.",
    "Statutes expire next December unfortunately.",
    "Reviewed the fiscal impact report carefully.",
    "Mandates take effect immediately now.",
    "We amended the original proposal significantly.",
    # LEGISLATION AND POLICY - MEDIUM
    "Omnibus spending bills contain too many unrelated provisions honestly.",
    "Regulatory frameworks we established have prevented countless environmental disasters.",
    "Sunset clauses will force legislators to revisit this issue eventually.",
    "Closing the loopholes that corporations have been exploiting for decades is essential.",
    "Drafting the enabling legislation that created this entire agency was my job.",
    "Unfunded mandates have placed enormous burdens on state governments everywhere.",
    "Attaching controversial amendments to must-pass appropriations bills seems wrong.",
    "Continuing resolutions just kick the can down the road again.",
    "Means-testing would make this entitlement program more sustainable long-term.",
    "Line-item vetoes would give executives far too much unilateral power.",
    "Sunset provisions force regular accountability reviews, which is good.",
    "Reconciliation processes allow bypassing the filibuster on budget matters.",
    "Administrative rulemaking has become a form of legislation by bureaucracy.",
    "Implementation guidelines fundamentally altered the law's original intent.",
    "Executive orders are increasingly replacing actual lawmaking unfortunately.",
    # LEGISLATION AND POLICY - LONG
    (
        "Months of negotiating this bipartisan compromise collapsed at the last minute when party leadership decided "
        "to prioritize political optics over actual governance."
    ),
    (
        "Congressional Budget Office scoring on this proposal shows it would actually reduce the deficit over ten "
        "years, contrary to what opponents have been claiming."
    ),
    (
        "Regulatory capture has transformed many oversight agencies into rubber stamps for the very industries they "
        "were created to monitor and constrain."
    ),
    (
        "Passing continuing resolutions instead of actual budgets creates uncertainty and prevents long-term planning "
        "by federal agencies across the board."
    ),
    (
        "Testifying for three hours before the judiciary committee about the constitutional implications of expanding "
        "executive authority through administrative action was exhausting."
    ),
    (
        "Conference committees completely gutted the provisions fought hardest for, leaving only a hollow shell of the "
        "original reform package."
    ),
    (
        "Comprehensive earmark reform is needed because the current system encourages parochialism and horse-trading "
        "rather than evidence-based policymaking."
    ),
    (
        "Notice and comment periods revealed overwhelming public opposition, but the agency proceeded with the "
        "rulemaking anyway, which erodes trust in government."
    ),
    (
        "Drafting this legislation specifically to address the court's concerns from their previous ruling hopefully "
        "means it will survive constitutional scrutiny this time."
    ),
    (
        "Establishing a dedicated trust fund ensures future congresses can't raid this program's finances to paper "
        "over deficits in the general budget."
    ),
    # GOVERNMENT INSTITUTIONS - SHORT
    "Working at the state capitol daily.",
    "Judiciary remains independent here thankfully.",
    "Our bureaucracy has become incredibly bloated.",
    "Trusting intelligence agencies seems reasonable.",
    "Parliament convenes next Monday finally.",
    "Briefed the cabinet this morning early.",
    "Civil service protects institutional continuity.",
    "Our constitution desperately needs updating.",
    "Separation of powers matters immensely.",
    "That agency exceeded its authority clearly.",
    "Appealing to the ombudsman was necessary.",
    "Inspectors general found serious irregularities.",
    "Federalism allows local experimentation fortunately.",
    "Rule of law deserves our respect.",
    "Commission issued its final report yesterday.",
    # GOVERNMENT INSTITUTIONS - MEDIUM
    "Administrative states have grown far beyond what the founders envisioned.",
    "Checks and balances only work when each branch defends its prerogatives.",
    "Working in three different cabinet departments revealed the inefficiencies firsthand.",
    "Bicameral legislatures create gridlock but also prevent hasty decision-making.",
    "Deep state narratives misunderstand how professional civil servants actually operate.",
    "Constitutional crises were averted only because officials refused unlawful orders.",
    "Expanding the Supreme Court could restore ideological balance and public legitimacy.",
    "Federal systems allow states to serve as laboratories for policy experimentation.",
    "Witnessing institutional rot that accumulates when oversight mechanisms fail was disturbing.",
    "Parliamentary systems produce faster legislation but less deliberation than presidential systems.",
    "Judicial review gives unelected judges too much power over democratically enacted laws.",
    "Executive branches have accumulated powers that rightly belong to the legislature.",
    "Term limits for Supreme Court justices would reduce the stakes of confirmations.",
    "Municipal governments operate under home rule authority granted by state constitutions.",
    "Serving on the independent commission investigating executive branch misconduct was revealing.",
    # GOVERNMENT INSTITUTIONS - LONG
    (
        "Dedicating my career to public service stems from genuinely believing that competent, professional government "
        "institutions are essential for maintaining social order and promoting general welfare."
    ),
    (
        "Framers intentionally created a system of separated powers with overlapping responsibilities specifically to "
        "prevent any single faction from accumulating too much unchecked authority."
    ),
    (
        "Federal bureaucracies get unfairly maligned when most civil servants are dedicated professionals trying to "
        "faithfully execute laws passed by elected representatives."
    ),
    (
        "Constitutional orders depend on informal norms and traditions just as much as written rules, and watching "
        "those unwritten conventions erode has been deeply troubling."
    ),
    (
        "Serving in both legislative and executive branches gave unique perspective on how institutional incentives "
        "shape behavior regardless of individual intentions."
    ),
    (
        "Independent regulatory commission models were designed to insulate certain technical decisions from direct "
        "political pressure, but that independence is increasingly under attack."
    ),
    (
        "Constitutional systems' greatest strength is adaptability, allowing us to address challenges the founders "
        "could never have anticipated through amendment and interpretation."
    ),
    (
        "Presidential power growth at the expense of congressional authority represents a fundamental shift in our "
        "constitutional balance that transcends partisan politics."
    ),
    (
        "Restoring Congress's capacity for independent policy analysis is essential because lawmakers have become too "
        "dependent on outside interest groups for expertise."
    ),
    (
        "Judicial confirmation processes have become so politicized that qualified nominees are rejected based on "
        "ideology rather than competence or character."
    ),
    # AUTHORITARIANISM AND TYRANNY - SHORT
    "Escaping the dictatorship was barely possible.",
    "Regimes silenced all opposition brutally.",
    "Authoritarian drift concerns me deeply.",
    "Dissent was brutally suppressed there.",
    "Juntas seized power overnight suddenly.",
    "Witnessing political prisoners changed everything.",
    "Strongmen consolidated all power rapidly.",
    "Fleeing the totalitarian state saved us.",
    "Secret police monitored everyone constantly.",
    "Speaking against the despot was risky.",
    "Coups succeeded without any resistance.",
    "Family members were lost to purges.",
    "Autocrats banned free assembly entirely.",
    "Documenting human rights abuses became essential.",
    "Tyrants dissolved parliament completely then.",
    # AUTHORITARIANISM AND TYRANNY - MEDIUM
    "Watching democracy erode gradually through supposedly legal means and emergency decrees was terrifying.",
    "Personality cults around leaders have reached genuinely disturbing proportions now.",
    "Surveillance states they've built make meaningful dissent nearly impossible.",
    "Fleeing became necessary when emergency powers became permanent and the constitution was suspended.",
    "Parallels to nineteen thirties Europe are impossible to ignore anymore honestly.",
    "Propaganda apparatuses have made it impossible to distinguish truth from fiction.",
    "Witnessing show trials where predetermined verdicts followed scripted confessions was horrifying.",
    "One-party states eliminated any institutional check on executive power entirely.",
    "Sleepwalking into soft authoritarianism through democratic backsliding seems increasingly likely.",
    "Militarization of police has transformed them into instruments of political control.",
    "Surviving the reign of terror meant keeping my head down and mouth shut.",
    "Censorship has become so pervasive that people self-censor without even realizing it.",
    "Competitive authoritarianism uses democratic trappings to legitimize fundamentally undemocratic rule.",
    "Kleptocracies siphoned billions while ordinary people struggled to afford basic necessities.",
    "Documenting systematic torture at detention facilities became impossible before being forced to flee.",
    # AUTHORITARIANISM AND TYRANNY - LONG
    (
        "Growing up under a totalitarian system meant the state controlled not just political life but every aspect of "
        "existence from education to employment to personal relationships."
    ),
    (
        "Transitions from democracy to dictatorship happened so gradually that most people didn't recognize the danger "
        "until their freedoms had already been stripped away entirely."
    ),
    (
        "Tyranny's hallmark is not just concentrated power but the deliberate destruction of any institution or "
        "organization that might challenge the regime's total control."
    ),
    (
        "Watching the independent judiciary get systematically packed with loyalists until constitutional constraints "
        "on executive power became completely meaningless in practice was devastating."
    ),
    (
        "Insidious forms of authoritarianism maintain democratic facades like elections and parliaments while "
        "hollowing out their actual substance and meaning entirely."
    ),
    (
        "Cults of personality around supreme leaders demanded not just obedience but genuine enthusiasm, and those who "
        "couldn't convincingly perform loyalty were suspect."
    ),
    (
        "Escaping across the border at night with nothing but the clothes on my back meant leaving behind everyone and "
        "everything ever known."
    ),
    (
        "Regime legitimacy rested entirely on nationalist mythology and manufactured external threats that justified "
        "permanent emergency rule and suspension of civil liberties."
    ),
    (
        "Neighbors informed on neighbors, family members betrayed each other, and friendships dissolved as the "
        "surveillance state turned everyone into potential collaborators."
    ),
    (
        "Controlled press presented such a distorted picture of reality that people who consumed only state media "
        "lived in an entirely different factual universe."
    ),
]
