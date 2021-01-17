#!/usr/bin/env python3

from os import system
from gtts import gTTS
from datetime import datetime

if __name__ == '__main__':
	now = datetime.now()
	if now.minute in [0, 30]:
		curr_time = now.strftime("%I:%M %p")

		tts = gTTS(text='এখন সময় ' + curr_time, lang='bn')
		tts.save('time.mp3')

		system('ffplay -nodisp -autoexit -hide_banner ' + 'time.mp3')
