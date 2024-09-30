# Scene III.1: Implement
label s3_1:
    jump .intro

label .intro:
    # uncomment if coming from a scene with a different BG
    # scene bg office open_plan with Dissolve(1.0)
    # $ audio_crossFade(2.0, "music/office_open_plan.ogg")

    # TODO: move text from S4.1

    # check extensible_architecture var

    jump .implement_quick
    # or
    jump .implement_generic

label .implement_quick:

    jump .hear_designer_talk

label .implement_generic:

    jump .hear_designer_talk

label .design_edge_case:

    call .ask_designer_about_edge_case

    jump .hear_designer_talk

label .ask_designer_about_edge_case:
    return

label .hear_designer_talk:
    # choice to participate
    call .the_intruder

    jump .hopeful_vs_jaded_devs

label .the_intruder:
    return

label .hopeful_vs_jaded_devs:
    jump .implement_end

label .implement_end:
    pause 0.5

    jump s4_1
