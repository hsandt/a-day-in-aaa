label s4_4:
    "Scene IV.4: Personal project"
    jump .intro

label .intro:
    # uncomment when bg is ready
    # scene bg apartment desktop
    # uncomment when music is ready
    # play music apartment.music

    jump .work

label .work:
    "(After an ellipsis for traveling back to the apartment, MC goes to his desk and work on his personal project)"
    "(A little tired (depends on office decisions), would like to avoid more screen, but more satisfying than day job)"
    "(Play some music and get in the mood)"
    "(MC is working a retro-style game, the opposite of what he does during the day)"
    jump .eating

label .eating:
    "(MC must eat around 8pm)"
    "(MC watches some series while eating. It feels odd that he's keeping his high school habits, but after hours of work it doesn't feel bad. Plus he doesn't have much time watching them at other times of the day.)"
    "(MC ponders over the story and characters and would like them to affect his life more so he can improve)"
    jump .choice

label .choice:
    "(After dinner, MC must decide whether to keep working and risking sleeping late, or just playing)"
    menu:
        "Work more":
            jump .more_work
        "Play":
            jump .play

label .more_work:
    "(MC gets into his project too much but must fix a last bug. He works between 20:00-0:00 or 21:00-1:00, and ends sleeping late. Decisions at the office affect final time)"
    "(MC wonders if this extra work is really worth it, as the game doesn't seem promising enough to sell and will probably end up like another training project)"
    "(It would be cool to hire some people, but there is a vicious circle between having a good demo to attract people and having an artist, etc. to make a cool demo)"
    jump .sleep

label .play:
    "(MC plays, he feels like he's not doing anything but can relax at the same time. He plays 1h.)"
    "(If the scene started at 20:00, it is now 21:00 and the MC thinks he can still work, he has no reason to sleep now.)"
    "(So he works on his personal project but gets into it, which leads back to 1.!)"
    jump .sleep

label .sleep:
    "(MC finally goes to sleep)"
    jump .end

label .end:
    "END"
