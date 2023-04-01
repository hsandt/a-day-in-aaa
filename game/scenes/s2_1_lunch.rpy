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

    "I put my computer to hibernation and leave the company building."

    jump .fast_food

label .fast_food:
    # no dedicated bg for street, so use empty canvas as fallback
    scene bg empty_canvas with Dissolve(1.0)
    # no dedicated ambient sound for street, so just fade out as fallback
    $ audio_stopFade(2.0)

    # TODO: INSERT SHOP CHOICE HERE - for now, auto-choose fast food
    "I go to the usual fast-food takeaway in the street in front of the building."
    "Since I left a bit late, the queue is pretty long. It even continues outside of the shop. As usual, most of the customers are employees of Black Rooster."
    # TODO: uncomment line below and INSERT NEW DIALOGUE
    # "I recognize a few ones and start talking with them while waiting."
    # inside the shop, audio is similar to office eating area so reuse it
    $ audio_crossFade(2.0, "music/office_eating_area.ogg")
    "I finally enter the shop and reach the counter."

    fast_food_clerk "Hey!! What can I get for you?!"
    mc "Erm... Today's soup and... two onion rings, please."
    fast_food_clerk "Do you want any drink?!"
    mc "Er... No, thank you."
    fast_food_clerk "Will that be all?!"
    mc "Yes..."
    fast_food_clerk "That'll be 4.12 euros."

    pause 0.3

    "With my lunch pack in hands, I go back to the office."
    jump .office_lunch

label .office_lunch:
    scene bg office eating_area with dissolve

    "Each floor has its own lunch area. It's not very big, but since employees come by wave at different times, the flow of people is spread across the lunch break."
    "On top of that, some developers eat out in fancier restaurants, while others eat at their desk to {i}maximize efficiency{/i} (or watch fun videos). So the space is generally enough for the remaining people."

    pause 0.3

    # INSERT SITTING CHOICE HERE - for now, auto-choose table with juniors
    "I find a table with some people I recognize and join the discussion."

    pause 1.0

    jump .table

label .table:
    junior_gameplay_programmer "There is Paris Games Week next week. Did you get your tickets?"
    junior_gd "No, it's always the same big studios with the same IPs showing trailers I will see on the net anyway."
    ui_artist "Including our company."
    junior_gd "Including our company."
    mc "I saw they had an indie square too."
    junior_gameplay_programmer "Yeah, but it's pretty small right? Indies are still marginal on the market."
    mc "Really? I think that if you put together sales and time spent, they are bigger than AAA."
    junior_gameplay_programmer "You're sure? From free-to-play to premium, people spend a lot of time on big games."
    ui_artist "Yesterday, I reached 100 hours on Alpha Legend..."
    "The online game that was released just last month? Wow."

    pause 0.5

    "I notice that there are 20 minutes left before the end of the lunch break. I want play a little before going back to work, so I greet them and throw what's left of my lunch bag in the bin."
    "The bins are already full of similar bags. Sure, cardboard and plastic boxes are recyclable, but in such a big company, every action's impact is multiplied by 100."
    "Is everything alright, or is it another ecological disaster?"

    pause 0.5

    "Anyway, time to play!"
    jump s2_2
