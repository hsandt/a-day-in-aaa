init python:
    # We need to register the channel used by audio_crossFade below
    # Extra arguments after mixer seem optional, but we follow the documentation to be safe
    renpy.music.register_channel("music1", mixer="music", loop=True, tight=True)

    # Source: Mole
    # https://moley-face.tumblr.com/post/88819624433/i-just-figured-id-post-some-code-i-implemented
    # https://pastebin.com/Cn7xMcu0
    def audio_crossFade(fadeTime, music):
        oldChannel = None
        newChannel = None
        if renpy.music.get_playing(channel="music") is not None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = "music"
            newChannel = "music1"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is not None:
            oldChannel = "music1"
            newChannel = "music"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = None
            newChannel = "music"

        if oldChannel is not None:
            renpy.music.stop(channel= oldChannel, fadeout=fadeTime)

        if newChannel is not None:
            renpy.music.play(music, channel=newChannel, loop=None,fadein=fadeTime)

    # Added this method for fadeout only, agnostic of which channel was used for last music
    def audio_stopFade(fadeTime):
        if renpy.music.get_playing(channel="music") is not None:
            renpy.music.stop(channel="music", fadeout=fadeTime)

        if renpy.music.get_playing(channel="music1") is not None:
            renpy.music.stop(channel="music1", fadeout=fadeTime)
