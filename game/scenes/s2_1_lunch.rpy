# Scene II.1: Lunch
label s2_1:
    jump .intro

label .intro:
    "Oh, it's already 12:40? I turn around and see that most of the people around me have already left for lunch."
    "I should probably get going too."
    "Lunch break has a flexible time of one hour between 12:00 and 14:00, but if you start your break after 13:00, you still have to get back to work at 14:00, so you're basically losing break time."
    "I wish we could carry unused break time over the next day just like holidays over the next year..."

    pause 0.5

    "Oh, looks like I forgot my bento today. I'll just get some food from one of the shops outside."
    jump .fast_food

label .fast_food:
    scene bg office eating_area
    $ audio_crossFade(2.0, "music/office_eating_area.ogg")
    "(INSERT SHOP CHOICE HERE - for now, auto-choose fast food)"
    "I go to the usual fast food shop in front of the company building. Not great for my diet, but... I don't have a diet."
    "Since I left a bit late, the queue is pretty long, it even continues outside of the shop. As usual, most of the customers are employees of the same company."
    "I recognize a few ones and start talking with them while waiting."
    "(INSERT DIALOGUE HERE)"
    "I finally reach the counter and ask for today's soup. The clerk is very enthusiastic. Maybe a bit too much, but at least he's efficient."
    "With my lunch pack in hands, I go back to the office."
    jump .office_lunch

label .office_lunch:
    "Each floor has its own lunch area. It's not very big, but since employees come at different times, some eat out and others eat at their desk, the space is generally enough."
    "(INSERT SITTING CHOICE HERE - for now, auto-choose table with juniors)"
    "I find a table with some other junior employees and join the discussion."
    jump .table_junior

label .table_junior:
    junior_programmer "There is Paris Games Week next week. Did you get your tickets?"
    junior_gd "No, it's always the same big studios with the same IPs showing trailers I will see on the net anyway."
    junior_artist "Including our company."
    junior_gd "Including our company."
    mc "I saw they had an indie square too."
    junior_programmer "Yeah, but it's pretty small right? Indies still seem pretty marginal on the market."
    mc "Really? I think that put together, they are bigger than AAA in terms of sales and time spent."
    junior_programmer "You're sure? Between free-to-play and premium with season passes, people spend a lot of time and money on big games."
    junior_artist "Yesterday, I had 100 hours on Monster Hunter World..."
    mc "Oh... (yet it was just released last month?)"
    "I notice it's time to go back to work, so I greet them and throw what's left of my lunch bag in the bin."
    "The bins are already full of similar bags. Sure, cardboard and plastic boxes are recyclable, but in such a big company, every action's impact is multiplied by 100."
    "So I can't help wondering if all this waste is processed right, or we're just part of another ecological disaster."
    "Once I'm done, I go back to my desk."
    jump s2_2
