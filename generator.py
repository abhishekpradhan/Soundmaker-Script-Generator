'''
Created by Abhishek Pradhan for MUS448, Spring 2011

The purpose of this program is to generate a script file that can be passed into SoundMaker Script
'''
import random
import sys

class Partial:
	'''Representation of a Partial'''
	def __init__(self):
		self.envPart = random.randint(5, 8)
		self.scalePart = random.uniform(0, 1)
class Modifier:
	'''Sound Modifier'''
	def __init__(self):
		self.ampEnv = random.choice([1,2,3])
		self.ampScale = random.uniform(0, 1)
		self.noteEnv = random.choice([1,2,3])
		self.noteScale = random.uniform(0, 1)

class Sound:
	''' Representation for a Sound '''
	def __init__(self):
		self.stime = random.randint(start, time - 1)
		self.dur = random.randint(1, time - self.stime)
		self.numPart = random.randint(1, 8)
		self.freq = random.randint(100, 999)
		self.loud = random.randint(32, 256)
		self.deviation = random.uniform(0, 1)
		self.partials = []
		for i in range(0, self.numPart):
			self.partials.append(Partial())
		if random.randint(0, 1) == 0:
			self.vibrato = None
		else:
			self.vibrato = Modifier()
		if random.randint(0, 1) == 0:
			self.tremolo = None
		else:
			self.tremolo = Modifier()
		if random.randint(0, 1) == 0:
			self.glissando = None
		else:
			self.glissando = Modifier()
			self.glissando.ampEnv = random.choice([4, 25])
		self.panEnv = 1
		self.panScale = random.uniform(0, 1)
		self.room = random.uniform(0, 1)

def generateFile(fileName, sounds):
	scriptFile = open(fileName, 'w')
	scriptFile.write("numSounds\t" + str(len(sounds)) + "\n\n")

	for sound in sounds:
		scriptFile.write("stime\t\t" + str(sound.stime) + "\n")
		scriptFile.write("dur\t\t" + str(sound.dur) + "\n")
		scriptFile.write("numPart\t\t" + str(sound.numPart) + "\n")
		scriptFile.write("freq\t\t" + str(sound.freq) + "\n")
		scriptFile.write("loud\t\t" + str(sound.loud) + "\n")
		scriptFile.write("deviation\t" + str(sound.deviation) + "\n")

		for i, partial in enumerate(sound.partials):
			scriptFile.write("envPart" + str(i + 1) + "\t" + str(partial.envPart) + "\n")
			scriptFile.write("scalePart" + str(i + 1) + "\t" + str(partial.scalePart) + "\n")
		
		if sound.vibrato != None:
			scriptFile.write("    \t\tV\n")
			scriptFile.write("ampEnv\t\t" + str(sound.vibrato.ampEnv) + "\n")
			scriptFile.write("ampScale\t" + str(sound.vibrato.ampScale) + "\n")
			scriptFile.write("noteEnv\t\t" + str(sound.vibrato.noteEnv) + "\n")
			scriptFile.write("noteScale\t" + str(sound.vibrato.noteScale) + "\n")

		if sound.tremolo != None:
			scriptFile.write("    \t\tT\n")
			scriptFile.write("ampEnv\t\t" + str(sound.tremolo.ampEnv) + "\n")
			scriptFile.write("ampScale\t" + str(sound.tremolo.ampScale) + "\n")
			scriptFile.write("noteEnv\t\t" + str(sound.tremolo.noteEnv) + "\n")
			scriptFile.write("noteScale\t" + str(sound.tremolo.noteScale) + "\n")

		if sound.glissando != None:	
			scriptFile.write("    \t\tG\n")
			scriptFile.write("Env\t\t" + str(sound.glissando.ampEnv) + "\n")
			scriptFile.write("Scale\t\t" + str(sound.glissando.ampScale) + "\n")

		scriptFile.write("    \t\tE\n")
		scriptFile.write("panEnv\t\t" + str(sound.panEnv) + "\n")
		scriptFile.write("panScale\t" + str(sound.panScale) + "\n")
		scriptFile.write("room\t\t" + str(sound.room) + "\n\n")
	
	scriptFile.write("name\t\t" + fileName + ".aiff\n")
	scriptFile.close()

