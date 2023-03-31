# Scene IV.4: Personal project
label s4_4:
    jump .intro

label .intro:
    scene bg tram with Dissolve(1.0)
    $ audio_stopFade(2.0)

    "I exit the company building and take the tram back home."
    jump .work

label .work:
    scene bg empty_canvas with Dissolve(1.0)

    "Back in my apartment, I hang my coat and have a drink."

    scene bg apartment desktop with dissolve

    "I'm a little tired, but I soon find myself sitting at my desktop and booting my laptop."

    pause 0.5

    "I starting checking my personal emails, but there are too many coming every day. As ironic as it sounds, I manage to read all of them at the office, but I can't keep up with my personal inbox."
    "And now, it's time to work on my personal game projects!"

    "It wouldn't be exaggerated to say that a second day starts for me around 19:45."
    "But! I got to work solo with my favorite tech, which means:
    {p}- a lightweight game engine with short compile times!
    {p}- no arbitrary bugs caused by other developers pushing bad stuff!"

    play sound audio.sfx.keyboard_typing_weak
    "I play some chiptunes to get in the mood and start working on my old school platformer..."
    "... until the realities of development bring me back to reason."
    "I find an annoying bug: when I spawn an enemy, it flashes at the wrong position before moving to the correct one."

    play sound audio.sfx.keyboard_typing_weak
    "Hail the Internet! I find a few other users who suffered the same symptoms, and apply their solution (or rather their \"workaround\")."
    "A little later, as I'm editing the level, the editor suddenly crashes."

    play sound audio.sfx.keyboard_typing_weak
    "I decide to write a bug report, but to do that, I need to find the exact sequence of actions that leads to the crash."
    "Gathering my courage, I spend half an hour to find what causes it, and another half writing the bug report."
    "One hour lost for something I'm not even responsible for? Indie or AAA, development is still development after all."
    # TODO: NO NDA but don't want to post on SNS
    jump .eating

label .eating:
    scene bg empty_canvas with dissolve

    "At half past eight, I realize I should have dinner. Drat! No leftovers in the fridge. I need to cook something."
    "Too tired for a proper recipe, I decide to go with my legendary seasoned steamed vegetables."
    "I let the cooking machine do its job so I can gain a few more minutes of work."
    "When the meal is ready, I grab it and start an anime."
    "The characters talk about how people's sense of justice fades out over time and how they become grayer and grayer when they become adult."
    "I don't feel like I'm selling my soul to my company, but maybe I could do more than what I'm told to?"
    "Hmm... I'm already sending feedback on stuff like accessibility. To go further, I'd need more authority, which I don't have."
    jump .choice

label .choice:
    "It's 9pm after dinner. Should I work a little more and risk oversleeping tomorrow, or just stop and relax?"
    menu:
        "Work more":
            jump .more_work
        "Relax":
            jump .relax

label .more_work:
    scene bg apartment desktop with dissolve

    "Okay, just one last fix."
    play sound audio.sfx.keyboard_typing_weak
    ".{w=0.5}.{w=0.5}."
    "After fixing three bugs and adding one feature, I realize we're close to midnight."
    "Was all this extra work necessary though? My game doesn't seem promising enough to sell and will probably end up like another training project or experiment."
    "It would be cool to hire some people, but that's a vicious circle: I need a good demo to attract other developers, and I need an artist and a level designer to make a cool demo."
    "It sure is nice working in a studio..."
    "Finally done with my work, I shut down my laptop and go to sleep."

    scene bg empty_canvas with dissolve

    jump .sleep

label .relax:
    "I grab some comics and starting reading. This time I picked a comedy, so I won't go through another phase of self-doubt."
    "After a few chapters, I close the book and go to sleep."

    pause 0.5
    jump .sleep

label .sleep:
    "Well, I did good a job today, on both of my projects. I deserve a good night's rest."

    pause 0.5

    scene overlay black with Dissolve(1.0)

    pause 0.5

    ".{w=0.5}.{w=0.5}."

    pause 2.0

    mc "Oh no!{w=1.0} I forgot to remove the debug line!"

    pause 2.5

    jump .end

label .end:
    jump credits
