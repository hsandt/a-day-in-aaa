label s2_1:
    "Scene II.1: Lunch"
    jump .intro

label .intro:
    scene bg eating_space
    play music eating_space.quiet
    "(MC thinks he may miss some break time due to being late, because unfortunately delaying the break start time doesn't delay the break end time!)"
    "(MC realizes he doesn't have a bento and wonders where to go get some food.)"
    "(Player must choose where to go to buy food)"
    "(MC automatically goes to the fast food)"
    jump .fast_food

label .fast_food:
    "(MC waits in the queue, takes the lunch pack and comes back to the office)"
    jump .office_lunch

label .office_lunch:
    "(Back in the office lunch area, MC wonders where to sit)"
    "(Player must choose whom to sit with)"
    "(MC automatically goes to table A, with more junior profiles)"
    jump .table_junior

label .table_junior:
    "(MC discusses AAA domination)"
    "A ~ The National Game Show will start next week. Did you get your tickets?"
    "B ~ No, it's always the same big studios with the same IPs showing trailers I will see on the net anyway."
    "C ~ Including our company."
    "B ~ Of course."
    "A ~ Sure I'd also like to see more indies, but they seem pretty marginal on the market."
    "MC ~ What? I think that put together, they are bigger than AAA in terms of sales and even time spent!"
    "A ~ You're sure? With the season pass and all, people spend a lot of time and money on big games."
    "C ~ Yesterday I had 100 hours on Monster Hunter World..."
    "MC ~ Oh... (I think it was released last month?)"
    "(MC finishes eating, and goes back to his desk)"
    jump .play_break

label .play_break:
    scene bg open_space desktop
    play music open_space.quiet
    "Play break"

label .end:
    "END"
