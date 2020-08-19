# -*- coding: utf-8 -*-
import eyed3

#Remove logs
eyed3.log.setLevel("ERROR")

def isMono(filename):
    audiofile = eyed3.load(filename)
    try:
        result = audiofile.info.mode == 'Mono'
    except Exception as err:
        result = False
    return result

def getGenre(filename):
	audiofile = eyed3.load(filename)
	#No genre
	if not audiofile.tag.genre:
		return None
	else:
		return audiofile.tag.genre.name.encode('utf-8')



	
