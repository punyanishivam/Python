def song_decoder(song):
    song = song.replace("WUB", " ")
    song = song.replace("     ", " ")
    song = song.replace("    ", " ")
    song = song.replace("   ", " ")
    song = song.replace("  ", " ")    
    
    if song.startswith(" "):
        song = song[1:]
    if song.endswith(" "):
        song = song[:-1]
    return song

song = "AWUBWUBWUBBWUBWUBWUBC"
print(song_decoder(song))