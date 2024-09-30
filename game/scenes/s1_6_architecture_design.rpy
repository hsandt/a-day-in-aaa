# Scene I.6: Architecture design
label s1_6:
    jump .intro

label .intro:
    scene bg office open_plan with Dissolve(1.0)
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

    "Once the editor is ready, it automatically opens the default \"sandbox\" scene: a small 3D map made of a variety of geometrical shapes and enemies."
    "It helps us testing various movements and interactions with the player character."
    "System designer, animators and programmers use the sandbox a lot, whereas level designers and level artists generally work directly on actual game areas."
    "But programmers are probably at the edge of the spectrum due to their extreme needs to test things quickly, and some (like me) exclusively use the sandbox."
    "The good side is that I'm {i}super excited{/i} when I'm testing the actual game — not something many employees would agree with, after spending one or two years in development and repetitive testing."

    pause 0.8

    "Anyway, here is my task for the incoming days: make the player character shout a victory cry and play an upper-body animation when they beat a strong enemy."
    "Since the game is in an advanced stage of development, the character can already do all their main moves. So we are mostly adding advanced moves or aesthetic features like these now."
    "Though they all contribute to polishing the game, so they shouldn't be underestimated."

    pause 0.8

    jump .feature_specs

label .feature_specs:
    "Before diving into the code, I should ask the game designer for more details on the new feature."

    play sound audio.sfx.keyboard_typing_strong
    "I open Skype and send him a message, asking about additional information like what a \"strong enemy\" means."
    "While I wait for an answer, I open Visual Studio (a bulky programming app for Windows). While Visual Studio opens, I start a YouTube video on —"

    character_gd "Hey! I saw your message."

    "I turn back and see the game designer standing just behind me. Right, he was sitting just two desks away."

    character_gd "So, the idea is that an enemy at least 10 levels above the player is considered \"strong\". Beating it will make your dude boast. And \"beating\" is basically killing, but having the enemy surrender also works."
    character_gd "I've sent you the feature specs for more details."
    mc "Okay, thanks!"

    "I actually enjoy these chatting moments, they make me feel part of the team and responsible for my tasks."

    # feature specs explanation
    "As the designer goes back to his desk, I notice a new email linking to the \"feature specs\"."
    "The feature specs describes the requirements to fulfill to complete a feature (new game mechanic, menu option, etc.)."
    "To be honest, while other development environments may have proper requirements, things are more flexible in video games."
    "It's common that programmers tweak things a bit to make the feature easier to code or extend, as long as designers are okay."
    "There are also many special cases or \"edge cases\" not described in the feature specs, so both programmers and designers will have to improvize when they encounter them."
    jump .architecture

# TODO: add Character psychology from Scenes doc:
# responsibility of architecturing => confidence
# feature ownership => legitimity to contact people
# remind of high school and talking to both programmers and plain game lovers

label .architecture:
    "But let's keep the details for later. For now, I'll try to code something simple that does the job in most cases."
    # TODO SFX: add pen SFX
    "I grab my notebook (graciously offered by the company), and start sketching some possible ways to implement the feature. As usual, each method has pros and cons..."
    "Method A: Be specific\nCheck for enemy death or surrender and level directly in code, then play the victory cry and pose if conditions are met."
    "It should be faster to code (probably finished by the end of the day), but less flexible."
    "Method B: Be generic\nCheck for generic condition on enemy status, then play an arbitrary voice and animation if the condition is verified."
    # Below, MC underestimates the actual time the generic solution will take. In reality, it will take 2x more time than expected.
    "It should take longer to code, maybe 2 days, but flexible: designers will be able to edit the condition for being \"strong\" and play different voices and animations depending on whether the enemy was killed or surrendered."
    "The classic process is to start specific (A) to get something to work early, then extend to more generic code (B) when we need to handle more cases."
    "However, programmers know by experience that designers are likely to change conditions and effects later in development. As a result, thinking ahead and making the behavior flexible from the start is often beneficial."
    "There is also a risk that I start with method A, but nobody will have the courage to switch to B later, so we'll keep adding more and more rules coupled with exceptions, turning the codebase into a grammar handbook."
    "So, what way do I go?"

    menu:
        "A. Be specific: code fast to make it work early":
            $ store.extensible_architecture = False
            "Let's make it quick!"
        "B. Be generic: take time to make a flexible system for later":
            $ store.extensible_architecture = True
            "Let's write something clean and easily reusable in the future!"

    play sound audio.sfx.keyboard_typing_strong
    "I dive into the project's source code to find the correct places to plug the new behavior, and start coding."

    pause 1.5

    jump s2_1

label .end:
    "END"
