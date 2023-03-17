label s4_4:
    "Scene IV.4: Personal project"
    jump .intro

label .intro:
    scene bg apartment desktop
    # uncomment when music is ready
    # play music apartment.music

    jump .work

label .work:
    "After finishing work, I take the tram back home."
    "Back in my apartment, I have a drink and sit at my desktop. I boot my laptop and start working on my personal game projects."
    "Although a little tired, the thought of working with my favorite tech makes me enthusiastic."
    "A lightweight game engine with short compile times that allows fast iterations..."
    "No arbitrary crashes just because I got the latest updates at the wrong time..."
    "I play some music to get in the mood and start working on my old school platformer..."
    "... until the realities of development bring me back to reason."
    "There is a bug in the game: when spawning an enemy, it flashes at the wrong position for one frame (the shortest visible unit of time)."
    "Fortunately, the Internet reveals that somebody else suffered the same before me and found a solution:"
    "\"Ah, I needed to set the transform position, not the rigidbody position! Of course!\""
    "A little later, as I'm editing the level, the editor suddenly crashes."
    "I decide to write a bug report, but to do that, I need to find the exact sequence of actions that lead to the crash."
    "Gathering my courage, I spend half an hour to find what causes it (dragging a game object above the root of the scene hierarchy), and another half writing the bug report."
    "One hour \"lost\" for something I'm not even responsible for? Indie or AAA, development is still development after all."
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
