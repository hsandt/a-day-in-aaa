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
    "As I close the editor and start fixing the issues, I see an associate lead game designer joining the designers behind me."

    jump .lead_designer_comes_back

label .lead_designer_comes_back:
    associate_lead_gd "Okay, I got news from the meeting!"

    "While we're often told that the hierarchy is flat in the studio, truth is, the directors of each section would rarely come and talk to us without a very good reason."
    "In fact, I've only seen them a few times, from twenty meters away, during those crowded meetings with {i}everyone{/i}."
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

    "In my previous studios, we got some unreasonable demands from our publisher, and our producer was acting like a shield between them and our team. In Black Rooster, we are self-published, so everything is offset."
    "We need a good producer and leads, or the associate leads become the new shields."
    jump .satisfaction

label .satisfaction:
    "On my side, I prefer keeping a low profile and just get the job done."
    "... Before I joined the game industry, I complained a lot about how developers handled their projects, but I could do nothing as a player to change it."
    "I wanted to become a game developer to change that from the inside. But as I feared, in a big company like this, I just feel like a pawn again."
    "All I can do is make sure at least my code is not too bad."
    jump .work_end

label .work_end:
    "I keep working on my task until I'm satisfied with the result."
    "Fortunately, the \"tech team\" (programmers that work on the underlying tech rather than gameplay or UI) set up a few tricks to reduce iteration times, so it should only last 1 or 2 minutes this time."
    "(If you chose the quick solution in Scene I.6, the task ends here and MC asks a colleague for review)"
    "(Otherwise, the task is not over yet, and MC will have to finish later)"
    "Time for code review! (TODO)"
    jump s4_4
