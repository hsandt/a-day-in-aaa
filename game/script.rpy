﻿# Declare characters used by this game. The color argument colorizes the
# name of the character.
define narrator = Character(None, window_background=Image("gui/textbox_narration.png", xalign=0.5, yalign=1.0))
define mc = Character("Me", color="#247336")
define neighbor_gd = Character("Neighbor game designer", color="#712473")
define junior_programmer = Character("Junior programmer", color="#735724")
define junior_artist = Character("Junior artist", color="#247173")
define junior_gd = Character("Junior game designer", color="#712473")
define junior_ui_designer = Character("Junior UI designer", color="#9c23a6")
define programmer = Character("Programmer", color="#735724")
define artist = Character("Artist", color="#247173")
define gd = Character("Game designer", color="#712473")
define ui_designer = Character("UI designer", color="#9c23a6")
define associate_lead_programmer = Character("Associate Lead programmer", color="#735724")
define associate_lead_artist = Character("Associate Lead artist", color="#247173")
define associate_lead_gd = Character("Associate Lead game designer", color="#712473")
define associate_lead_ui_designer = Character("Associate Lead UI designer", color="#9c23a6")

# Story event flags
default extensible_architecture = False

label start:
    # Game setup

    # Hide the text box during pause statements, as no text is shown
    window hide

    jump s1_6
    return
