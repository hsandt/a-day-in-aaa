label s2_2:
    "Scene II.2: Play Break"
    jump .intro

label .intro:
    scene bg open_space desktop
    play music open_space.quiet

    jump .watch_play

label .watch_play:
    "(Background should be other people playing)"
    "(MC sees colleagues having fun on local multi-player games in competition, and others playing indie)"
    "(MC could probably have a decent coop play but gives up on competition and prefers playing alone)"
    jump .play_game

label .play_game:
    "(MC starts playing a game alone)"
    "(MC automatically chooses Starcraft II)"
    "(MC plays for some time)"
    jump .colleagues_arrive

label .colleagues_arrive:
    "(Colleagues arrive from various clubs and explain they have been practicing healthy or artistic activities)"
    "(While still playing, MC hears the conversation and thinks he should do the same, but doesn't feel the courage to go out at noon)"
    "(MC thinks at least, people are not criticized for playing all noon here. But it is double-edged)"
    jump .break_end

label .break_end:
    "(The break is over, but MC is still playing as the Starcraft session was harder than expected)"
    "(MC automatically chooses to continue playing despite going over the break end time)"
    "(However, MC sees people around him stop playing and gets worried he gives a bad image.)"
    "(Eventually, MC stops playing and gets back to work)"
    jump s4_1