def mainmenu():
	print "=== MAIN MENU ==="
	print "[E]dit a sound"
	print "[A]ppend sounds"
	print "[I]nformation"	
	print "[G]enerate and exit program"
	input = raw_input("Please enter an option: ")
	if input == 'E':
		soundmenu()
	elif input == 'G':	
		generateFile(fileName, sounds)
	elif input == 'A':
		appendmenu()
	elif input == 'I':
		print "Piece length: " + str(time)
		print "Number of sounds: " + str(len(sounds))
		mainmenu()
	elif input == 'Z':
		powersoftwo()
	else:
		print "Bad input"
		mainmenu()	

def powersoftwo():
	global start, time
	addent = 2
	for i in range(1,10):
		start = time
		time = time + 9	
		print addent
		for j in range(0, addent):
			sounds.append(Sound())
		addent = addent * 2
	for i in range(0, 10):
		start = time
		time = time + 9
		addent = addent / 2
		print addent
		for j in range(0, addent):
			sounds.append(Sound())
	mainmenu()

def appendmenu():
	global start, time
	print "==Append to Piece=="
	input = int(raw_input("How much time to add: "))
	start = time
	time = time + input
	input = int(raw_input("How many sounds to add: "))
	for i in range(0, input):
		sounds.append(Sound())
	mainmenu();

def soundmenu():
	print "==Sound Menu=="
	input = int(raw_input("Select sound 0 through " + str(numSounds - 1) + ": "))
	sound = sounds[input]
	sound.stime = int(raw_input("Start Time: "))
	sound.dur = int(raw_input("Duration: "))
	sound.numPart = int(raw_input("Number of Partials: "))
	sound.partials = []
	for i in range(0, sound.numPart):
		sound.partials.append(Partial())
		sound.partials[i].envPart = int(raw_input("Envelope for Partial " + str(i+1) + ": "))
		sound.partials[i].scalePart = float(raw_input("Scale for Partial " + str(i+1) + ": "))
	sound.freq = float(raw_input("Frequency: "))
	sound.loud = int(raw_input("Loudness: "))
	sound.deviation = float(raw_input("Deviation: "))
	vibratoMenu(sound)
	tremoloMenu(sound)
	glissandoMenu(sound)
	sound.panEnv = int(raw_input("Pan Envelope: "))
	sound.panScale = float(raw_input("Pan Scale: "))
	sound.room = float(raw_input("Room: "))
	mainmenu()

def vibratoMenu(sound):
	input = raw_input("Add vibrato? (Y/N)\n")
	if input == 'Y':
		sound.vibrato = Modifier()
		sound.vibrato.ampEnv = int(raw_input("Amplitude Envelope: "))
		sound.vibrato.ampScale = float(raw_input("Amplitude Scale: "))
		sound.vibrato.noteEnv = int(raw_input("Note Envelope: "))
		sound.vibrato.noteScale = float(raw_input("Note Scale: "))
	else:
		sound.vibrato = None

def tremoloMenu(sound):
	input = raw_input("Add tremolo? (Y/N)\n")
	if input == 'Y':
		sound.tremolo = Modifier()
		sound.tremolo.ampEnv = int(raw_input("Amplitude Envelope: "))
		sound.tremolo.ampScale = float(raw_input("Amplitude Scale: "))
		sound.tremolo.noteEnv = int(raw_input("Note Envelope: "))
		sound.tremolo.noteScale = float(raw_input("Note Scale: "))
	else:
		sound.vibrato = None

def glissandoMenu(sound):
	input = raw_input("Add glissando? (Y/N)\n")
	if input == 'Y':
		sound.vibrato = Modifier()
		sound.vibrato.ampEnv = int(raw_input("Amplitude Envelope: "))
		sound.vibrato.ampScale = float(raw_input("Amplitude Scale: "))
	else:
		sound.vibrato = None

def main():
	global fileName, numSounds, sounds, time, start
	print "Soundmaker Script File Generator"

	fileName = raw_input("Enter the name of the file: ")
	numSounds = int(raw_input("Number of sounds: "))
	start = 0
	time = int(raw_input("Length of piece in seconds: "))
	sounds = []

	for i in range(0, numSounds):
		sounds.append(Sound())

	mainmenu()	
	
 
if __name__ == "__main__":
	main()
