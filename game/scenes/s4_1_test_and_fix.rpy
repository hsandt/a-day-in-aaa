# Scene IV.1: Test and fix
label s4_1:
    jump .intro

label .intro:
    jump .testing

label .testing:
    play sound audio.sfx.keyboard_typing_strong
    "Back to work, I get the latest code changes in the project to make sure I'm up-to-date. I then start coding the victory cry, using the method I considered this morning."

    if extensible_architecture:
        "Writing a generic system will take a few days and require a big code change at once, but it generally makes designers and other programmers happy."
        "Plus, nothing prevents me from adding elements bit by bit, like the victory cry first, and then the pose."
    else:
        "I'll just add minimal code to get the job done, so that means less stress and a smaller code change to have reviewed by other programmers."

    pause 0.5

    "I hit compile to test my first draft."
    "Compiling code is a necessary step to run the application in some programming languages, like the one we're using."
    "The problem on big games is that it can take quite a lot of time, esp. after adding new files or other structural changes."
    "Considering the new files I added for the first draft {i}and{/i} the ones added by other programmers that I just retrieved from the latest code changes, the first compilation will be pretty long, probably 3 to 5 minutes."
    "Fortunately, there are always things to do during the compilation. Some watch videos or read comics, some chat with their colleagues."
    "Personally, I like reading programming articles or books. I know it sounds crazy inserting more work inside work, but it keeps me in the flow."

    pause 0.5

    "The game editor suddenly pops up, telling me what it has finished compiling. I run the sandbox to test the character behavior, and spot a few bugs in this first version."
    "I debug a bit what is happening through the code, but I realize most of the mistakes are trivial. I could have avoided them by paying more attention."
    "It's often faster to write a little, then test and improve code over many iterations than trying to handle all the cases at once. However, when compilation time is long, it's worth thinking more ahead."
    "I close the game editor and start fixing the issues."
    "To make it easier to debug the victory cry repeatedly, I also add a debug line: a temporary line of code that bypasses some conditions and triggers the cry in more cases than it should."
    "Of course, I need to remember removing it before I submit the change."

    pause 0.5

    "A few minutes later, I see an associate lead game designer joining the designers behind me."

    jump .lead_designer_comes_back

label .lead_designer_comes_back:
    scene bg office open_plan with dissolve
    associate_lead_gd "Okay, I got news from the meeting!"

    "While we're often told that the hierarchy is flat in the studio, truth is, the directors of each section would rarely come and talk to us, in that corner of the studio, without a very good reason."
    "In fact, I've only seen them a few times, from twenty meters away. You know, during those crowded meetings with {i}every employee{/i}."
    "On the contrary, it's pretty common to see associate leads wander around, as they act like a bridge between the upper and lower layers."

    progression_gd "How did they find the design of loot quality increase over play time?"
    associate_lead_gd "Oh, they just redrew the curve a little to make sure players spend a {i}little{/i} more time playing before they can get better gear."
    progression_gd "So more than the suggested one hour? Like what, two hours?"
    associate_lead_gd "More like four."
    progression_gd "A-ha.{w=0.5} Too bad we don't sell loot boxes anymore."

    pause 0.5

    progression_gd "What else?"
    associate_lead_gd "The producer gently suggested to add paragliding. He found it cool when he tried Alpha Legend the other day."
    "The game designer on player character & controls caught that sentence and joins in."
    character_gd "Wow, wait. Does that \"suggested\" means \"required\"? Because the level designers already sketched most of the map with simple climbing and jumping abilities in mind. Paragliding would break the level design!"
    associate_lead_gd "I tried to explain that, but we'll need the lead level designer's support on this."
    character_gd "Okay, let's have a talk with her."

    "In my previous studio, we got some unreasonable demands from our publisher, and our producer was acting like a shield between them and our team. In Black Rooster, we are self-published, so everything is offset."
    "We need a good producer and leads, or the associate leads become the new shields."

    pause 0.5

    jump .satisfaction

label .satisfaction:
    "About that paragliding thing... is there anything I could do to help as a programmer?"
    "If the designers don't manage to reject that feature, and it falls on me to implement it, would I have the courage to just... refuse? And what would that change, if somebody else does it in the end?"

    pause 0.5

    "... Bah, it's not like they'll give such a big task to a fresh recruit like me."

    pause 0.5

    jump .work_end

label .work_end:
    scene bg office desktop with dissolve
    "Anyway, back on my task. I search for some music on YouTube and find a video named \"2-hour Ultra Epic Motivational Anime OST Collection\". It's full of series I haven't even watched, but I'll trust it."

    play sound audio.sfx.keyboard_typing_strong
    "I keep working on the victory feedback over a few more iterations."
    "Fortunately, compilations are faster after the first time."

    # TODO: either create an even quieter variant of ambient sound, or manually decrease volume
    # (but will also affect own keyboard/mouse SFX integrated in ambient sound)
    "After more work (interspersed with company chat involving latest game releases, and pets), I see that it's getting late. Most of the employees have already left."
    "The room is now much quieter, and keyboard sounds are taking over voices. Actually, I kinda like this ambiance, and I'm generally quite productive in these last hours of work."
    "Some researches say we are only productive for 4 hours of office work. That sounds extreme, but if it's true, I should definitely ask for a special permission to come at the office in the afternoon."

    pause 0.5

    "I'll probably leave soon too, so let's assess the work done today."

    if extensible_architecture:
        "Half of the behavior is working, but as expected, writing a generic solution takes quite a lot of time. There are also a few odd cases where the player character plays the victory cry when they shouldn't."
        "So, I suppose I'll finish this another day."
    else:
        "It was easy to write the specific code, so the feature is ready to be reviewed. A \"code review\" is a process where another programmer goes through a code change to spot potential issues; or bad formatting."
        "I turn to one of the remaining programmers."
        mc "Mind doing a code review?"
        lead_gameplay_programmer "What is it about?"
        mc "Playing the victory shout and pose when beating a strong enemy."
        lead_gameplay_programmer "Hmm... I could review the code change, but we should avoid submitting it so late, to avoid bad surprises tomorrow, when designers and artists download the midnight build."
        mc "Tomorrow, then?"
        lead_gameplay_programmer "Sure."

    pause 0.5

    "I check for new messages on my computer one last time and shut down the computer."
    jump s4_4
