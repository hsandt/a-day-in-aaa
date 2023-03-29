# "Scene I.6: Architecture design"
label s1_6:
    jump .intro

label .intro:
    scene bg office open_plan
    play music office_open_plan

    # punchy intro
    "NDA... Non-Disclosure Agreement."
    "A contract clause whose role is to ensure we don't leak confidential information into the public space."
    "Information like the game we're working on, the technology we use or what happens inside the company."
    "I think these obscure glass windows represent it perfectly. Even the window cleaners that sometimes rappels down the building wouldn't see a thing inside the 6th floor of Black Rooster Games."

    pause 0.8

    "Even if they could, they would probably be disappointed.
    {p}Just a bunch of people sitting at their desks or talking to each other, trying to solve various issues — as in any other office."
    "The promotional posters and figurines look cool, though."

    pause 0.8

    # where I am, who I am, when I am, what I'm supposed to do
    "Anyway, let's get back to work."

    pause 0.3
    scene bg office desktop with dissolve
    $ audio_crossFade(2.0, "music/office_desktop.ogg")
    pause 0.3

    "I launch the game editor of our open-world action-adventure game, which displays a beautiful splash screen. While it's loading, I get myself a drink."

    pause 0.3
    $ audio_crossFade(1.0, "music/office_open_plan.ogg")
    scene bg office eating_area with wiperight
    pause 1.5
    $ audio_crossFade(1.0, "music/office_desktop.ogg")
    scene bg office desktop with wipeleft
    pause 0.3

    "When I come back, the editor has not even finished loading. Usually, it doesn't take {i}that{/i} long..."
    "... but when started, it downloads all the latest game assets (3D models, animations, sounds, etc.) uploaded by the artists and sound designers. And there is generally a lot to catch up in the morning."

    pause 0.8

    "Once the editor is ready, it automatically opens the default scene: a 3D \"sandbox\" made of a variety of geometrical shapes and enemies. It helps us testing various movements and interactions with the player character."
    "System designer, animators and programmers use the sandbox a lot, whereas level designers and level artists generally work directly on actual game areas."
    "But programmers are probably at the edge of the spectrum due to their extreme needs to test things quickly, and some (like me) exclusively use the sandbox."
    "The good side is that I'm {i}super excited{/i} when I'm testing the actual game — not something many employees would agree with, after spending one year in development and repetitive testing."

    pause 0.8

    "Anyway, here is my task for the incoming days: make the character shout a victory cry and play an upper-body animation when they kill a strong enemy."
    "Since the game is in an advanced stage of development, the character can already do all their main moves. So we are mostly adding advanced moves or aesthetic features like these now."
    "Though they all contribute to polishing the game, so they shouldn't be underestimated."

    pause 0.8

    jump .feature_specs

label .feature_specs:
    "Before diving into the code, I should ask the game designer for more details on the grunt feature."
    play sound audio.sfx.keyboard_typing_strong
    "I open Skype and send him a message, asking about the wanted behavior of the character, such as exact trigger conditions for the grunt."
    "While waiting for his answer, I open Visual Studio (it's a bulky app to write code). While Visual Studio opens, I start a YouTube video on –"

    gd "Hey! I saw your message."
    "I turn back and see the game designer right behind me. Oh, right, I always forget he's setting two desks behind."
    gd "The dude should grunt when he's hit by damage above a certain threshold, or special damage like fire. I've sent you the design doc for the feature specs."
    mc "Okay, thanks!"

    # feature specs explanation
    "The designer goes back to his desk as I notice a new email linking to the 'feature specs'."
    "The feature specs describes the requirements to fulfill to complete a feature (new game mechanic, menu option, etc.)"
    "To be honest, while other development environments may have proper requirements, things are more flexible in video games."
    "It's common that programmers tweak things a bit to make the feature easier to code or extend, as long as designers are okay."
    "There are also many 'edge cases' not described in the feature specs, so both programmers and designers will have to improvize when they encounter them."
    jump .architecture

label .architecture:
    "But let's keep the details for later. For now, I'll try to code something simple that does the job in most cases."
    "I grab my notebook (graciously offered by the company), and start sketching some possible ways to implement the feature. As usual, each method has advantages and disadvantages..."
    # Below, MC underestimates the actual time the generic solution will take. In reality, it will take 2x more time than expected.
    "a. Be specific: check for high and special damage directly in code, then play the grunt and 'badly hurt' animation."
    "It should be faster to code, probably finished by the end of the day, but less extensible."
    "b. Be generic: check for any damage received, then play an arbitrary voice and animation accordingly."
    "It should take longer to code, maybe 2 days, but extensible: designers will be able to edit the type of damage, voice and animation to add similar character reactions later."
    "I'm tempted to go with a. first, so I can finish my task today, and then maybe extend with b. later when we need a new animation."
    "But I fear that we'll never have the courage to switch to the more generic solution and keep adding more and more specific code, as usual."
    "What way do I go?"

    menu:
        "Be specific and code fast to make it work":
            $ store.extensible_architecture = False
            "Let's make it quick!"
        "Be generic and take time to make an extensible system":
            $ store.extensible_architecture = True
            "Let's write something clean and usable in the future!"

    play sound audio.sfx.keyboard_typing_strong
    "I dive into the project to find the correct places to plug the new functionality, and start adding new code."

    jump s2_1

label .end:
    "END"
