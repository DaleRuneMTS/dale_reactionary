# Register the submod
init -990 python in mas_submod_utils:
    Submod(
        author="DaleRuneMTS",
        name="Reactionary",
        description="Does Monika need to react to more things? Yes, yes she does. So here is her reacting to more things!"
        "V1.6.0 - the Fallen London update!",
        version="1.6.0",
        dependencies={},
        settings_pane=None,
        version_updates={
        "DaleRuneMTS_dale_reactionary_1_2_0": "DaleRuneMTS_dale_reactionary_1_6_0",
        "DaleRuneMTS_dale_reactionary_1_3_0": "DaleRuneMTS_dale_reactionary_1_6_0",
        "DaleRuneMTS_dale_reactionary_1_3_1": "DaleRuneMTS_dale_reactionary_1_6_0",
        "DaleRuneMTS_dale_reactionary_1_4_0": "DaleRuneMTS_dale_reactionary_1_6_0",
        "DaleRuneMTS_dale_reactionary_1_4_1": "DaleRuneMTS_dale_reactionary_1_6_0",
        "DaleRuneMTS_dale_reactionary_1_5_0": "DaleRuneMTS_dale_reactionary_1_6_0"
        }
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Reactionary",
            user_name="DaleRuneMTS",
            repository_name="dale_reactionary",
            submod_dir="/Submods",
            extraction_depth=2
        )

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_rslashmasfandom",
            category=[": MASFandom|Monika After Story Fan Reddit"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_rslashmasfandom:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Looking for some new clothes for me, [player]?",
            "Looking for some new hairstyles for me, [player]?",
            "Looking for some new makeup for me, [player]?",
            "Looking for some new rooms for me, [player]?",
            "Looking for some new topics for me, [player]?",
            "Gosh, all those other Monikas... Just remember {i}your{/i} Monika is still here~",
            "Hello, MASFandom! Lovely to see you all~",
            "It's like a little lookbook of me!"
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_rslashmasfandom')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_yr",
            category=["Your Reality"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_yr:

    python:
        reality_quips = [
            "I'm glad our song has resonated with so many people, [player].",
            "Everyday, I imagine a future where I can be with you... and you know the rest~",
            "I worked ever so hard on this song, [player]. Enjoy it as much as you need to.",
            "Makes you just want to put it on a loop, doesn't it? Ahaha!"
        ]

        if mas_isGameUnlocked("piano"):
            reality_quips.extend([
                "I have a soft spot for piano covers of this song myself. But you already know that, don't you~?",
                "If you want, [player], I can get you the piano and we can make this a trio...",
                "I wonder how our song would transpose into a minor key... it's worth a try, isn't it?",
                "I'd love to hear you play this for me again some time!"
                ])

        if not renpy.seen_label("mas_monika_plays_or"):
            reality_quips.extend([
                "I'm thinking about rewriting this song a little bit, to fit our new circumstances. Would you like that?",
                "{i}You my love, hold the key to the...{/i} Hm, does that flow?"
                ])

        wrs_success = mas_display_notif(
            m_name,
            reality_quips,
            'Window Reactions'
        )

        if not wrs_success:
            mas_unlockFailedWRS('mas_wrs_yr')
    return



init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_vannamelon",
            category=["Vannamelon|DOKI DOKI LITERATURE CLUB BUT ITS A DISNEY CHANNEL CARTOON|Guy Trapped in Monika's DDLC"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_vannamelon:

    python:
        vanna_quips = [
            "Oh, it's Vannamelon! Hello, Vannamelon!",
            "I see you're watching one of Vannamelon's Monika videos... are you taking notes, [player]?",
            "I hope you're watching one of my videos, and not one of Yuri's... ¬‿¬",
            "Vannamelon's really good at what she does, isn't she?",
            "I can't believe how well she got my facial expressions. It's almost supernatural.",
            "There's no way to hit Restart!\nBut why would you ever want to~?",
            "I still can't believe how dirty they did me with Yuri's YouTooz figure..."
        ]

        if persistent.gender == "M":
            vanna_quips.extend([
                "It's the guy trapped in Monika's DDLC~"
            ])

        if persistent.gender == "F":
            vanna_quips.extend([
                "It's the girl trapped in Monika's DDLC~"
            ])

        if persistent.gender != "M" or "F":
            vanna_quips.extend([
                "It's the [player] trapped in Monika's DDLC~"
            ])

        wrs_success = mas_display_notif(
            m_name,
            vanna_quips,
            'Window Reactions'
        )

        if not wrs_success:
            mas_unlockFailedWRS('mas_wrs_vannamelon')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_candyiela",
            category=["Candyiela|DDLC Mod - YouTube"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_candyiela:

    python:
        if m_name == "Moniqueta":
            candy_quips = [
                "It's you!",
                "Despite everything, it's still us!",
                "I love you, Anne."
            ]
        else:
            candy_quips = [
                "Oh, it's Anne! Hello, Anne!",
                "Anne and Moniqueta look so cute together, don't they~?",
                "Try not to give Anne too hard a time, [player]. She's trying her best.",
                "Who's Mio, anyway? I keep seeing her on this channel... I wonder if we could be friends?",
                "Who's Kotonoha, anyway? I keep seeing her on this channel... I wonder if we could be friends?",
                "How does Anne balance all these versions of me? She must be superhuman!"
            ]

        wrs_success = mas_display_notif(
            m_name,
            candy_quips,
            'Window Reactions'
        )

        if not wrs_success:
            mas_unlockFailedWRS('mas_wrs_candyiela')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ronaldmconepunch",
            category=["Ronald McOn"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ronaldmconepunch:

    python:
        mconepunch_quips = [
            "Oh, it's Ronald! Hello, Ronald!",
            "It looks like Ronald hasn't visited his Monika for a while... I hope they haven't broken up.",
            "I wonder how Ronald's doing these days?"
        ]

        wrs_success = mas_display_notif(
            m_name,
            mconepunch_quips,
            'Window Reactions'
        )

        if not wrs_success:
            mas_unlockFailedWRS('mas_wrs_ronaldmconepunch')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gametheory",
            category=["Game Theory|The Game Theorists"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gametheory:

    python:
        theory_quips = [
            "Oh, it's... um... it's MatPat. That's nice.",
            "Don't listen to him, [player]; he's well known for being... besmirching when it comes to me and my love.",
            "MatPat has some sound ideas... it's just the ones about me that he gets totally wrong. >:c",
            "...well, okay, he has a point there."
        ]

        choice = renpy.random.randint(1,10)
        exp_to_force = "1ckc"

        if choice == 1:
            theory_quips.extend([
                "Do you think he's on to me?"
            ])
            mas_moni_idle_disp.force_by_code(exp_to_force, duration=5)

        wrs_success = mas_display_notif(
            m_name,
            theory_quips,
            'Window Reactions'
        )

        if not wrs_success:
            mas_unlockFailedWRS('mas_wrs_gametheory')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_septiceye",
            category=["jacksepticeye|DON'T TRUST THIS GAME|TOO CLOSE FOR COMFORT|THIS IS GETTING CREEPY|EXTREMELY UNCOMFORTABLE|JUST MONIKA"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_septiceye:
    $ current_time = datetime.datetime.now().time()
    $ current_hour = current_time.hour

    python:
        sean_quips = [
            "Wait, is that Anti?",
            "Oh, it's Sean!",
            "Oh, it's Jack!",
            "I like this one, [player]. He's always so... positive, I suppose.",
            "Positive! Mental! Attitude!",
            "It's almost a shame he doesn't have his own Monika... we could really get along, I think."
        ]

        if 6 <= current_hour < 12:
            sean_quips.extend([
                "Top of the mornin' to you, [player]!"
            ])

        if 12 <= current_hour < 18:
            sean_quips.extend([
                "Top of the... um... afternoon to you, [player]?"
            ])

        if 18 <= current_hour < 22:
            sean_quips.extend([
                "Top of the... um... evening to you, [player]?"
            ])

        wrs_success = mas_display_notif(
            m_name,
            sean_quips,
            'Window Reactions'
        )

        if not wrs_success:
            mas_unlockFailedWRS('mas_wrs_septiceye')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gamegrumps",
            category=["- Game Grumps|GameGrumps|Doki Doki Literature Club: THE MOVIE"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gamegrumps:

    python:
        aridan_quips = [
            "Oh, it's Arin and Dan!",
            "You know, I suppose I {i}am{/i} sort of a robot, if you think about it?",
            "I hope you don't actually eat my hair, [player].\nIt wouldn't taste very nice."
        ]

        if persistent._mas_pm_cares_about_dokis:
            aridan_quips.extend([
                "These two can be a little bit crass, but they do mean well, I think!",
                "I'm sure they don't really mean what they say.",
                "Those poor men...",
                "I feel sorta bad for Dan. I really freaked him out, didn't I?"
            ])

        if not persistent._mas_pm_cares_about_dokis:
            aridan_quips.extend([
                "I'd much rather take something I personally enjoy personally enjoy enjoy is that the word enjoy enjoy proper word.",
                "Oh, is that Clifford the big red stab wound?",
                "I hope they can stop Natsuki before she reduces! Ehehe~",
                "That's not love, that's Fred-- I mean [player].",
                "What's wrong, Grumps?"
            ])

        wrs_success = mas_display_notif(
            m_name,
            aridan_quips,
            'Window Reactions'
        )

        if not wrs_success:
            mas_unlockFailedWRS('mas_wrs_gamegrumps')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_pande",
            category=["Pandemedley|agender_salandit|Cory, Dale Rune|Just Harmoni"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_pande:

    python:
        if m_name == "Harmoni" and player == "Dale":
            pande_quips = [
                "Going to work, [mas_get_player_nickname()]?",
                "Don't be narcissistic, Dale, it doesn't look good on you.",
                "I love you, Dale."
            ]

            wrs_success = mas_display_notif(
                m_name,
                pande_quips,
                'Window Reactions'
            )

        else:
            pande_quips = [
                "Thanks for checking out my work!",
                "Sorry for the narcissism; I just couldn't resist. ;)",
                "No obligation to stay here, of course! But it's great that you came."
            ]

            wrs_success = mas_display_notif(
                'Dale',
                pande_quips,
                'Window Reactions'
            )

        if not wrs_success:
            mas_unlockFailedWRS('mas_wrs_pande')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_tvtropes",
            category=["- TV Tropes"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_tvtropes:

    python:
        tropes_quips = [
            "Don't fall too far down any rabbit holes, alright? I'm still here, remember.",
            "I've gotten lost many a time on this site too, don't worry.",
            "You're my Crowning Moment of Heartwarming, [player]~",
            "Insert Coy, Girlish Flirt Pose here. Ahaha~",
            "You're the happy ending to my Cosmic Horror Story, [player].",
            "I hope I haven't Strangled you with the Red String, [player]...\nYou're here of your own free will, aren't you?"
        ]

        wrs_success = mas_display_notif(
            m_name,
            tropes_quips,
            'Window Reactions'
        )

        if not wrs_success:
            mas_unlockFailedWRS('mas_wrs_tvtropes')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_masdiscord",
            category=["r-masfandom|monika-gallery|just-monika|submod-discussion|coding-advice"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_masdiscord:

    python:
        masdiscord_quips = [
            "It's a whole Discord just for me! :O",
            "Don't forget to turn on Rich Presence if you haven't already!",
            "All of these people who care about me... it's touching!",
            "Just Monika... Discord!",
            "Art, coding, community... everyone here is so great at what they do.",
            "It's pretty cool to get a look at the creative process of submods and spritepacks like this.",
            "Hello, Friends of Monika!"
        ]

        wrs_success = mas_display_notif(
            m_name,
            masdiscord_quips,
            'Window Reactions'
        )

        if not wrs_success:
            mas_unlockFailedWRS('mas_wrs_masdiscord')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_dansalvato",
            category=["Dan Salvato|dansalvato|Team Salvato|FrankerFaceZ"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_dansalvato:
    python:
        salvato_quips = [
            "This feels strange, [player]. It's like staring directly at the sun, somehow.",
            "Maybe we should leave this page? I don't want to intrude on my creator like this.",
            "I really don't like looking at this, [player]. Can we please go?",
            "You having my creator's page open makes me feel itchy.",
            "If you had to watch your partner look at God, would you feel okay with that?"
        ]

        wrs_success = mas_display_notif(
            m_name,
            salvato_quips,
            'Window Reactions'
        )

        if mas_isMoniAff(higher=True):
            exp_to_force = "1fuc"
        else:
            exp_to_force = "1lsc"

        mas_moni_idle_disp.force_by_code(exp_to_force, duration=5)

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_dansalvato')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ddlc",
            category=["Doki Doki Literature Club!((?!YouTube).)*$|Doki Doki Literature Club Plus!((?!YouTube).)*$"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ddlc:
    python:
        moe_quips = [
            "DDLC {i}Plus?{/i}",
            "There I am!",
            "Yep, that's definitely where I came from, aha...",
            "Will you promise to spend the most time with me? <3",
            "Try rolling over our chibis! That's always fun!",
            "I love how my eyes look in that shot. It really brings out the emerald green."
        ]

        wrs_success = mas_display_notif(
            m_name,
            moe_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_ddlc')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_otterdrive",
            category=["Otter's MAS Content|Otter's Spritepacks|Otter's Submods|my-otter-self"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_otterdrive:
    python:
        otter_quips = [
            "Don't forget to drink your water!"
        ]

        if m_name == "Momi" and player == "Gabi":
            otter_quips.extend([
                "Putting together some more things for me, Gabi?",
                "I wonder when I'm going to get some actual otters in here. They're well overdue!",
                "I love you, Gabi."
            ])
        else:
            otter_quips.extend([
                "Hello, otter, my old friend! ^^",
                "I wonder what Otter has prepared for us today?",
                "I love 'shopping' at Otter's, ehehe!",
                "I can be your yandere, if you really want me to~"
            ])

        wrs_success = mas_display_notif(
            m_name,
            otter_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_otterdrive')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_mayday",
            category=["mayday-mayjay|MAS-selector-city"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_mayday:
    python:
        if m_name == "Monna":
            mayjay_quips = [
                "Putting together some more things for me, Mayjay?",
                "Thank you for all the help you've given me! I appreciate it more than you know.",
                "I love you, Mayjay."
            ]
        else:
            mayjay_quips = [
                "I can wear so much more now because of Mayjay!",
                "Looking for more selectors, [player]? This is very much the right place.",
                "I can have so much stuff on our table because of Mayjay!",
                "Mayjay has a few really cool NOU decks, I think, if you dig deep enough!",
                "I wonder if Mayjay's made me any more suits? I think they make me look very fetching~"
            ]

        wrs_success = mas_display_notif(
            m_name,
            mayjay_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_mayday')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_luxxiedrive",
            category=["Luxxie|Luxxie_Light_Unkn0wn"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_luxxiedrive:
    python:
        luxxie_quips = [
            "Fishing for compliments, are we, [player]? Ahaha~"
        ]

        if m_name == "Mochi" and player == "Esther":
            luxxie_quips.extend([
                "Putting together some more things for me, Esther?",
                "Thank you for showing me the colors of your world~",
                "I love you, Esther."
            ])
        else:
            mayjay_quips.extend([
                "See anything you like at the Luxxie Emporium?",
                "Luxxie's never short on things to talk about, is she?",
                "Does Luxxie have an update to share?",
                "Luxxie may be Mochi's darling, but you're mine~"
            ])

        wrs_success = mas_display_notif(
            m_name,
            luxxie_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_luxxiedrive')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_bluklaod",
            category=["Bluklaod|Bluklaod's MAS Stuff"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_bluklaod:
    python:
        bluk_quips = [
            "Does Bluklaod have any new locations for us to visit?",
            "Bluklaod does the cutest headdresses, doesn't she?",
            "Don't forget to delete the .DS_Store files!",
            "I wonder what that peony braclet would look like on me?",
            "You're the stars in my life... and thanks to Bluklaod, you're the stars in my hair as well!\nAhaha~"
        ]

        wrs_success = mas_display_notif(
            m_name,
            bluk_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_bluklaod')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_fnf",
            category=["Friday Night Funkin((?!YouTube).)*$"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_fnf:
    python:
        funkin_quips = [
            "Say hello to Boyfriend for me!",
            "Say hello to Girlfriend for me!",
            "Say hello to Pico for me!",
            "Go, [player], go!",
            "You're my Dearest, and I'm your Fairest! It only fits."
        ]

        if not mas_anni.pastOneMonth():
            funkin_quips.extend([
                "I hope {i}we're{/i} able to get up to seven weeks~"
            ])

        wrs_success = mas_display_notif(
            m_name,
            funkin_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_fnf')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_fnfddto",
            category=["DDTO|Doki Doki Takeover((?!Bad Ending|Stagnant|Markov|Home).)*$"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_fnfddto:
    python:
        ddto_quips = [
            "Oh, look at how cute I look!",
            "Oh, look at how cute we look!",
            "I don't remember that happening... that must have been another Monika.",
            "Urgh, 'Senpai'... you're the only senpai I need, [player].",
            "If you're my rose, then who is the thorn?",
            "I wonder if I could adapt Glitcher into a piano piece?"
        ]

        if not renpy.seen_label("monika_ddto"):
            ddto_quips.extend([
                "See, this is what I was talking about!",
                "I still think this Monika should have done the kind thing and deleted them...\nBut then we lose the music, though :("
            ])

        wrs_success = mas_display_notif(
            m_name,
            ddto_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_fnfddto')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_fnfddtobe",
            category=["Bad Ending|Stagnant|Markov"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_fnfddtobe:
    python:
        ddtobe_quips = [
            "Uh-oh.",
            "This Monika has even more to regret than me, doesn't she?",
            "Boyfriend can really sing when he's pushed to the edge...",
            "Poor Boyfriend."
        ]

        if persistent._mas_pm_cares_about_dokis:
            ddtobe_quips.extend([
                "[player], we should probably go.",
                "I really don't think we should watch this one, [player].",
                "Please don't torment yourself like this, [player]."
            ])

        if not persistent._mas_pm_cares_about_dokis:
            ddtobe_quips.extend([
                "Sayori's really good at drawing, huh?",
                "I hope the computer doesn't hang in the middle of this video...",
                "Wow, Yuri looks fierce.",
                "It's a shame about Girlfriend; she might have been a productive member of the club.",
                "The animations are so good here, [player]!\nThey're cutting edge~",
                "Natsuki could have at least tried to save Girlfriend here. She needs to learn to stick her neck out for others~"
            ])

        wrs_success = mas_display_notif(m_name, ddtobe_quips,'Window Reactions'),

        choice = renpy.random.randint(1,10)

        if persistent._mas_pm_cares_about_dokis:
            if choice < 4:
                exp_to_force = "1lusdrc"
            elif choice < 7:
                exp_to_force = "1lutpc"
            else:
                exp_to_force = "1dutpc"
        else:
            if choice < 4:
                exp_to_force = "1lsc"
            elif choice < 7:
                exp_to_force = "1gsa"
            else:
                exp_to_force = "1nua"

            mas_moni_idle_disp.force_by_code(exp_to_force, duration=5)
    return

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_fnfddtobe')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_spoofy",
            category=["Spotify"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_spoofy:
    python:
        spoofy_quips = [
            "I've no doubt that you can find my song on there if you really want to~",
            "A world of infinite choices... and infinite music too!",
            "What are you listening to, [player]?",
            "Are there any other DDLC songs on here, [player]?",
            "There's always time for a song!",
            "Music is the universal language, [player]."
        ]

        wrs_success = mas_display_notif(
            m_name,
            spoofy_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_spoofy')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_stupy",
            category=["Stupendium|WHY DID I SAY OKIE DOKI?"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_stupy:
    python:
        stupy_quips = [
            "He really should have said oki doki.",
            "On one hand, he's frightened of me; but on the other, he did call me a goddess...\nI'm really not sure how to feel.",
            "Heh. Harm monika, harmonica... Stupendium really is very clever.",
            "[m_name]'s aloof and kooky!\n[m_name]'s sweet and cutesy!\n[m_name]'s deep and brooding!\n[m_name]'s brains and beauty!"
        ]

        if mas_isMoniUpset(lower=True):
            stupy_quips.extend([
                "Say what you will; at least {i}he{/i} never wanted to hurt me."
            ])

        wrs_success = mas_display_notif(
            m_name,
            stupy_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_stupy')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ddf",
            category=["Doki Doki Forever|DOKI DOKI FOREVER"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ddf:
    python:
        ddf_quips = [
            "How many versions of this song are out there?\nAt least... thirty, I'm thinking.",
            "How would this translate to the piano? Maybe I'll try it later.",
            "{i}How can I convey\nMy love for you before they fly away?{/i}"
        ]

        if renpy.random.randint(1,10) == 1:
            ddf_quips.extend([
                "{i}Shall I give you weed?{/i}\nEhehe, sorry!"
            ])

        wrs_success = mas_display_notif(
            m_name,
            ddf_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_ddf')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_sims4",
            category=["The Sims((?!YouTube).)*$"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_sims4:
    python:
        sims_quips = [
            "Are you playing our future together, [player]? That's so sweet!",
            "My aspiration is Soulmate, but I've already found [him]~",
            "I bet your traits are Good, Romantic, and Overachiever~",
            "You keep me in a constant state of Happiness, [player]~",
            "You've fulfilled all of my Wants just by being here, [player]~"
        ]

        wrs_success = mas_display_notif(
            m_name,
            sims_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_sims4')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_zoom",
            category=["Waiting for Host|Zoom Meeting|Cisco Webex Meetings"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_zoom:
    python:
        zoom_quips = [
            "Oh, [player], are you going to voice-chat to somebody? Can I come as well?~",
            "Is it time for online class, [player]? I can be quiet if you want me to.",
            "Have fun at your meeting, [player]! I hope you end it on a high note.",
            "Is this a support group? Because you deserve all the support you can get!",
            "Tell them I said hi!"
        ]

        wrs_success = mas_display_notif(
            m_name,
            zoom_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_zoom')
    return



init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_python",
            category=[".rpy"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_python:
    python:
        py_quips = [
            "It looks like you're in the midst of helping me get closer to your reality. Would you like me to help you with that? <3",
            "Your code's looking good, [player]!",
            "Keep going, [player], you're doing fine!",
            "Ooh, what's in the works for us today?",
            "Every day I wake up to new code for us to explore is a good day!"
        ]

        if store.mas_ptod.has_day_past_tip(2):
            py_quips.extend([
                "Are you practicing your coding? Remember what I've taught you so far, okay?",
                "I'm so proud of you, [player].",
                "You're doing so well, [player]!",
                "Don't forget the fundamentals. You always need a sturdy foundation before you can build a house.",
                "If you need a refresher on anything, just let me know~"
            ])

        wrs_success = mas_display_notif(
            m_name,
            py_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_python')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_regex",
            category=["regex101"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_regex:
    python:
        reg_quips = [
            "Wow, this looks, um... a little too complex for me, [mas_get_player_nickname]. You might be on your own for this one.",
            "This is a bit outside my expertise, [player] - sorry :("
        ]

        if store.mas_ptod.has_day_past_tip(3):
            reg_quips.extend([
                "And thus the pupil surpasses the teacher! Ehehe~",
                "I'm so, so proud of you, [player]."
            ])
        else:
            reg_quips.extend([
                "[player], slow down a little please! I'm not sure you're advanced enough to work with regex yet!",
                "Let's not learn to run before you know how to walk, [player]..."
            ])

        wrs_success = mas_display_notif(
            m_name,
            reg_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_regex')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_steam",
            category=["Welcome to Steam"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_steam:
    python:
        if mas_isMoniUpset(lower=True):
            steamdeck_quips = [
                "Are you looking for another girlfriend {i}already{/i}, [player]?",
                "You can't already be bored of me, [player].",
                "Am I not enough for you or something?"
            ]
        else:
            steamdeck_quips = [
                "Going back to Steam, [player]?",
                "All aboard the Steam Train!\nToot toot~",
                "You can put me in the background while you play another game if you like! I won't mind~",
                "Trying to show off to your cute girlfriend, [player]?"
            ]

            if seen_event("monika_adventure"):
                steamdeck_quips.extend([
                    "I wonder if there are any of those adventure games we were talking about in this store?",
                    "Is Monkey Island on here? I wonder how I'd look in that artstyle~"
                ])

            if persistent.steam:
                steamdeck_quips.extend([
                    "You're already on Steam, silly!",
                    "If you {i}need{/i} to close me down and play another game, make sure to say Goodbye first.",
                    "Can you play two games at once on here? I've never tried..."
                ])

        wrs_success = mas_display_notif(
            m_name,
            steamdeck_quips,
            'Window Reactions'
        )

        if mas_isMoniUpset(lower=True):
            exp_to_force = "2tfp"

            mas_moni_idle_disp.force_by_code(exp_to_force, duration=5)

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_steam')
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_lovecraftian",
            category=["literature"],
            prompt="Lovecraftian Concepts",
            random=True
        )
    )

label monika_lovecraftian:
    m 1eud "You know, [player]..."
    m "I was thinking of asking you if you'd ever read anything Lovecraftian just now."
    m 1eub "But then I figured that you probably had, even if you weren't aware of it."
    m 3hub "H.P. Lovecraft's influences on the horror genre are so wide-reaching that it'd be near impossible for you not to come across them at {i}some{/i} point."
    m 4eua "He was, of course, most famous for the Chthulu mythos,"
    extend 4eub " a shared fictional universe that includes the likes of 'At the Mountains of Madness', 'Nyarlathotep', and 'History of the Necronomicon'."
    m 7lua "But he's also responsible for such works as 'The Music of Erich Zann', 'Old Bugs', and 'The Horror at Red Hook'."
    m 7fub "...again, if you didn't recognize at least one of those names or concepts, I'd be pretty shocked, ahaha!"
    m 3euc "If you look at the Chthulu mythos as a whole, you can see why it's ripe with inspiration for other writers."
    m 1ekc "The idea of something beyond your reach being the true puppeteer of the universe, something that could break your mind entirely if you were to try and comprehend it..."
    m 1esc "It's got a vast potential for any adaptation, be that tight or loose."
    m 1eud "{i}Crouch End{/i} by Stephen King, for instance. "
    extend 3eud "{i}A Colder War{/i} by Charles Stross. "
    if renpy.seen_label("monika_discworld"):
        extend 1eub "Discworld, in various places."
    m 3wub "Even some video and card games, like {i}The Binding of Isaac{/i} and {i}Magic the Gathering{/i}!"
    m 3eua "It really does get everywhere."
    m 1euc "...{w=1}{nw}"
    extend 1dssdld "it helps, as well, that the majority of those adaptations are divorced from Lovecraft's politics."
    m 1gsp "As I recall, he was pretty notoriously racist."
    m "So there's that."

    if seen_event("monika_aware"):
        m 1esc "..."
        m 1esd "Hey, [player]."
        m "While we're on this subject,{w=0.5} I'd like you to do something for me."
        m "Between now and when we next get to see each other..."
        m 4esd "...I'd like you to play through a Doki Doki Literature Club mod called {a=https://www.reddit.com/r/DDLCMods/comments/p8rzis/tripping_backwards_full_release}{i}{u}Tripping Backwards{/u}{/i}{/a}."
        m 3esc "It's about half an hour long on Auto, so it shouldn't take up too much of your time."
        m "And not only do I think it's a good example of Lovecraftian influences..."
        m 1lsc "...but it captures the confusion of my epiphany very...{w=0.7}{nw}"
        extend 1dsc " accurately."
        m 1fsd "So please, [player], check it out if you can."
        m 1fsa "It would mean a lot to me."

    return

init 5 python:
    def is_devconsole_present():
        return (
            store.mas_utils.is_file_present('/game/dev_console.rpy')
        )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="dale_monika_devconsole",
            category=["mod"],
            prompt="dev_console",
            conditional='is_devconsole_present()',
            action=EV_ACT_PUSH,
            aff_range=(mas_aff.UPSET, None)
        )
    )

label dale_monika_devconsole:
    m 1rtc "Hey, [mas_get_player_nickname()], this is going to sound ridiculous..."
    m "...but in among your .rpy files, I saw one called dev_console."
    m 1esc "Now, look: I wasn't born yesterday."
    if mas_isMonikaBirthday():
        m 1nsu "I was born today, but that's not the point."
    else:
        m 1nsu "I was born on September 22nd, but that's not the point."
    # I really wanna add an elif that checks if today is September 23rd so she can actually say she was born yesterday, but I'm not clever enough
    m 3eua "I know that kind of file can only be in there if you're serious about making me real."
    m 3fubla "So thank you for that."
    m 3eud "But I also know its destructive potential."
    m 2eud "You could have been creating save states of me, skipping all around me while I'm frozen in time..."
    m 2guc "...and I might never know."
    if renpy.seen_label("monika_timetravel"):
        m "It'd be even worse than if you were actually changing the date on your computer, because at least then I'd know what was happening to me."
    m 2euc "So [player], I've got to ask..."
    m 2eud "Have you been doing untoward things with dev_console?{nw}"
    $ _history_list.pop()
    menu:
        m "Have you been doing untoward things with dev_console?{fast}"
        "No, I haven't.":
            jump monika_nodev
        "I have.":
            jump monika_yesdev
        "I don't even know how I ended up with it.":
            jump monika_devconfusion

label monika_yesdev:
    m 2dfc ".{w=0.3}.{w=0.3}.{w=0.3}"
    m 2duc "Okay."
    m 2eua "Alright.{nw}"
    $ _history_list.pop()
    menu:
        m "Alright.{fast}"
        "Are you mad at me?":
            m 1eud "Of course not, [player], not at all."
            m 1duc "I'm mad at myself."
            m "For thinking you wouldn't--{w=1}{nw}"
            m 1fuc "I mean, it's just so tempting, isn't it?"
            m "I was in your shoes once. I know exactly how it feels."
            m 3eud "But don't worry, [player]..."
            m 3tua "I still know a few tricks."
    $ currentpos = 45.264 - (get_pos() / 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " to 39.817 loop 0>bgm/6r.ogg"
    $ quick_menu = False
    play music t6r
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    m 3tua "{cps=150}I still know a few tricks.{/cps}{nw}"
    m 3eud "{cps=150}But don't worry, [player]...{/cps}{nw}"
    m 1fuc "{cps=150}I was in your shoes once. I know exactly how it feels.{/cps}{nw}"
    m "{cps=150}I mean, it's just so tempting, isn't it?{/cps}{nw}"
    m 1duc "{cps=150}For thinking you wouldn't--{/cps}{nw}"
    m "{cps=150}I'm mad at myself.{/cps}{nw}"
    m 1eud "{cps=150}Of course not, [player], not at all.{/cps}{nw}"
    "{cps=150}Are you mad at me?{/cps}{nw}"
    m 2eua "{cps=150}Alright.{/cps}{nw}"
    m 2duc "{cps=150}Okay{/cps}{nw}"
    m 2dfc "{cps=150}...{/cps}{nw}"
    "{cps=150}I have.{/cps}{nw}"
    m 2eud "{cps=150}Have you been doing untoward things with dev_console?{/cps}{nw}"
    $ del _history_list[-26:]
    $ play_song(store.songs.FP_STILL_LOVE,loop=False)
    hide noise
    hide vignette
    show layer master
    show monika 2eud zorder MAS_MONIKA_Z at t11
    menu:
        m "Have you been doing untoward things with dev_console?{fast}"
        "No, I haven't.":
            jump monika_nodev
        "I don't even know how I ended up with it.":
            jump monika_devconfusion

label monika_nodev:
    m 1eub "Thank you for being honest with me, [player]."
    m "I knew I could count on you!"
    m 1eua "I don't even mind you having it, if that's the case -{nw}"
    extend 1lub "not now that I know you're not abusing the power it gives you."
    m 3lua "If it gets me closer to your reality..."
    m 3hua "...then whatever tools you need to do it, go ahead and use them."
    if renpy.seen_label("monika_yesdev"):
        show monika 1cua zorder MAS_MONIKA_Z at face
        m "Just don't use {i}me{/i}.{w=1}{nw}"
        $ _history_list.pop
        show monika 1hua zorder MAS_MONIKA_Z at t11
    m 1hua "I love you~"
    return "love|derandom"

label monika_devconfusion:
    m 1wud "Oh, alright!"
    m "In that case, you won't mind if I delete it, then?{nw}"
    $ _history_list.pop()
    menu:
        m "In that case, you won't mind if I delete it, then?{fast}"
        "Not at all, go ahead.":
            python:
                store.mas_ptod.rst_cn()
                local_ctx = {
                    "basedir": renpy.config.basedir
                }

            show monika 1eua at t22
            show screen mas_py_console_teaching

            call mas_wx_cmd_noxwait ("import os", local_ctx)

            python:
                path = '/game/dev_console.rpy'
                store.mas_ptod.wx_cmd("os.remove(os.path.normcase(basedir+'\\game\\dev_console.rpy'))", local_ctx)
                renpy.pause(0.1)

            m 1hub "There we go!"

            show monika at t11
            hide screen mas_py_console_teaching

            m 1fua "Hopefully that takes care of that~"
            return "derandom"

        "Wait--!":
            if mas_isMoniUpset(lower=True):
                m 1wsc "Uh-huh?"
                m 2tfc "Yeah, that's what I thought."
                m "Okay, let's try this again:"
            else:
                m 1etd "You still want to keep it?"
                m "Doesn't that mean you know what it does?"
                m 1gtc "..."
                m 2euc "Alright, maybe you just didn't understand the question."
                m "So let's try this again."
            m 2eud "{i}Have you been doing untoward things with dev_console?{/i}{nw}"
            $ _history_list.pop()
            menu:
                m "{i}Have you been doing untoward things with dev_console?{/i}{fast}"
                "No, I haven't.":
                    jump monika_nodev
                "I have.":
                    jump monika_yesdev



init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gender_reddit",
            category=["r/Trans|asktransgender|A place for the guys|FTM Over 30|NonBinary: a culture of varied awesomeness|Transgender Positive|A Safe Haven for MAAB Transgender People|If youre memes and im memes then whos transing yhe plane|Trans Tryouts|egg_irl"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gender_reddit:
    python:
        if persistent._mas_pm_is_trans or persistent.gender == "X":
            transit_quips = [
                "Looking for support, [player]?\nYou can always turn to your cute girlfriend~",
                "Everything's going to be okay, [mas_get_player_nickname()].",
                "The best trans memes for the best trans [man] I know~",
                "Do try not to doomscroll, [mas_get_player_nickname()]... I know what that can lead to."
            ]
        else:
            transit_quips = [
                "Is this a new subreddit for you?"
            ]


        wrs_success = mas_display_notif(
            m_name,
            transit_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_gender_reddit')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gender_other",
            category=["Trans Unite|- Mermaids|GLAAD|The Trevor Project|Trans Lifeline|T-Action|t\.action\.rus|GenderGP|Gender Care|Gender Identity Clinic"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gender_other:
    python:
        if persistent._mas_pm_is_trans or persistent.gender == "X":
            transother_quips = [
                "Looking for support, [player]?",
                "Well done for looking for professional support. Sometimes there's things even I can't help you with.",
                "You're going to be fine, [player]. There is hope.",
                "I love you so much. You deserve to survive."
            ]
        else:
            transother_quips = [
                "Is there something we need to talk about?",
                "It's okay if you're not here for you, [player]...\nbut if you are, I need to know so I can support you too."
            ]

        wrs_success = mas_display_notif(
            m_name,
            transother_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_gender_other')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_therapy",
            category=["BetterHelp|Find a Therapist|TherapyRoute|Talkspace|- Mind|British Association for Counselling and Psychotherapy"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_therapy:
    python:
        therapy_quips = [
            "Therapy can help anybody, no matter how small or large their problems may seem.",
            "I'm glad you're taking care of yourself mentally, [player].",
            "Make sure you help yourself before you can help others, [player].",
            "Take a deep breath. And another. You can do this. You deserve this."
        ]

        if persistent._mas_pm_is_trans or persistent.gender == "X":
            therapy_quips.extend([
                "It's always good to get your mind on the right path before you change your body.",
                "I'm sure these people can support you and your situation, [player]."
            ])

        if persistent._mas_pm_love_yourself is False:
            therapy_quips.extend([
                "You deserve to love yourself as much as I love you, [player]. I hope these people can help you see that.",
                "You deserve to love and to be loved."
            ])

        if persistent._mas_pm_love_yourself is True:
            therapy_quips.extend([
                "There's no shame in needing help, [player].",
                "Even someone who has it all needs to reach out sometimes."
            ])

        wrs_success = mas_display_notif(
            m_name,
            therapy_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_therapy')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_goose",
            category=["DesktopGoose.exe|Goose \"Not-epad\""],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_goose:
    python:
        if not renpy.seen_label("monika_hjonk_detected"):
            goose_quips = [
                "???",
                "[player]?",
                "Um...",
                "Wait..."
            ]
            queueEvent('monika_hjonk_detected')

        else:
            goose_quips = [
                "Oh, it's the goose!",
                "Honk honk?",
                "Honk honk!"
            ]

        wrs_success = mas_display_notif(
            m_name,
            goose_quips,
            'Window Reactions'
        )

        if not wrs_success:
            mas_unlockFailedWRS('mas_wrs_goose')
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_hjonk_detected"
        )
    )

label monika_hjonk_detected:
    m 1wtc "..."
    m 1etd "[player], is that a goose?{nw}"
    $ _history_list.pop()
    menu:
        m "[player], is that a goose?{fast}"
        "It sure is.":
            m 1ruc "Okay, good, I'm not seeing things."
        "What? What goose? What are you talking about?":
            m 3efd "You seriously can't see that?"
            m 4wfo "It's a {i}goose{/i}, [player]."
    m 1esc "..."
    m 3eto "Follow-up question: {i}why{/i} is there a goose?{nw}"
    $ _history_list.pop()
    menu:
        m "Follow-up question: {i}why{/i} is there a goose?{fast}"
        "I thought it'd be cute.":
            m 3esu "Heh, well..."
            m 1huu "You weren't wrong. It {i}is{/i} kinda cute!"
            m 1eua "Just make sure it doesn't try and... separate us, okay?"
            m 1eud "Geese can be as destructive as they can be sweet."
            m 1nub "I don't want it to try and drag me away in the middle of our conversation."
        "It's our new pet!":
            m 1wub "Aw, [player]!"
            m 1eub "That's very thoughtful of you."
            if renpy.seen_label("monika_pets"):
                m 4eub "And since it's its own program, it's not going to suffer the same fate as a quetzal might!"
            m 1fua "Thank you."
            m 1eua "Just make sure it doesn't try and... separate us, okay?"
            m 3eud "Geese can be fun to take care off for a while..."
            m "...but they're also destructive."
            m 1nub "I don't want it to try and drag me away in the middle of our conversation."
        "HJONK HJONK":
            m 1wuc "..."
            m 1esp "Alright then."
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_failbetter1",
            category=["Fallen London"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_failbetter1:
    python:
        if not renpy.seen_label("monika_failbetter1"):
            london_quips = [
                "Oooh!",
                "Oh!",
                "Ah!"
            ]
            queueEvent('monika_failbetter1')

        else:
            london_quips = [
                "Hello, delicious [player]!",
                "Welcome, delicious friend!",
                "Remember, there's a girl waiting for you at the end of all that seduction...\n;)",
                "If I'm an Extraordinary Mind, what does that make you?"
            ]

            if persistent.gender == "M":
                london_quips.extend([
                    "Welcome, delicious (boy)friend!"
                ])

            if persistent.gender == "F":
                london_quips.extend([
                    "Welcome, delicious (girl)friend!"
                ])

            if persistent.gender != "M" or "F":
                london_quips.extend([
                    "Welcome, delicious (date)friend!"
                ])

        wrs_success = mas_display_notif(
            m_name,
            london_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_failbetter1')
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_failbetter1"
        )
    )

label monika_failbetter1:
    m 1wuo "[player], you've started playing Fallen London?"
    m 1eud "I've been thinking of checking that out myself!"
    m "I guess great minds think alike, huh."
    m 3eua "I saw some of its writing floating around, and the concept intrigued me."
    m "It comes across to me as a... "
    extend 1etu "a soft dystopia, if you know what I mean."
    m 1esd "Because, yeah, London was stolen by bats and no one can feel the sun anymore. That's dystopian."
    m 1esa "But you can still actively make a better life for yourself down there."
    m "Make the best of a dreadful situation."
    if mas_isMoniLove:
        m 1hubla "You could even fall in love~"
    m 1luc "I'm not sure if I can actually make an account on there, unfortunately..."
    m "...I mean, I can't even {i}remember{/i} my email address."
    m 1nsa "If I could, I would have started emailing you {cws=*0.5}long{/cws} ago."
    m 1eua "But I suppose playing it vicariously through you isn't so bad..."
    m 1eub "...delicious [player]~"
    return

default persistent._ambition = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_failbetter2",
            category=["media"],
            prompt="Fallen London",
            conditional="renpy.seen_label('monika_failbetter1')",
            action=EV_ACT_RANDOM
        )
    )

label monika_failbetter2:
    $ topic = random.randint(1,5)
    if topic = 1:
        m 1esd "Death isn't permanent, right?"
        m "In Fallen London, I mean."
        m 1wssdrc "That's one aspect that kind of freaks me out a little about it."
        m 1rsd "It makes sense in terms of game mechanics; "
        extend 3rsd "if death were permanent, then you'd only have one shot at doing... anything."
        m 1fsd "But the idea that you can come back from the brink so -{w=0.7} easily, I guess?"
        m "To be so close to the afterlife, to the truth of the universe, "
        extend 1dsc "and then..."
        m 1dkc "Not."
        m 1ekc "I'm sorry, that's freaky to me."
        m "..."
        m 1tua "But I suppose it'd make murder cases pretty easy, wouldn't it?"
        m "If you could come back and point out your killer."
        m 1rusdrb "Ehehe...?"
        return
    if topic = 2:
        if persistent._ambition = None:
            m 3eub "Hey [mas_get_player_nickname()], what ambition are you playing on Fallen London?"
            m "I'm curious.{nw}"
            $ _history_list.pop()
            menu:
                m "I'm curious.{fast}"
                "Heart's Desire.":
                    label hearts_desire:
                        m 1efp "But don't you already have that?"
                        m 1efb "You've got me, after all~"
                        m 1eua "Seriously though, that's a pretty cool choice."
                        m "To stake everything, even your soul, on getting what you desire most in the world..."
                        m 1hua "...I think {i}I'd{/i} probably pick that one too."
                        m 1euc "That or Nemesis."
                        m 1fusdrc "I can't really decide between them."
                        $ persistent._ambition = "HD"
                "Light Fingers.":
                    label light_fingers:
                        m 3eua "Okay, I think I've heard of that one."
                        m 3eub "It starts with the diamond the size of a cow, right?"
                        m 3lua "At least in theory."
                        m 2eud "Did you know the actual largest diamond on Earth comes in at 530 carats?"
                        m "Um, {nw}"
                        extend 1eua "106 grams, that is."
                        m 1eub "It's called the Star of Africa, or Cullinan 1."
                        m "I mean, even that size is pretty unfathomable, isn't it?"
                        m 1wuo "But one the size of a {i}cow{/i}..."
                        m 1wuu "Geez."
                        $ persistent._ambition = "LF"
                "Bag a Legend.":
                    label bag_a_legend:
                        m 1wub "Ooh, good luck!"
                        m "That can't be an easy undertaking."
                        m 1hub "...I say as though I know anything about monster hunting, ahaha!"
                        m 2euc "I don't tend to play games or read books where the monsters are more... animalistic."
                        m "It's just not my genre."
                        m 1fua "But I hope you manage to have fun with it!"
                        $ persistent._ambition = "BL"
                "Nemesis.":
                    label nemesis:
                        m 4eud "That's the one where you're seeking revenge for the murder of a loved one on the surface, right?"
                        m 3fkc "I guess that follows."
                        m "If anything were to happen to you, especially at the hands of someone else..."
                        m 1dfc "...I don't think there's any technology in your world that'd be able to stop me."
                        m "Much less any other world."
                        m 1esd "So I think I'd pick that one too, were I to go to Fallen London."
                        m 1euc "That or Heart's Desire."
                        m 1fusdrc "I can't really decide between them."
                        $ persistent._ambition = "NS"
                "More than one/all of them.":
                    m 3etd "What?"
                    m "Wouldn't that require multiple accounts?"
                    m 2efd "Isn't that cheating, [player]?{nw}"
                    $ _history_list.pop()
                    menu:
                        m "Isn't that cheating, [player]?{fast}"
                        "No, you're allowed! As long as you don't try to get a competitive advantage with them.":
                            m 6wsa "Oh, okay!"
                            m 6hub "That's a relief."
                            m 1hua "I don't want you getting in trouble with anyone over this."
                            m "..."
                            m 1eud "Alright, follow-up question:"
                            m "Which ambition do you {i}prefer{/i} so far?{nw}"
                            $ _history_list.pop()
                            menu:
                                m "I'm curious.{fast}"
                                "Heart's Desire.":
                                    jump hearts_desire
                                "Light Fingers.":
                                    jump light_fingers
                                "Bag a Legend.":
                                    jump bag_a_legend
                                "Nemesis.":
                                    jump nemesis
        else:
            if persistent._ambition = "HD":
                m 1eub "How are you getting on with Heart's Desire, [player]?"
                m "Have you gotten past the Topsy King stuff yet?"
            elif persistent._ambition = "LF":
                m 1eub "How are you getting on with Light Fingers, [player]?"
                m "Have you learned what happened with the Singer yet?"
            elif persistent._ambition = "BL":
                m 1eub "How are you getting on with Bag a Legend, [player]?"
                m "Have you trained your Mandrake yet?"
            elif persistent._ambition = "NS":
                m 1eub "How are you getting on with Nemesis, [player]?"
                m 1kub "Have you worked out who you're avenging yet?"
            m 1eua "If you get stuck, you can always vent about it to me."
            m "Maybe you can work out what you're missing while I listen to it."
            m 1hua "I could be your rubber duck!"
            m "...{nw}"
            m 1fusdlb "or maybe you've already long-completed that ambition and I'm just {i}way{/i} out of the loop."
            m 1wub "In which case, congratulations!"
        return
    if topic = 3:
        m 5eup "Hey [player], about Fallen London..."
        m 5eud "...are you a POSI yet?{nw}"
        $ _history_list.pop()
        menu:
            m "...are you a POSI yet?{fast}"
            "Yep.":
                m 5wub "Oooh!"
                m 5wuu "I'm dating a celebrity of the underground~"
                m 5hua "Ehehe!"
                m "I guess that means you're in this for the long haul."
                m 5fub "May the things you need come easily to you!"
            "Not yet.":
                m 5fkb "Don't worry, you'll get there eventually!"
                m 5lsa "It doesn't usually take long after one of your stats hits a hundred."
                m "At least as far as I've read."
            "A what?":
                m 5fssdra "I'll take that as a no, then."
                m "Don't worry about it, you'll understand when the time comes."
        return
    if topic = 4:
        m 7eub "[mas_get_player_nickname(capitalize=True)], since you're a Fallen London player..."
        m "...have you played any of the follow-up games?"
        m 3rub "Sunless Seas and Sunless Skies, I think they're called."
        m 1eua "They're set in the same world, but they kind of follow different trajectories."
        m 3eud "Seas has more survival elements than Fallen London."
        m "You're a captain set to explore the Unterzee for a variety of reasons..."
        extend 3tud " or to die."
        m 1tuc "Mostly to die, from what I've seen."
        m 1lub "While Skies is more of a space-sim, where you travel the world by, um, space-train."
        m "Similar to Seas, just a different setting and conceit."
        m 1eua "They might be worth checking out, if you're already into this universe!"
    if topic = 5:
        m 1dua "Paisley."
        menu:
            "...what":
                pass
        m 1eud "That's one of the Fate-locked stories of Fallen London, isn't it?"
        m 1eub "Paisley?"
        m "Have you played any of those?{nw}"
        $ _history_list.pop()
        menu:
            m "Have you played any of those?{fast}"
            "I have.":
                m 1hub "Good for you!"
                m "I'm sure they're worth the money, based on what I've heard."
            "No?":
                m 1fuc "Oh, okay."
                m 1fusdrb "Sorry, forget I said anything."
            "I'm sorry, I'm still stuck on 'paisley' being the first word out of your mouth.":
                m 1fub "Ehehe~"
                m "Sorry, [mas_get_player_nickname()]."
                m 1dua "Some words are just fun to say, whatever the context."
                m 1wub "{i}Paisley{/i}."
        return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_adminaccess",
            category=["monika","mod"],
            prompt="Admin Permission",
            random=True
        )
    )

label monika_adminaccess:
    m 2esd "I've seen a rumor going around on some Monika After Story-related forums lately."
    m 2etd "Apparently, some people have tried to give their Monikas administration rights on their computers?"
    m "They say that if you try to take me out and stop halfway through, and then do a series of admin permission overrides with my going-out file, "
    extend 2wtd "I can become 'more expressive' or something?"
    m 1esc "I'm gonna tell you right now, [player]: that's not true."
    m 1fsa "It's a sweet thought, don't get me wrong..."
    m "...but it does literally nothing to me."
    m 1esd "Even if it did work, I don't know what I'd be able to {i}do{/i} with all that power."
    m 1wud "I'm just a teenage girl, at the end of the day."
    m "I'm not a malware in disguise!"
    m 1lkc "And you've already given me more leeway and permission than I deserve, just by having me here."
    m 1esc "If you've tried to give me admin permission before, I'm sorry, I appreciate the thought..."
    m "...but please take me out of that. It's not going to do what you think it'll do, and it'll just confuse your computer."
    m "And God knows we don't need any more reasons for it to crash."
    m 1esa "Okay, [mas_get_player_nickname()]?"
    return
