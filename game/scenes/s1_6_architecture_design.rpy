label s1_6:
    "Scene I.6: Architecture design"
    jump .intro

label .intro:
    scene bg open_space desktop
    play music open_space.quiet

    # where I am, who I am, when I am, what I'm supposed to do
    "The weekly meeting was pretty efficient this morning. We summed up project status on the game, I got assigned a new programming task and we ate a dozen chocolates."
    "The project is an open-world third-person action-adventure game, so expect the player character to have a variety of moves at his disposal. My task is to implement a combo detection system."
    "No, not a combo system that allows the player character to chain cool moves together. Just a system that detects when the player chained certain actions within a certain time frame."
    "The former would be cooler, but I guess the leads are not ready to give me such responsibility."

    "Anyway, let's have a look at the {i}feature specs{/i}. "
    jump .feature_specs

label .feature_specs:
    # feature specs explanation
    "Feature specs are basically requirements to fulfill to complete a feature (new game mechanic, menu option, etc.)"
    "But let's be honest, {i}requirement{/i} is the hard word used in environments a bit more strict than the game industry. In reality, we have a list of things the game designers want to see work in the game, and that we should start with."
    "From then on, there is a lot of flexibility on how the game should behave exactly. We often take care of edge cases directly in the code, sometimes asking the designers for a few more details."

    jump .architecture

label .architecture:
    "He ponders over which architecture is best, describing advantages and disadvantages, while writing the same on paper in the office"
    "He tends to underestimate the actual time the generic solution will take"
    "The quick and dirty solution:
    {p}- will work fine for this use case
    {p}- ...as long as nobody tries to extend the feature, including the MC
    {p}- only a few functions to implement"
    "- will be finished in the day, can even be code reviewed
    {p}- ...but the MC will feel ashamed it that gets through and gets forgotten"
    "The generic solution:
    {p}- will work for many use cases
    {p}- ...but may feel over-engineered
    {p}- Add a full class."
    "- It will guarantee future extensibility
    {p}- ...but will ask me more time. Probably 3 days. But the MC thinks only 1.5."
    jump s2_1

label .end:
    "END"
