# Declare characters used by this game. The color argument colorizes the
# name of the character.
define narrator = Character(None, window_background=Image("gui/textbox_narration.png", xalign=0.5, yalign=1.0))
define mc = Character("Me", color="#7b401c")

define junior_gameplay_programmer = Character("Junior gameplay programmer", color="#977100")
define ui_programmer = Character("UI programmer", color="#646d2a")
define ai_programmer = Character("AI programmer", color="#820097")
define lead_gameplay_programmer = Character("Lead gameplay programmer", color="#970000")
define junior_gd = Character("Junior game designer", color="#4c7126")
define character_gd = Character("Character game designer", color="#307126")
define progression_gd = Character("Progression game designer", color="#146c6b")
define associate_lead_gd = Character("Associate lead game designer", color="#146c29")
define junior_artist = Character("Junior artist", color="#009796")
define ui_artist = Character("UI artist", color="#006097")
define level_artist = Character("Level artist", color="#002797")
define animator = Character("Animator", color="#362f68")
define senior_animator = Character("Senior animator", color="#4a0097")
define junior_ui_designer = Character("Junior UI designer", color="#643f8a")
define senior_ui_designer = Character("Senior UI designer", color="#a906c3")
define associate_lead_artist = Character("Associate lead artist", color="#71265f")

define fast_food_clerk = Character("Fast food clerk", color="#b95c00")

# Story event flags
default extensible_architecture = False

label start:
    # Game setup

    # Hide the text box during pause statements, as no text is shown
    window hide

    jump s1_6
    return
