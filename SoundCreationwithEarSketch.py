#		python code
#		script_name: Sound
#
#		author: Kshitij Singh
#		description:Composition Practice
#
#Setup
from earsketch import *

init()
setTempo(120)

#Music
chord= RD_UK_HOUSE__5THCHORD_2
secondaryBeat = COMMON_LOVE_VOX_ADLIB_1
fitMedia(chord, 1, 1, 16)
setEffect(1, VOLUME, GAIN, -60, 1, 5, 12)
setEffect(1, VOLUME, GAIN, 5, 12, -60, 16)
fitMedia(secondaryBeat, 2, 1, 12)
#ADD Effect
setEffect(2, DELAY,DELAY_TIME, 500)
#ADD EFFECT
setEffect(3, REVERB, REVERB_TIME, 200)


#Finish
finish()
