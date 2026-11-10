"""Politics prompts about constitutional law, international relations theory, legislation, and economy."""

from __future__ import annotations

STATECRAFT: list[str] = [
    # CONSTITUTIONAL LAW TECHNICAL - LONG
    (
        "Living constitutionalism versus originalism debate obscures the more fundamental question of what "
        "interpretive approach best serves constitutional purposes across changing circumstances."
    ),
    (
        "Administrative state growth has rendered the nondelegation doctrine's original understanding obsolete, "
        "requiring new frameworks to maintain democratic accountability over regulatory agencies."
    ),
    (
        "Executive power expansion through emergency declarations, signing statements, and prosecutorial discretion "
        "has fundamentally altered the constitutional separation of powers."
    ),
    (
        "Qualified immunity doctrine as currently applied makes it nearly impossible to hold government officials "
        "accountable for constitutional violations, undermining rights enforcement entirely."
    ),
    (
        "Federalism revolution of the Rehnquist Court represented a genuine if incomplete effort to restore "
        "constitutional limits on congressional power."
    ),
    (
        "Structural constitution embodied in separation of powers and federalism may be more important for protecting "
        "liberty than the rights provisions in the Bill of Rights."
    ),
    (
        "Incorporation of the Bill of Rights against states through the Fourteenth Amendment represented legitimate "
        "constitutional development rather than judicial usurpation."
    ),
    (
        "Prophylactic rules the Court creates to protect constitutional rights sometimes sweep more broadly than the "
        "underlying constitutional text strictly requires."
    ),
    (
        "Political safeguards of federalism thesis overstates how effectively the political process protects state "
        "prerogatives against federal encroachment."
    ),
    (
        "Unwritten constitution of traditions, practices, and norms may be as important as the written document for "
        "understanding how our constitutional system actually operates."
    ),
    # INTERNATIONAL RELATIONS THEORY - SHORT
    "Structural realism is embraced entirely here.",
    "Security dilemmas perpetuate international conflict.",
    "Constructivist approaches are studied carefully.",
    "Bandwagoning differs from balancing behavior.",
    "Offensive realism is rejected completely.",
    "Liberal peace thesis seems quite plausible.",
    "Hegemonic stability theory is analyzed closely.",
    "Soft balancing characterizes current dynamics.",
    "Neoliberal institutionalism is firmly supported.",
    "English school offers important middle ground.",
    "Critical security studies is explored deeply.",
    "Multipolarity creates systemic instability potentially.",
    "Normative international theory is embraced.",
    "Copenhagen school securitizes various issues.",
    "Regime complexity is analyzed carefully.",
    "Buck-passing shifts defense burdens strategically.",
    "Strategic culture is studied quite thoroughly.",
    "Entrapment risks alliance commitments sometimes.",
    "Postcolonial IR perspectives are embraced.",
    "Two-level games link domestic and international.",
    # INTERNATIONAL RELATIONS THEORY - MEDIUM
    "Waltzian neorealism's systemic focus neglects important unit-level variation in state behavior.",
    "Democratic peace finding represents the closest thing to an empirical law in international relations.",
    "Wendtian constructivism correctly emphasizes that anarchy is what states make of it.",
    "Offense-defense balance shapes the security dilemma's intensity across different technological eras.",
    "Mearsheimer's offensive realism provides the most parsimonious explanation for great power competition.",
    "Power transition theory predicts conflict when rising powers challenge declining hegemonic orders.",
    "Regime theory explains cooperation even under conditions of anarchy and self-help.",
    "Spiral model and deterrence model generate opposite policy prescriptions under similar circumstances.",
    "Audience costs theory overstates how domestic politics constrain executive foreign policy discretion.",
    "Selectorate theory explains why authoritarian and democratic leaders pursue different grand strategies.",
    "Epistemic communities shape international cooperation by establishing shared causal understandings.",
    "Two-level game framework illuminates how domestic win-sets constrain international bargaining outcomes.",
    "Responsibility to protect norm has developed unevenly and inconsistently in state practice.",
    "Liberal world order rested on American hegemonic power and is declining alongside relative power.",
    "Diversionary war theory lacks robust empirical support despite theoretical plausibility.",
    # INTERNATIONAL RELATIONS THEORY - LONG
    (
        "Classical realist tradition from Thucydides through Machiavelli to Morgenthau offers more nuanced insights "
        "than structural realism's austere systemic parsimony allows."
    ),
    (
        "Rationalist explanations for war emphasizing incomplete information, commitment problems, and issue "
        "indivisibilities provide the most rigorous framework for understanding conflict onset."
    ),
    (
        "English school's distinction between international system, international society, and world society captures "
        "important variation in the depth of international order."
    ),
    (
        "Constructivist turn in international relations theory properly restored attention to ideas, norms, and "
        "identity that rationalist approaches systematically neglected."
    ),
    (
        "Feminist international relations theory reveals how gender hierarchies structure both state behavior and the "
        "discipline's analytical frameworks in previously invisible ways."
    ),
    (
        "Global governance literature addresses how international cooperation occurs through networks and institutions "
        "beyond traditional interstate diplomacy and treaty-making."
    ),
    (
        "Critical security studies appropriately expands the security agenda beyond military threats to include human "
        "security, environmental security, and economic security."
    ),
    (
        "Practice turn in international relations theory emphasizes embodied knowledge and routinized behavior over "
        "explicit strategic calculation."
    ),
    (
        "Historical institutionalist approach to international organizations reveals important path dependencies that "
        "constrain institutional adaptation to changed circumstances."
    ),
    (
        "Post-structural critique of sovereignty as a social construct rather than natural fact has important "
        "implications for how we understand international order."
    ),
    # LEGISLATIVE PROCESS TECHNICAL - SHORT
    "Cloture was invoked successfully yesterday.",
    "Quorum calls revealed many absences.",
    "Unanimous consent agreements are supported.",
    "Engrossment contained transcription errors unfortunately.",
    "Previous question was opposed strongly.",
    "Discharge petitions gathered sufficient signatures.",
    "Roll call votes were requested.",
    "Markup sessions amended bills extensively.",
    "Germaneness requirements deserve support.",
    "Holds blocked floor consideration entirely.",
    "Legislative drafting is studied extensively.",
    "Enrolled bills were presentment-ready finally.",
    "Division votes were requested repeatedly.",
    "Recommittal motions failed quite narrowly.",
    "Byrd rule is supported here.",
    "Conference reports passed unchanged finally.",
    "King-of-the-hill rules were opposed.",
    "Privileged resolutions reached the floor.",
    "Speech or debate clause was invoked.",
    "Sequestration triggered automatic spending cuts.",
    # LEGISLATIVE PROCESS TECHNICAL - MEDIUM
    "Filibusters have transformed from tools for extended debate into routine obstruction.",
    "Budget reconciliation processes circumvent the filibuster but impose substantive constraints on content.",
    "Hastert rule requiring majority-of-the-majority support undermines bipartisan compromise.",
    "Committee of the whole procedure allows the House to operate under more flexible rules.",
    "Germaneness requirements should be stricter to prevent unrelated riders on legislation.",
    "Motions to recommit with instructions give the minority a final amendment opportunity.",
    "Suspension of the rules process has been overused for non-controversial legislation.",
    "Self-executing rules allow the House to deem bills passed without direct recorded votes.",
    "Blue slip tradition gives home-state senators excessive veto power over nominees.",
    "Nuclear option eliminated the filibuster for nominations but not for legislation yet.",
    "Point of order enforcement is essential for maintaining regular legislative procedure.",
    "Omnibus appropriations process bundles multiple spending bills in ways that obscure accountability.",
    "Parliamentarian's role in interpreting chamber rules should be more transparent.",
    "Motions to table offer a procedural way to kill amendments without direct votes.",
    "Reading clerk's role in filibuster procedures has become largely ceremonial.",
    # LEGISLATIVE PROCESS TECHNICAL - LONG
    (
        "Transformation of the Senate from a deliberative body to a supermajoritarian institution through routine "
        "filibuster use represents the most significant informal constitutional change in decades."
    ),
    (
        "Budget reconciliation process created by the Congressional Budget Act has become the primary vehicle for "
        "major legislation because it cannot be filibustered under Senate rules."
    ),
    (
        "Decline of the regular appropriations process in favor of continuing resolutions and omnibus packages has "
        "undermined congressional power of the purse fundamentally."
    ),
    (
        "Increased use of structured rules in the House that limit amendments and debate time has shifted power from "
        "individual members and committees to party leadership."
    ),
    (
        "Demise of earmarks eliminated important lubricant for bipartisan dealmaking without meaningfully reducing "
        "overall spending or improving policy outcomes."
    ),
    (
        "Congressional Review Act's expedited procedures for disapproving agency rules have become more significant as "
        "tools for regulatory rollback under unified government."
    ),
    (
        "War Powers Resolution's procedural framework has been systematically evaded by executives of both parties, "
        "rendering its constraints largely ineffective."
    ),
    (
        "Reconciliation instruction process through which committees receive directives from the budget resolution "
        "shapes what provisions can survive the Byrd rule's extraneous matter test."
    ),
    (
        "Advice and consent function for nominations has become so contentious that executive branch and judicial "
        "vacancies have reached crisis levels."
    ),
    (
        "Enrolled bill doctrine prevents courts from looking behind the authenticated signatures on legislation to "
        "examine whether proper procedures were actually followed."
    ),
    # POLITICAL ECONOMY TECHNICAL - SHORT
    "Public choice theory is studied extensively.",
    "Rent-seeking behavior is pervasive everywhere.",
    "Laissez-faire economics is generally supported.",
    "Regulatory capture distorts policy outcomes.",
    "Collective action problems are analyzed closely.",
    "Pareto frontiers constrain policy possibilities.",
    "Mercantilism is entirely rejected now.",
    "Moral hazard affects bailout decisions significantly.",
    "Institutional economics is studied closely.",
    "Coase theorem has important limits.",
    "Pigouvian taxation approaches are supported.",
    "Adverse selection plagues insurance markets.",
    "Principal-agent problems are analyzed carefully.",
    "Fiscal multipliers remain disputed among economists.",
    "Progressive taxation is firmly supported.",
    "Deadweight loss measures inefficiency clearly.",
    "Ordoliberalism is studied carefully now.",
    "Tragedy of the commons applies here.",
    "Protectionism is generally still opposed.",
    "Externalities justify government intervention sometimes.",
    # POLITICAL ECONOMY TECHNICAL - MEDIUM
    "Olsonian logic of collective action explains why concentrated interests dominate diffuse publics.",
    "Median voter theorem predicts centrist convergence that we don't observe in polarized systems.",
    "Buchanan's constitutional political economy properly emphasizes rules over within-rule choices.",
    "Mundell-Fleming trilemma constrains macroeconomic policy choices for open economies fundamentally.",
    "Washington Consensus prescription for development proved far too simplistic.",
    "Stolper-Samuelson theorem explains distributional conflicts over trade policy between factors.",
    "Williamson's transaction cost economics illuminates the boundaries of firms and markets.",
    "Heckscher-Ohlin model predicts trade patterns based on factor endowment differences.",
    "Rodrik's trilemma between democracy, sovereignty, and hyperglobalization is genuine.",
    "Varieties of capitalism literature reveals important institutional diversity among market economies.",
    "Acemoglu's inclusive institutions thesis provides the most compelling development framework.",
    "Keynesian-monetarist synthesis obscured important remaining disagreements about macroeconomic policy.",
    "Hayek's knowledge problem argument against central planning remains fundamentally sound.",
    "Bretton Woods system's collapse fundamentally transformed international monetary relations.",
    "Polanyi's double movement captures the inherent instability of market society.",
    # POLITICAL ECONOMY TECHNICAL - LONG
    (
        "Public choice revolution properly subjected government behavior to the same rational actor assumptions that "
        "economists apply to market behavior, revealing systematic pathologies."
    ),
    (
        "Credible commitment problem explains why some countries can sustain policies that require long-term "
        "consistency while others remain trapped in time-inconsistent equilibria."
    ),
    (
        "Comparative institutional analysis approach pioneered by Douglass North provides essential tools for "
        "understanding why some societies develop effective governance and others don't."
    ),
    (
        "Embedded liberalism compromise that sustained postwar international economic cooperation has eroded as "
        "globalization and financialization have undermined national policy autonomy."
    ),
    (
        "Developmental state model of East Asian industrialization demonstrated that strategic government intervention "
        "can accelerate growth under specific institutional conditions."
    ),
    (
        "Fiscal policy trilemma shows that governments cannot simultaneously maintain low taxes, generous social "
        "spending, and sustainable debt without eventual adjustment."
    ),
    (
        "Political business cycle literature reveals how electoral incentives systematically distort macroeconomic "
        "policy toward short-term stimulus before elections."
    ),
    (
        "Second-generation fiscal federalism literature moves beyond the Tiebout model to incorporate political "
        "economy considerations about intergovernmental bargaining and soft budget constraints."
    ),
    (
        "Resource curse literature demonstrates that natural resource wealth often undermines rather than promotes "
        "economic development through multiple political economy channels."
    ),
    (
        "Colonialism's institutional legacy thesis argues that extractive colonial institutions persist and explain "
        "contemporary development failures in formerly colonized regions."
    ),
    # BUREAUCRACY AND ADMINISTRATION - SHORT
    "Bureaucratic politics is studied closely here.",
    "Iron triangles captured that policy area.",
    "Merit-based civil service is supported.",
    "Spoils systems corrupted governance entirely.",
    "Street-level bureaucracy is analyzed carefully.",
    "Red tape strangled innovation completely.",
    "Politicization of agencies is opposed.",
    "Pendleton Act reformed federal hiring.",
    "Regulatory implementation is studied carefully.",
    "Policy feedback shapes political preferences.",
    "Administrative procedure requirements are supported.",
    "Weberian ideal types apply here.",
    "Bureaucratic discretion is analyzed carefully.",
    "Fire alarm oversight model works well.",
    "Unitary executive theory is opposed.",
    "Senior Executive Service professionalized leadership.",
    "Administrative law is studied closely.",
    "Notice-and-comment rulemaking succeeded overall.",
    "Whistleblower protections are absolutely supported.",
    "Inspectorates function independently here thankfully.",
]
