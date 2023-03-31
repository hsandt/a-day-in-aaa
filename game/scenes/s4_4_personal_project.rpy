label s4_4:
    "Scene IV.4: Personal project"
    jump .intro

label .intro:
    scene bg tram
    # uncomment when music is ready
    # play music apartment.music
    $ audio_stopFade(2.0)

    "I leave the company and take the tram back home."
    jump .work

label .work:
    scene bg apartment desktop
    "Back in my apartment, I have a drink and sit at my desktop. I boot my laptop and start working on my personal game projects."
    play sound audio.sfx.keyboard_typing_weak
    "Although a little tired, the thought of working with my favorite tech makes me enthusiastic."
    "A lightweight game engine with short compile times that allows fast iterations..."
    "No arbitrary crashes just because I got the latest updates at the wrong time..."
    "I play some music to get in the mood and start working on my old school platformer..."
    "... until the realities of development bring me back to reason."
    "There is a bug in the game: when spawning an enemy, it flashes at the wrong position for one frame (the shortest visible unit of time)."
    "Fortunately, the Internet reveals that somebody else suffered the same before me and found a solution:"
    "\"Ah, I needed to set the transform position, not the rigidbody position! Of course!\""
    "A little later, as I'm editing the level, the editor suddenly crashes."
    play sound audio.sfx.keyboard_typing_weak
    "I decide to write a bug report, but to do that, I need to find the exact sequence of actions that lead to the crash."
    "Gathering my courage, I spend half an hour to find what causes it (dragging a game object above the root of the scene hierarchy), and another half writing the bug report."
    "One hour \"lost\" for something I'm not even responsible for? Indie or AAA, development is still development after all."
    # TODO: NO NDA but don't want to post on SNS
    jump .eating

label .eating:
    "At 8pm, I realize I should have dinner. Drat! No leftovers in the fridge. I need to cook something to eat."
    "Too tired for a proper recipe, I decide to go with my legendary seasoned steamed vegetables."
    "I let the cooking machine do its job so I can gain a few more minutes of work."
    "When the meal is ready, I grab it and start an anime. Old high school habit."
    "The characters talk about how people's sense of justice fades out over time and how they become grayer and grayer when they become adult."
    "I don't feel like I'm selling my soul to my company, but maybe I could do more than what I'm told to?"
    "But I'm already sending feedback on stuff like accessibility. To go further I'd need more authority, which I don't have."
    jump .choice

label .choice:
    "It's 9pm after dinner. Should I work a little more and risk oversleeping tomorrow, or just stop and relax?"
    menu:
        "Work more":
            jump .more_work
        "Relax":
            jump .relax

label .more_work:
    "Okay, I just got one last bug to this for tonight."
    play sound audio.sfx.keyboard_typing_weak
    "..."
    "After fixing three bugs and adding one feature, I realize we're close to midnight."
    "Was all this extra work necessary though? My game doesn't seem promising enough to sell and will probably end up like another training project or experiment."
    "It would be cool to hire some people, but there is a vicious circle there: I need a good demo to attract other developers, and I need an artist and a level designer to make a cool demo."
    "It sure is nice working in a studio..."
    "Finally done with my work, I shut down my laptop and go to sleep."
    jump .sleep

label .relax:
    "I grab some comics and read for a while. The characters talk about... something that doesn't remind me of work. It's just fun."
    "After a few chapters, I close the book and go to sleep."
    jump .sleep

label .sleep:
    "After closing my eyes, I keep thinking about my game. Oh, but there's that thing I need to fix for the company's game too."
    "We'll see tomorrow."
    jump .end

label .end:
    "END"
