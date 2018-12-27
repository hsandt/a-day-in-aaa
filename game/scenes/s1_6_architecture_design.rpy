label s1_6:
    "Scene I.6: Architecture design"
    jump .intro

label .intro:
    "Intro"
    scene bg open_space desktop
    play music open_space.quiet
    "MC explains the context: he's a game programmer in a big company and must implement a new feature"
    jump .architecture

label .architecture:
    "he ponders over which architecture is best, describing advantages and disadvantages, while writing the same on paper in the office"
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
