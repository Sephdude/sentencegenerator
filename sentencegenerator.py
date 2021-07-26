run = True
#list of not funny sentences
notfunny = []
#list of words counted as funny
funnynouns = []
funnynounsusedagain = []
funnyverbs = []
funnyverbsusedagain = []
#list of words that counted as even more funny
funnynouns1 = []
funnyverbs1 = []
#the chances of the words marked as more funny are decided by how many words have been marked as funny so that the words will get progressively more funny
evenfunnieryesornochances = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# modules
import random
while run == True:
	if funnynouns != []:
		if nounbeforesuffix in funnynouns:
			funnynouns1.append(nounbeforesuffix)
		if verbbeforesuffix in funnyverbs:
			funnyverbs1.append(verbbeforesuffix)
	#words
	verb = "accept ache acknowledge act add admire admit admonish adopt advise affirm afford agree alert allege allow allude amuse analyze announce annoy answer apologize appeal appear applaud appreciate approve argue arrange arrest arrive articulate ask assert assure attach attack attempt attend attract auction avoid avow awake"
	noun = open('nouns.txt', 'r')
	noun = noun.read()
	adverb = "gladly gently quietly safely truthfully warmly wildly carefully wisely hard fast straight well angrily boldly daringly"
	preposition = "aboard about above across after against along amid among anti around as at before behind below beneath beside besides between beyond but by concerning considering despite down during except excepting excluding following for from in inside into like minus near of off on onto opposite outside over past per plus regarding round save since than through to toward towards under underneath unlike until up upon versus via with within without"
	#decides if the sentence will be funny or not
	funnyyesorno = [0, 1]
	funnyyesorno = random.choice(funnyyesorno)
	print(evenfunnieryesornochances)
	#decides if sentence will use an extra funny word
	#definining extras
	preposition1 = preposition
	directobject = noun
	directobject1 = noun
	directobject2 = noun
	#turn string into list
	verb = verb.split()
	noun = noun.split()
	adverb = adverb.split()
	preposition = preposition.split()
	preposition1 = preposition1.split()
	directobject = directobject.split()
	directobject1 = directobject1.split()
	directobject2 = directobject2.split()
	#randomly pick a word
	verb = random.choice(verb)
	noun = random.choice(noun)
	nounbeforesuffix = noun
	verbbeforesuffix = verb
	adverb = random.choice(adverb)
	preposition = random.choice(preposition)
	preposition1 = random.choice(preposition1)
	directobject = random.choice(directobject)
	directobject1 = random.choice(directobject1)
	directobject2 = random.choice(directobject2)
	#decides if the sentence will use funny words or not
	if funnyyesorno == 1 and funnynouns != []:
		noun = random.choice(funnynouns)
		verb = random.choice(funnyverbs)
		#adds more chances to get an even funnier word
		evenfunnieryesornochances.append(1)

	#decides if there might be extra funny words
	evenfunnieryesornodecided = random.choice(evenfunnieryesornochances)
	#decides if it will use even funnier words
	if funnyyesorno == 1 and funnynouns1 != [] and evenfunnieryesornodecided == 1:
		noun = random.choice(funnynouns1)
		verb = random.choice(funnyverbs1)
	#suffix for noun
	nounsuffix = [['s', 'es'], '']
	nounsuffix = random.choice(nounsuffix)
	#noun grammar
	if nounsuffix != '':
		if noun[-1] != 's' and nounsuffix == ['s', 'es',]:
			nounsuffix = 's'
	elif noun[-1] == 'y' and nounsuffix != '':
			noun = noun[:-1]
			nounsuffix = 'ies'
	elif noun[-1] == 's' and nounsuffix != '':
		nounsuffix =''
	if nounsuffix == ['s', 'es']:
		nounsuffix = random.choice(nounsuffix)
#put special noun grammar cases here
		if noun[-1] == 's':
			nounsuffix = 'es'
		elif noun[-1] == 'o':
			nounsuffix = 'es'
		elif noun[-1] == 'h':
			nounsuffix = 'es'
		elif noun[-1] == 'y':
			noun == noun.replace('y','i') + 'es'
	verbsuffix = [['s', 'es'], '',]
	if nounsuffix == '':
		verbsuffix.remove('')
		verbsuffix = random.choice(verbsuffix)
		if verbsuffix == ['s', 'es']:
			verbsuffix = 's'
	elif nounsuffix != '':
		verbsuffix = ''
	#chooses what extra words will be in the sentence
	adverbyesorno = [0, 1]
	prepositionyesorno = [0, 1]
	prepositionyesorno2 = [0, 1]
	directobjectyesorno = [0, 1]
	directobjectyesorno2 = [0, 1]
	directobject1yesorno = [0, 1]
	adverbyesorno = random.choice(adverbyesorno)
	prepositionyesorno = random.choice(prepositionyesorno)
	prepositionyesorno2 = random.choice(prepositionyesorno2)
	directobjectyesorno2 = random.choice(directobjectyesorno2)
	directobjectyesorno = random.choice(directobjectyesorno)
	directobject1yesorno = random.choice(directobject1yesorno)
	#add suffixes
	directobject2 = directobject2 + nounsuffix
	directobject1 = directobject1 + nounsuffix
	directobject = directobject + nounsuffix
	noun = noun + nounsuffix
	verb = verb + verbsuffix
	sentence = noun + ' ' + verb
	if adverbyesorno == 1:
		sentence = sentence + ' ' + adverb
	if directobject1yesorno == 1:
		sentence = sentence + ' ' + directobject1
	if prepositionyesorno == 1 and directobject1yesorno == 1:
		sentence = sentence + ' ' + preposition + ' ' + directobject
	elif prepositionyesorno == 1 and directobject1yesorno == 1 and prepositionyesorno2 == 1:
		sentence = sentence + ' ' + preposition + ' ' + directobject + ' ' + preposition1 + ' ' + directobject2
	print(sentence)
	#start machine learning part
	#tell if the sentence was funny or not
	funnyornot = input('Was this sentence funny? y or n\n')
	if funnyornot == 'n':
		notfunny.append(sentence)
	elif funnyornot == 'y':
		# adds words that have been said are funny more than once to the even funnier word list
		funnynouns.append(nounbeforesuffix)
		funnyverbs.append(verbbeforesuffix)
	print(funnynouns)
	print(funnyverbs)
	print(funnynouns1)
	#determines if the sentence is funny or not and it wll decide if it will display it to you
	if len(sentence) != len(set(notfunny)):
		print(sentence)
		stop = input('Do you want to keep going? y or n\n')
		if stop == 'n':
			run = False