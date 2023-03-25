label s4_1:
    "Scene IV.1: Test and fix"
    jump .intro

label .intro:
    scene bg office desktop
    play music open_space.quiet

    jump .testing

label .testing:
    "I spend a few hours coding the new feature, using the architecture I considered this morning."
    "I spot a few bugs in my first implementation, so I go through a few more iterations to improve the code."
    "My biggest issue, as usual, is that it takes a lot of time to recompile the code after each change to test it."
    "Fortunately, there are always things to do during the compilation. Some watch videos or read comics, some chat with their colleagues."
    "In my case, I like reading programming articles or books. I know it sounds crazy inserting more work inside work, but it keeps me in the flow."
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
