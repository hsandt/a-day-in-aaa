label s2_2:
    "Scene II.2: Play Break"
    jump .intro

label .intro:
    # TODO: replace with open space overview
    scene bg office desktop
    play music open_space.quiet

    jump .watch_play

label .watch_play:
    "When I enter the room, I see some of my colleagues playing online together on free-to-play, and others playing solo indie games."
    "I haven't played online for a while, yet alone the recent titles, so I don't think I'll be able to withstand the competition."
    "So I'll just pick a solo game today, as usual."
    jump .play_game

label .play_game:
    "(INSERT GAME CHOICE HERE - for now, auto-choose Starcraft II)"
    "Let's go with Starcraft II today."
    "I launch the game and play a bit of campaign. Yeah, the mode every serious player has already finished years ago."
    "But what do you want? I hadn't played Starcraft since Brood War in the 2000s, so my RTS-fu is a little rusty."
    "I feel like I improved since last time though, so I try a versus AI at Hard difficulty – how can I hope playing online if I can't even beat the AI?"
    "I get crushed."
    "I turn to my knowledgeable colleague for advice.\n'Disappointing', he says."
    "'You need to memorize your build order. Your {b}build order{/b}!'"
    jump .colleagues_arrive

label .colleagues_arrive:
    "As the end of lunch break draws nearer, I see more and more colleagues coming back to the room."

    programmer "So, how was the gym?"
    artist "It was fine, but the leg machine was broken. AGAIN."
    programmer "Like our codebase."
    artist "And you? How was improv?"
    programmer "Great! The new guy had some hilarious lines!"
    programmer "... like our codebase."

    # Alternative dialogue
    # programmer "So, how was the gym?"
    # artist "Fine, but the leg machine was broken, so I had to improvize. Speaking of, how was the improv club?"
    # programmer "Great! The new guy had some hilarious rejoinders!"

    "I realize how other developers have regularly been practicing healthy or artistic activities. Maybe I should join a club too?"
    "... or I could keep sitting here and playing every noon, as usual."
    "Thinking of it, it's great that we are all adults and we can just do what we want on our spare time."
    "But sometimes I'd need some life coach to get me to do more varied things, as I used to at school."
    "OK, I got a few minutes left. Ready for another versus?"
    jump .break_end

label .break_end:
    "Before I notice, break time is over, but I haven't finished my game yet. The opponent is tougher than expected."
    "(INSERT GAME CHOICE HERE on whether to keep playing - for now, auto-choose to continue playing)"
    "Believing in my incoming victory, I push the game a little further. But it's now quarter past two and I'm still far from it."
    "Should I just give up?"
    "The mood slowly changing in the room. People are getting back to work, speaking less and typing more."
    "I quickly glance at the room to check that nobody cares about me."
    "They don't, yet as time goes on, I feel an invisible pressure growing on my back."
    "Eventually, I manage to grab my victory (nothing to be proud of, I set the AI to Medium this time) –"
    "– and at the same time my peace of mind, as I close my game and open Visual Studio."
    jump s4_1
