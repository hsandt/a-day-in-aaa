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

    # TODO: move after 1st compilation
    # "I spot a few bugs in my first implementation, so I go through a few more iterations to improve the code."
    # "Further compilations should be faster, thanks to a few tricks we use to optimize small incremental changes."
    jump .lead_designer_comes_back

label .lead_designer_comes_back:
    associate_lead_gd "Hey!"
    "... at least, until somebody comes. I turn around my chair and see an enthusiastic associate lead game designer."
    "While the open space is flat, the hierarchy is still prominent as you'd expect, so the big leads rarely come as far as this corner of the studio."
    "On the contrary, it's pretty common that associate leads directly talk to us."
    "In this case though, he was addressing his fellow designers."

    gd "How was the meeting?"
    associate_lead_gd "Not bad... I showed them my proposal for gradual loot quality increase over play time."
    gd "Let me guess... the producer rejected it with no good reason?"
    associate_lead_gd "Not exactly... He just redrew the curve a little to make sure players spend a little more time playing before they get better gear."
    associate_lead_gd "Four hours here... Five hours there..."
    gd "That's ridiculous. We talked about one hour per level last time. Typical of mindless RPG-ization."
    gd "The point of progression design is to increase the game's lifespan, but it doesn't help if the player gets bored and drops before the end."

    "So, usually, the producer's job is to make sure the team can properly work on the product and release it in time."
    "But here, anyone with a high place in the hierarchy can give their opinion on anything."
    "Which would be great... if the process was democratized and led to actual discussions."

    associate_lead_gd "Also, he pushed a request to add paragliding. He found it cool when he tried Alpha Legend the other day."
    gd "The game that was released last week? Okay, sure, but we've already designed most of the map with simple climbing and jumping abilities in mind."
    gd "Adding paragliding would break the level design!"

    "Now I'm surprised. I can understand a little tweak here and there, but it's hard for me to believe the producer would go that far. I mean, when I saw him during the big meeting with everyone, he looked nice."
    "From twenty meters away."

    associate_lead_gd "I tried to explain that, but we'll need the lead level designer's support on this."
    gd "Okay, let's have a talk with her."

    "I see, so the associate leads act like a bridge between the top management and their team."
    "Or rather, they act like a shield, doing all the negotiations to find the best middle ground for their team."
    "In other words, they do more compromises, and allow their team to keep their integrity. And also swear when they want."
    "I suppose the job is less stressful in studios with better executives."
    jump .satisfaction

label .satisfaction:
    "On my side, I prefer keeping a low profile and just get the job done."
    "... Before I joined the game industry, I complained a lot about how developers handled their projects, but I could do nothing as a player to change it."
    "I wanted to become a game developer to change that from the inside. But as I feared, in a big company like this, I just feel like a pawn again."
    "All I can do is make sure at least my code is not too bad."
    jump .work_end

label .work_end:
    "I keep working on my task until I'm satisfied with the result."
    "(If you chose the quick solution in Scene I.6, the task ends here and MC asks a colleague for review)"
    "(Otherwise, the task is not over yet, and MC will have to finish later)"
    "Time for code review! (TODO)"
    jump s4_4
