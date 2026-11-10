"""Politics prompts about socialism, conservatism, liberalism, and international relations."""

from __future__ import annotations

IDEOLOGIES: list[str] = [
    # SOCIALISM AND COMMUNISM - SHORT
    "Joining the workers' collective felt right.",
    "Means of production belong collectively here.",
    "Economic democracy matters deeply to us.",
    "Communes share all resources equally.",
    "Nationalizing key industries makes sense.",
    "Proletariat will rise eventually someday.",
    "Bourgeois exploitation deserves complete rejection.",
    "Cooperative models work better honestly.",
    "Wealth redistribution is absolutely necessary.",
    "State-owned factories dominated the economy.",
    "Studying Marxist theory extensively was enlightening.",
    "Central planners allocated everything inefficiently.",
    "Living under state socialism was difficult.",
    "Collectivization devastated agriculture completely.",
    "Democratic socialism specifically deserves support.",
    # SOCIALISM AND COMMUNISM - MEDIUM
    "Distinctions between socialism and social democracy confuse most Americans honestly.",
    "Experiencing the failures of central planning and the shortages it created firsthand was eye-opening.",
    "Worker ownership of enterprises would transform labor relations fundamentally.",
    "Vanguard parties claimed to represent workers while actually substituting for them.",
    "Universal public services deserve support but total state control of the economy doesn't.",
    "Command economies produced surpluses of unwanted goods and shortages of necessities constantly.",
    "Market socialism combines the efficiency of markets with equitable distribution effectively.",
    "Abolishing private property doesn't automatically create egalitarian societies as we learned.",
    "Living through the transition from communism showed how difficult transformation was.",
    "Nomenclatura became a new ruling class despite officially classless ideology.",
    "Socialism requires democracy or it inevitably degenerates into bureaucratic despotism.",
    "Five-year plan targets bore no relation to actual economic needs or capacities.",
    "Robust public ownership of utilities makes sense while maintaining private enterprise elsewhere.",
    "Revolutions devoured their own children as successive purges eliminated old Bolsheviks.",
    "Scandinavian social democracy offers a better model than Soviet-style socialism.",
    # SOCIALISM AND COMMUNISM - LONG
    (
        "Growing up in a nominally socialist state meant the gap between egalitarian rhetoric and the reality of party "
        "privilege was a constant source of cynicism."
    ),
    (
        "Planned economies eliminated unemployment but also eliminated consumer choice, worker autonomy, and any "
        "meaningful connection between effort and reward."
    ),
    (
        "Capitalism generates immense wealth but distributes it so unequally that democratic socialism represents the "
        "only viable path to broadly shared prosperity."
    ),
    (
        "Waiting in lines for hours to purchase basic necessities while party officials shopped in special stores "
        "stocked with imported Western goods was infuriating."
    ),
    (
        "Soviet communism's collapse discredited not just Leninist vanguardism but unfairly tainted all forms of "
        "collective economic organization."
    ),
    (
        "Agricultural collectivization destroyed traditional farming communities and produced famines that killed "
        "millions while ideologues insisted the policy was succeeding brilliantly."
    ),
    (
        "Socializing healthcare, education, and essential infrastructure while preserving market mechanisms for "
        "consumer goods and services where competition benefits everyone makes sense."
    ),
    (
        "Workers' councils that briefly flourished before being crushed represented a genuinely democratic alternative "
        "to both capitalism and authoritarian state socialism."
    ),
    (
        "Witnessing the Berlin Wall fall brought both joy at freedom's triumph and uncertainty about what capitalism "
        "would bring to people unprepared for it."
    ),
    (
        "Socialist calculation debates proved that without market prices, central planners lack the information "
        "necessary to efficiently allocate resources across complex modern economies."
    ),
    # CONSERVATISM AND TRADITION - SHORT
    "Cherishing our established traditions matters.",
    "Constitutions must be preserved carefully.",
    "Radical social engineering deserves opposition.",
    "Traditional values guide my politics.",
    "Limited government is my principle.",
    "Free markets allocate resources best.",
    "Strong national defense is essential.",
    "Individual liberty matters most here.",
    "Utopian social schemes deserve distrust.",
    "Family remains society's true foundation.",
    "Incremental change only seems wise.",
    "Local communities know their needs.",
    "Personal responsibility is paramount always.",
    "Administrative states constantly overreach authority.",
    "Law and order deserve support.",
    # CONSERVATISM AND TRADITION - MEDIUM
    "Society's accumulated wisdom deserves more respect than abstract theoretical schemes honestly.",
    "Conserving institutions that have evolved over centuries to meet human needs is essential.",
    "Law should reflect enduring moral principles, not passing popular fancies.",
    "Erosion of mediating institutions between individual and state concerns me deeply.",
    "Federalism matters because distant bureaucracies cannot understand local circumstances.",
    "Progressive income taxes punish success and discourage the entrepreneurship we need.",
    "Judicial activism undermines democracy by substituting judges' preferences for legislation.",
    "Strong borders are necessary because national sovereignty requires control over who enters.",
    "Religious traditions provide moral foundations that secular philosophy simply cannot replace.",
    "Welfare states have undermined personal initiative and created cycles of dependency.",
    "Deregulation is important because bureaucratic rules strangle innovation and economic growth.",
    "Culture has shifted so far left that yesterday's liberals seem conservative today.",
    "Environmental regulations impose costs that far exceed their actual benefits.",
    "Western civilization must be defended against those who would deconstruct its achievements.",
    "Equality of opportunity matters, not government-mandated equality of outcomes.",
    # CONSERVATISM AND TRADITION - LONG
    (
        "Conservative philosophy fundamentally recognizes that human nature is flawed and that utopian schemes to "
        "perfect society inevitably produce unintended consequences worse than the problems."
    ),
    (
        "Approaching inherited institutions with humility means recognizing they embody practical wisdom accumulated "
        "over generations that purely theoretical analysis cannot fully appreciate or replicate."
    ),
    (
        "Centralized federal power growth has undermined the constitutional balance that founders carefully designed "
        "to preserve liberty through divided and limited government."
    ),
    (
        "Administrative states have accumulated quasi-legislative and quasi-judicial powers that make unelected "
        "bureaucrats effectively unaccountable to either citizens or their elected representatives."
    ),
    (
        "Family, church, and local community are the natural institutions that nurture virtue and transmit culture far "
        "more effectively than any government program ever could."
    ),
    (
        "Restoring constitutional limits on federal power is essential because Washington dictating to states violates "
        "federalism principles essential to liberty."
    ),
    (
        "Free markets generate prosperity through voluntary exchange while government intervention creates winners and "
        "losers based on political connections rather than merit."
    ),
    (
        "Originalist approaches to constitutional interpretation constrain judges to apply the law as written rather "
        "than inventing new rights based on evolving personal preferences."
    ),
    (
        "Religious practice decline has removed a crucial source of moral formation that secular education and "
        "therapeutic culture cannot adequately replace."
    ),
    (
        "Resisting the progressive impulse to transform society according to abstract ideals is necessary because such "
        "experiments have historically produced catastrophic human suffering."
    ),
    # LIBERALISM AND PROGRESSIVISM - SHORT
    "Marching for civil rights feels essential.",
    "Progress requires bold action now.",
    "Expanding social programs is necessary.",
    "Marginalized communities deserve justice finally.",
    "Systemic reform is absolutely essential.",
    "Environmental protection is non-negotiable.",
    "Income equality deserves our advocacy.",
    "Healthcare is a fundamental human right.",
    "Criminal justice reform is overdue.",
    "Wealthy people should pay more.",
    "Fighting discrimination actively matters everywhere.",
    "Workers deserve union representation always.",
    "Government should help people directly.",
    "Education funding needs increasing dramatically.",
    "Reproductive rights deserve complete support.",
    # LIBERALISM AND PROGRESSIVISM - MEDIUM
    "Intersectionality reveals how different forms of oppression compound and reinforce each other.",
    "Structural solutions are needed because individual goodwill cannot overcome systemic inequities.",
    "Economic security is a prerequisite for meaningful political liberty.",
    "Social safety nets represent our collective commitment to human dignity and welfare.",
    "Affirmative action is necessary remedy for centuries of documented discrimination.",
    "Addressing climate change is essential because future generations deserve a habitable planet.",
    "Universal basic income could provide economic security in an automated economy.",
    "Prison industrial complexes have created mass incarceration that devastates entire communities.",
    "Housing is a right and government should guarantee shelter for everyone.",
    "Campaign finance reform is needed because money in politics drowns out ordinary voices.",
    "Medicare for all makes sense because healthcare access shouldn't depend on employment status.",
    "Minimum wages should be indexed to inflation and local cost of living.",
    "Student debt cancellation would stimulate the economy and expand opportunity.",
    "Reparations are needed to address the compounding effects of historical injustice.",
    "Immigration enriches our society and welcoming more newcomers makes sense.",
    # LIBERALISM AND PROGRESSIVISM - LONG
    (
        "Government has a positive role in correcting market failures, reducing inequality, and ensuring that "
        "prosperity is broadly shared rather than concentrated among the few."
    ),
    (
        "Genuine equality of opportunity is impossible when children born into poverty face compounding disadvantages "
        "in health, education, and social capital from their earliest years."
    ),
    (
        "Civil rights movement's unfinished business requires not just removing legal barriers but actively "
        "dismantling structures that perpetuate racial disparities across every institution."
    ),
    (
        "Environmental crises demand immediate transformation of our energy systems, transportation infrastructure, "
        "and agricultural practices, whatever the short-term economic disruption might cost."
    ),
    (
        "Significantly higher taxes on extreme wealth are justified because billionaires enjoying massive fortunes "
        "while people die from lack of healthcare represents a moral obscenity."
    ),
    (
        "Comprehensive immigration reform must provide pathways to citizenship for undocumented residents who have "
        "built lives here while contributing to their communities for decades."
    ),
    (
        "Labor movement decline explains much of the rising inequality because workers without collective bargaining "
        "power cannot negotiate fair share of productivity gains."
    ),
    (
        "Criminal justice systems from policing through prosecution to incarceration are riddled with racial bias that "
        "requires fundamental restructuring rather than incremental tinkering."
    ),
    (
        "Access to quality healthcare, education, housing, and nutritious food should be guaranteed rights rather than "
        "commodities distributed according to ability to pay."
    ),
    (
        "Reckoning honestly with our history of colonialism, slavery, and dispossession is essential because healing "
        "requires acknowledgment before truly building an inclusive multiracial democracy."
    ),
    # INTERNATIONAL RELATIONS - SHORT
    "Multilateral diplomacy deserves strong support.",
    "Alliances remain strategically vital today.",
    "Unilateral military intervention seems wrong.",
    "Sanctions have crippled their economy.",
    "Witnessing peace negotiations was powerful.",
    "Treaties were finally ratified recently.",
    "International humanitarian law matters deeply.",
    "Embargoes affect ordinary civilians primarily.",
    "Collective security is my principle.",
    "Arms races must stop immediately.",
    "Attending the summit personally was memorable.",
    "Détente reduced nuclear tensions significantly.",
    "United Nations deserves our support.",
    "Territorial disputes remain unresolved unfortunately.",
    "Human rights advocacy matters globally.",
    # INTERNATIONAL RELATIONS - MEDIUM
    "Liberal internationalism underestimated nationalism's enduring power in world politics.",
    "Prioritizing diplomacy over military force in pursuing foreign policy objectives makes sense.",
    "Multilateral institutions constrain great powers and protect smaller nations effectively.",
    "Balance of power systems prevented hegemony but produced devastating great power wars.",
    "Humanitarian intervention is justified when governments commit atrocities against their own populations.",
    "Sphere of influence concepts violate the sovereignty of smaller neighboring states.",
    "Economic interdependence makes major power conflict increasingly irrational and unlikely.",
    "Reforming international institutions to reflect the current distribution of power is necessary.",
    "Nuclear deterrence has kept great powers from direct military confrontation.",
    "Proxy wars devastated that country while great powers avoided direct engagement.",
    "International criminal court jurisdiction over crimes against humanity deserves support.",
    "Non-proliferation regimes have largely prevented the spread of nuclear weapons capabilities.",
    "Soft power through cultural influence often achieves more than military coercion.",
    "Nation-building failed when we attempted to impose democracy externally.",
    "Strategic ambiguity sometimes serves security interests better than explicit commitments.",
    # INTERNATIONAL RELATIONS - LONG
    (
        "Rules-based international order built after World War Two is under unprecedented strain from rising powers "
        "that benefited from it but now challenge its foundational principles."
    ),
    (
        "Investing more in development assistance makes sense because reducing global poverty strengthens stability, "
        "expands markets for our products, and reduces migration pressure at our borders."
    ),
    (
        "Responsibility to protect doctrine establishes legitimate grounds for intervention when states fail to "
        "protect their populations from genocide, ethnic cleansing, and crimes against humanity."
    ),
    (
        "Great power competition we're entering will test whether democratic societies can mobilize sustained "
        "responses to authoritarian challenges without sacrificing the values that define us."
    ),
    (
        "Regional integration through economic unions and security alliances has transformed interstate relations in "
        "ways that make traditional great power conflict increasingly obsolete."
    ),
    (
        "Military power's limits in achieving political objectives became clear when occupying forces could win every "
        "battle but still lose the war against determined insurgencies."
    ),
    (
        "Climate change represents the most significant security threat because its effects will destabilize regions, "
        "create refugee flows, and intensify resource competition globally."
    ),
    (
        "Autonomous weapons systems proliferation raises profound questions about accountability and the laws of armed "
        "conflict that the international community has barely begun addressing."
    ),
    (
        "Maintaining forward-deployed forces and security commitments is essential because abandoning allies would "
        "destroy the credibility essential for effective deterrence and alliance cohesion."
    ),
    (
        "Tensions between sovereignty and universal human rights remain unresolved because the international community "
        "still lacks legitimate mechanisms to enforce global norms against resistant states."
    ),
]
