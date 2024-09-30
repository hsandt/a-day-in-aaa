# Scene II.2: Play Break
label s2_2:
    jump .intro

label .intro:
    scene bg office open_plan with Dissolve(1.0)
    $ audio_crossFade(2.0, "music/office_open_plan.ogg")

    jump .watch_play

label .watch_play:
    "When I enter the room, I see some of my colleagues playing together some free-to-play title, and others focused on solo indie games."
    "I haven't played online for a while and I don't even know the more recent titles, so I don't think I'll be able to withstand the competition."
    "I guess I'll just pick a solo game, as usual."
    jump .play_game

label .play_game:
    scene bg office desktop with dissolve
    $ audio_crossFade(2.0, "music/office_desktop.ogg")
    # INSERT GAME CHOICE HERE - for now, auto-choose Starcraft II
    "Let's go with Starcraft II this time. {p}Yeah, it's an online game, but I'm just playing offline for now."
    play sound audio.sfx.keyboard_typing_weak
    "After all, my only previous experience with Starcraft was Brood War in the 2000s, so my RTS-fu is a little rusty."
    "But! I beat the AI at Medium level last time... so I try Hard this time!"
    "I get crushed. {p}I suppose I won't be going online today."

    pause 0.5

    jump .colleagues_arrive

label .colleagues_arrive:
    "As the end of lunch break draws nearer, I see more and more coworkers coming back to the room."

    ui_programmer "So, how was the gym?"
    level_artist "It was fine, but the leg machine was broken. {i}Again{/i}."
    ui_programmer "Like our code."
    level_artist "And you? How was improv?"
    ui_programmer "Great! The new guy had some hilarious lines!"
    ui_programmer ".{w=0.2}.{w=0.2}.{w=0.5} like our code."

    "I realize how other developers have regularly been practicing healthy or artistic activities. Maybe I should join a club too?"
    ".{w=0.4}.{w=0.4}.{w=0.8} or, I could keep sitting here and playing every noon, as usual."
    "Thinking of it, it's great that we are all adults and we can just do what we want on our spare time."
    "But sometimes I'd need some life coach to get me to do more varied things. A bit like school with sports classes and all."

    pause 0.5

    "OK, I got a few minutes left. Ready for another match?"

    pause 1.0

    jump .break_end

label .break_end:
    "Before I notice, break time is over, but I haven't finished my game yet. Hard mode sure is tough."
    # INSERT GAME CHOICE HERE on whether to keep playing - for now, auto-choose to continue playing
    "Believing in my incoming victory this time, I push the game a little further. But it's now 14:15 and I'm still far from it."
    # INSERT GAME CHOICE HERE on whether to keep playing - for now, auto-choose to continue playing
    "Should I just give up? No, too early for that."
    # TODO: create a variant of office open plan/desktop with louder voices, and play it during the break,
    # but cross fade to the quieter variant now
    "The mood is slowly becoming more serious in the room. People are getting back to work, speaking less and typing more."
    "I quickly glance at the room to check that nobody cares about me and my Terran base."
    "They don't seem to. Yet, as time goes on, I feel an invisible pressure growing on my back."
    "As the Zergs eventually defeat me, I paradoxically feel relieved, as I can finally close the game and avoid further suspicion."

    pause 0.5

    play sound audio.sfx.keyboard_typing_weak
    "I reopen Visual Studio, which needs some time to launch. This gives me an opportunity to bother my RTS-enthusiast coworker for some advice."

    mc "I couldn't beat AI in Hard."

    "My coworker sighs, looking terribly disappointed."

    junior_gd "Okay, what's your build order?"
    mc "My build... ?{w=0.8} Oh, right.{w=0.8} Er...{w=0.8} Barracks...{w=0.8} Supply Depot...{w=0.8} Refinery... ?"
    "Visual Studio finishes opening right at that moment, giving me an excuse to escape the surprise test before this whole thing turns into a scene straight out of SC2VN."

    pause 0.5

    # TODO: other devs wearing playing hardcore game?

    jump s4_1
