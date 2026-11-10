"""Religious prompts: long reflections, praise, liturgy, and theology, then casual speech and vocabulary."""

from __future__ import annotations

LITURGY: list[str] = [
    # LONG - QUESTIONS & REFLECTIONS
    (
        "Have you ever knelt in an empty cathedral and felt the Divine's presence so tangibly that tears streamed down "
        "your face in overwhelming holy encounter?"
    ),
    (
        "What does it mean to take up your cross daily when the world offers comfortable alternatives to the narrow "
        "path of discipleship and self denial?"
    ),
    (
        "How can we claim to love the Almighty whom we have not seen if we do not love our brothers and sisters whom "
        "we see daily?"
    ),
    (
        "When did you last share your faith with someone who needed to hear the good news of salvation through the "
        "Messiah's finished work on Calvary?"
    ),
    (
        "Do you believe that prayer actually changes circumstances, or has it become merely religious routine devoid "
        "of expectation and genuine communion with the Divine?"
    ),
    (
        "What idols have crept into your heart, stealing devotion and affection that rightfully belongs to the "
        "Almighty alone who is worthy of all worship?"
    ),
    (
        "Are you living in the freedom the Redeemer purchased, or have you returned to the slavery of sin that once "
        "held you captive in chains?"
    ),
    (
        "Have you made your confession to a priest recently, unburdening your soul in the sacrament of reconciliation "
        "and receiving absolution for your transgressions?"
    ),
    (
        "Do you observe the Sabbath as a holy day of rest, or has the world's busyness crowded out this commandment "
        "from your weekly rhythm?"
    ),
    (
        "Have you participated in the Eucharistic feast lately, receiving the body and blood of the Savior in the "
        "sacred mystery of communion with Him?"
    ),
    (
        "What would it look like if every believer tithed faithfully, giving the firstfruits of their income to "
        "support the temple's work and the poor?"
    ),
    (
        "Do you fast and pray during Lent, denying the flesh to strengthen the spirit and draw closer to the Almighty "
        "through sacrificial discipline?"
    ),
    (
        "Have you been confirmed in the faith, receiving the Holy Spirit's gifts through the laying on of hands by "
        "bishop or elder in your tradition?"
    ),
    (
        "When did you last go on a spiritual retreat, stepping away from daily distractions to hear the still small "
        "voice of the Divine speaking?"
    ),
    (
        "Are you part of a small group or fellowship where believers spur one another toward love and good works as "
        "Hebrews instructs us?"
    ),
    # LONG - EXCLAMATIONS OF PRAISE
    (
        "What a glorious day it will be when we see the Savior face to face, every tear wiped away, sorrow and death "
        "gone forevermore!"
    ),
    (
        "How magnificent is the grace of the Divine that would send His only Son to die for sinners who deserved "
        "nothing but eternal separation!"
    ),
    (
        "Praise Jehovah for He is good, His love endures forever, His faithfulness continues through all generations "
        "who call upon His holy covenant name!"
    ),
    (
        "The Almighty who spoke the universe into existence knows my name and calls me beloved child, what amazing "
        "love beyond human comprehension this is!"
    ),
    (
        "Oh, that people would praise the Sovereign for wonderful works to humanity, for He satisfies the longing soul "
        "with good things abundantly!"
    ),
    (
        "How beautiful upon the mountains are the feet of those who bring good news, proclaiming peace and salvation "
        "to a lost and dying world!"
    ),
    (
        "The Redeemer has done great things for us, filling hearts with joy that overflows from souls transformed by "
        "matchless grace and tender mercy!"
    ),
    (
        "What an honor to be called servants of the Most High, chosen before the foundation of the world to be holy "
        "and blameless!"
    ),
    (
        "The love of the Messiah compels us to live not for ourselves but for Him who died and rose that we might have "
        "eternal life!"
    ),
    (
        "Glory to Elohim in the highest heaven, and on earth peace to those on whom divine favor rests, for the Savior "
        "has been born!"
    ),
    (
        "Worthy is the Lamb who was slain to receive power and riches and wisdom and strength and honor and glory and "
        "blessing forever!"
    ),
    (
        "The trumpet shall sound and the dead shall be raised incorruptible, and we shall all be changed in the "
        "twinkling of an eye!"
    ),
    (
        "Behold, the Bridegroom comes! Trim your lamps and go out to meet Him, for the wedding feast of the Lamb is "
        "prepared and waiting!"
    ),
    (
        "How awesome is this place! This is none other than the house of Elohim, and this is the gate of heaven where "
        "angels ascend!"
    ),
    (
        "The ransomed of Jehovah shall return to Zion with singing, everlasting joy upon their heads, sorrow and "
        "sighing fleeing away forever!"
    ),
    # LONG - PRIESTLY & LITURGICAL SPEECH
    (
        "Dearly beloved, we are gathered here in the sight of the Almighty and this congregation to join this man and "
        "woman in holy matrimony."
    ),
    (
        "In the name of the Father, and of the Son, and of the Holy Spirit, I baptize you into the death and "
        "resurrection of the Messiah."
    ),
    (
        "The body of Christ, broken for you. The blood of Christ, shed for you. Take, eat, and remember His sacrifice "
        "until He comes again."
    ),
    (
        "Go in peace to love and serve the Sovereign. The Mass is ended, thanks be to the Almighty. Ite, missa est, go "
        "forth and proclaim."
    ),
    (
        "May the Almighty bless you and keep you. May His face shine upon you and be gracious. May He lift His "
        "countenance and give peace."
    ),
    (
        "I absolve you from your sins in the name of the Father, the Son, and the Holy Spirit. Your penance is three "
        "Our Fathers and Hail Marys."
    ),
    (
        "Let us confess our sins to Almighty Elohim and to one another, that we may be prepared to celebrate the "
        "sacred mysteries worthily."
    ),
    (
        "The peace of the Sovereign be with you always. And also with you. Let us offer one another a sign of peace in "
        "holy love."
    ),
    (
        "Lift up your hearts. We lift them up to the Master. Let us give thanks to Jehovah our Provider. It is right "
        "to give thanks and praise."
    ),
    (
        "Through Him, with Him, in Him, in the unity of the Holy Spirit, all glory and honor is Yours, Almighty "
        "Father, forever and ever. Amen."
    ),
    (
        "Receive the Holy Spirit. Whose sins you forgive are forgiven them, and whose sins you retain are retained. Go "
        "in peace to serve."
    ),
    (
        "I commend your soul to Almighty Elohim, and your body to the ground, earth to earth, ashes to ashes, dust to "
        "dust, awaiting resurrection."
    ),
    (
        "This is the Lamb of the Divine who takes away the sins of the world. Happy are those called to His supper of "
        "sacred communion."
    ),
    (
        "Be sealed with the gift of the Holy Spirit. The chrism of salvation, in the Messiah unto eternal life. Go "
        "forth as a soldier of faith."
    ),
    (
        "The reading is from the holy Gospel according to Matthew, Mark, Luke, or John. Glory to You, O Sovereign. The "
        "Gospel of the Master."
    ),
    # LONG - THEOLOGICAL TRUTHS
    (
        "Justification by faith alone through grace alone in the Messiah alone brings peace with the Almighty that no "
        "human works or religious rituals can ever offer."
    ),
    (
        "The sovereignty of Elohim over all things gives confidence that nothing happens outside divine will, working "
        "all things together for good according to purpose."
    ),
    (
        "I believe in the bodily resurrection of Yeshua the Messiah, the cornerstone of our faith and the foundation "
        "of our hope for eternal life."
    ),
    (
        "The doctrine of the Trinity reveals the Divine as Father, Son, and Holy Spirit, three persons yet one "
        "essence, mysteriously united in love."
    ),
    (
        "Salvation cannot be earned by works but is received by grace through faith as a gift, lest anyone should "
        "boast before the throne."
    ),
    (
        "The virgin birth testifies to the Messiah's divine nature, conceived by the Holy Spirit in Mary's womb, fully "
        "human and fully divine."
    ),
    (
        "I hold to the authority of Scripture as the inspired, inerrant Word of Elohim, our sole infallible rule for "
        "faith and practice."
    ),
    (
        "The atonement satisfies divine justice while demonstrating love, reconciling sinners to their holy Creator "
        "through the Lamb's substitutionary sacrifice on Calvary."
    ),
    (
        "Sanctification is the Spirit's ongoing work, conforming believers progressively to the Messiah's image "
        "through trials, discipline, and the means of grace."
    ),
    (
        "The second coming is our blessed hope, when the Risen One will return in glory with angels to judge the "
        "living and the dead."
    ),
    (
        "Eternal security rests in the Almighty's promise that none shall snatch believers from the Father's hand who "
        "holds them by sovereign grace."
    ),
    "The church is the Bride of the Messiah, called out from the world to be holy, set apart as a kingdom of priests.",
    (
        "Baptism symbolizes death to sin and resurrection to new life, identifying believers with the Messiah's burial "
        "and rising from the tomb."
    ),
    (
        "The Eucharist proclaims the Savior's death until He comes, a sacred remembrance and mysterious participation "
        "in His body and blood truly present."
    ),
    (
        "Election speaks to divine sovereign choice before the foundation of the world, choosing those who would "
        "believe by irresistible grace and calling."
    ),
    # ADDITIONAL - CASUAL RELIGIOUS SPEECH (varied)
    (
        "I've been really feeling the Spirit's presence during my quiet time lately, it's been so refreshing for my "
        "weary soul."
    ),
    "Can you believe how good the Almighty has been to us? I'm just in awe of His faithfulness through everything.",
    "I'll be lifting you up in prayer about that situation. The Sovereign's got this and He loves you deeply.",
    (
        "Reading through Romans again, and Paul's epistles just hit different when you're going through trials and "
        "tribulations."
    ),
    (
        "The worship service this Sunday was amazing. The praise really moved my spirit and I felt so alive in His "
        "presence."
    ),
    "I keep meditating on that passage in Jeremiah about plans to prosper and not to harm, to give hope and future.",
    "The Divine really convicted me about my attitude lately. I needed that humbling experience so much for my growth.",
    "I just love how Providence works everything together for good, even the hard stuff we can't understand right now.",
    "Been feeling called to fast and pray about this major decision. Want to make sure it's the Almighty's will.",
    "The small group Bible study has been such a blessing. Iron sharpening iron like Proverbs describes happens there.",
    "I'm standing on that promise in Isaiah 41:10 that the Sovereign will strengthen and help me through this valley.",
    "My prayer life has been inconsistent lately, but grace covers even my spiritual laziness and draws me back.",
    "The Messiah really is the best friend you could ever have. He's always there no matter what circumstances arise.",
    "I've been wrestling with doubt but then I remember all the ways the Almighty has shown up before in my life.",
    "Worship music has been getting me through this difficult week. There's just something about praising the Divine.",
    # ADDITIONAL - MORE OBJECTS & VOCABULARY (short)
    "The monstrance displays the Eucharist for adoration.",
    "Genuflect before the Blessed Sacrament in reverence.",
    "The aspergillum sprinkles holy water on the congregation.",
    "Stations of the Cross line the cathedral walls.",
    "The thurible swings, releasing fragrant clouds of incense.",
    "Vestments of green mark ordinary time in the liturgical calendar.",
    "The chasuble and stole indicate the priest's sacred office.",
    "Canticles of praise rise from the monastic choir stalls.",
    "The antiphonal chanting echoes through vaulted stone arches.",
    "Prayer beads help count the mysteries of the rosary.",
    "The corporal and purificator prepare for Eucharistic celebration.",
    "Advent wreaths hold four candles marking weeks until Christmas.",
    "The ciborium holds consecrated hosts for communion distribution.",
    "Cassock and surplice clothe the altar servers at Mass.",
    "The paten receives the sacred bread for consecration.",
    "Holy oils are kept in the ambry near the altar.",
    "The sanctuary lamp burns eternally before the tabernacle.",
    "Palms from last year become ashes for Ash Wednesday.",
    "The baptistery houses the font for infant christenings.",
    "The sacristy stores vestments and sacred vessels safely.",
]
