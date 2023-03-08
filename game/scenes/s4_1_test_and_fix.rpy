label s4_1:
    "Scene IV.1: Test and fix"
    jump .intro

label .intro:
    scene bg open_space desktop
    play music open_space.quiet

    jump .back_to_work

label .back_to_work:
    "(MC goes back to his desk)"
    jump .lead_designer_comes_back

label .lead_designer_comes_back:
    "(The lead designer comes back from a meeting where he thinks the producer has been pushing and rejecting features childishly)"
    "(The other designers show their sympathy and swear at the producer, but the lead decides to keep compromising to find the best middle ground for his team, and keep his job)"
    "(MC found the producer nice when he presented the game before, so he's surprised and suspect him of having a dual personality)"
    "(MC doesn't add to the complaints and prefers keeping a low profile)"
    "(In a sense, he protects them as they are free to keep on working without feeling like they are selling their souls)"
    "(The other designers have varied attitudes, some are indifferent and pragmatic, they know AAA works like that; some are hopeful they can do something to change it because 'it's our job to make the game better')"
    "(They note that some people start hopeful when they enter the company, and end up desperate, while others do the opposite. MC wonders which category he is in, but since he read articles on AAA before, he was not too surprised, nor too desperate)"
    jump .testing

label .testing:
    "(MC tests what he wrote in the morning, spots a few remaining bugs and fixes them)"
    "(However, this requires several iterations and MC complains about the long compile time)"
    "(Some developers use the compile time to watch videos or read comics, some have funny or serious talks, but MC prefers studying more programming languages and tools)"
    "(MC wonders if he's not crazy inserting more work time between work times)"
    "(But if feels good studying and learning new things as in the University)"
    jump .satisfaction

label .satisfaction:
    "(Thinking back at University, MC remembers he learned to a lot to avoid the past mistakes of other companies making games that turned bad when he was a child)"
    "(MC felt weak at the time and swore he'd become strong enough to change this. But now, he's still a mere employee and nothing really changed)"
    "(MC knows that he's just a junior, but he doesn't want to feel like one, esp. after working on student games handling most of the programming before.)"
    "(MC is not satisfied with his position at all, he is simply satisfying himself into that position to make life easier)"
    jump .work_end

label .work_end:
    "(MC finally finishes testing)"
    "(If you chose the quick solution in Scene I.6, the task ends here and MC asks a colleague for review)"
    "(Otherwise, the task is not over yet, and MC will have to finish later)"
    jump .end

label .end:
    "END"
