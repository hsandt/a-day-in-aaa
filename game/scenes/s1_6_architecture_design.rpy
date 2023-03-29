label s1_6:
    "Scene I.6: Architecture design"
    jump .intro

label .intro:
    scene bg office open_plan
    play music office_open_plan

    # where I am, who I am, when I am, what I'm supposed to do
    "The weekly meeting was pretty efficient this morning. We summed up project status on the game, I got assigned a new programming task and we ate a dozen chocolates."
    "We are working on an open-world third-person action-adventure game, and I'm part of team that handles character control and actions."
    "My new task is to make the character grunt and play a specific animation when they get badly hurt (I'll call it 'grunt feature' for short)."
    "Development is already pretty advanced and the character already has all their basic moves done."
    "So it's very common at this stage to just add minor aesthetic features like these, especially for a junior programmer."
    "They all contribute to polishing the game and making it look cool though, so I don't complain."
    jump .feature_specs

label .feature_specs:
    scene bg office desktop
    $ audio_crossFade(2.0, "music/office_desktop.ogg")
    "I sit back at my computer."
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
