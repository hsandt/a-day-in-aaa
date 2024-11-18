# Scene III.1: Implement
label s3_1:
    jump .intro

label .intro:
    # uncomment if coming from a scene with a different BG
    # scene bg office open_plan with Dissolve(1.0)
    # $ audio_crossFade(2.0, "music/office_open_plan.ogg")

    "Back to work, I get the latest code changes in the project to make sure I'm up-to-date. I then start coding the victory cry, using the method I considered this morning."

    if extensible_architecture:
        call .implement_generic
    else:
        call .implement_quick

    jump .design_edge_case

label .implement_quick:

    "As decided this morning, I'll just add minimal code to get the job done, so that means less stress and a smaller code change to have reviewed by other programmers."

    # TODO

    return

label .implement_generic:

    "As I mentioned this morning, writing a generic system will take a few days and require a big code change at once, but it generally makes designers and other programmers happy."
    "Plus, nothing prevents me from adding elements bit by bit, like the victory cry first, and then the pose."

    "Before writing a new system, it's good to draft the architecture on paper first."
    "I open my notebook and start sketching the different components I need."

    # TODO image: open notebook
    # TODO sfx: pencil

    "1. EnemyStatusChecker: a component that checks the current status of an enemy."
    "In this case, we'll be interested in death and surrender states, as well as the enemy level so see if it is strong."
    "2. PlayerCharacterReaction: a component that defines which reaction the player character should play when a certain condition is fulfilled."
    "Reaction may contain an animation and a voice line, which we will fill with the Victory Pose and Victory Cry."

    "Wait, should I make them even more generic? Like CharacterStatusChecker and CharacterReaction?"
    "That would allow enemies to also take a victory pose when they defeat a player character... Fine, let's do that."

    "Another big question is when to execute the check: should I only check enemy status when the player character interacts with it (for instance damage it)?"
    "Or should I monitor the enemy's status every frame in case something else kills it, such as a prop explosion?"
    "Checking the enemy status only on certain interactions may miss too many cases, while checking it every frame sounds overkill."
    "I should be pragmatic instead, and simply check the enemy status when it changes."
    "There should be a centralized place in code where the enemy is declared dead, or surrenders."

    "Finally, I need to decide how to connect the two components."
    "A classic trick is to have CharacterReaction register itself to CharacterStatusChecker, then have the Checker trigger the Reaction when appropriate."

    "I finish drawing boxes and arrows connecting them."
    "OK, let's go with that."

    pause 0.5

    "A few minutes after I start, I'm struck by doubts again."
    "It seems that I need to create more classes and data structures as I thought to make the whole thing work."
    "For instance, the status check condition may need their own data structure to store status types and character level. And for the character reaction, store animation and voiceline."
    "That makes me create a bunch of new files in the project and I wonder if that's not overkill. Especially as most files only contain a few lines."
    "But that's what programming modularity is about, after all."
    "Besides, I learned in previous projects that it's often better to just stick to the plan and accommodate later, than waste time hesitating too much."
    "In other words, quick iterations beat having the perfect plan."
    "Plus, even if it takes more time to code, I still get my wages at the end of the month."
    "So, I keep coding following my draft and adjusting here and there."

    return

label .design_edge_case:

    pause 0.5

    "After a while, I realize that an edge case I thought about earlier is actually important to tackle:"
    "What if the enemy gets killed by something else than the player character, such as a prop explosion or some ally dealing the finishing blow?"
    "Should the player still play the Victory Pose, or do nothing?"
    "Actually, if another character stole the kill, they could play a Frustrated animation! Ehehe."

    "Hm, I suppose that's up to Design to decide."
    "But wait, I how Game Design and UX Design too, maybe I can find the right answer on my own."

    menu:
        "What should I do?"
        "Only play Victory Pose when the player character defeats the strong enemy.":
            call .play_victory_pose_only_own_hit
        "Also play Victory Pose when an external factor caused enemy death or surrendering":
            call .play_victory_pose_also_external_cause
        "Ask the game designer":
            call .ask_designer_about_edge_case

    call .ask_designer_about_edge_case

    jump .hear_designer_talk

label .play_victory_pose_only_own_hit:
    return

label .play_victory_pose_also_external_cause:
    return

label .ask_designer_about_edge_case:
    return

label .hear_designer_talk:
    # choice to participate
    call .the_intruder

    jump .hopeful_vs_jaded_devs

label .the_intruder:
    return

label .hopeful_vs_jaded_devs:
    jump .implement_end

label .implement_end:
    pause 0.5

    jump s4_1
