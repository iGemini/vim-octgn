def FlipCoin(group, x = 0, y = 0):
	n = rnd(1, 2)
	if n == 1:
		notify("{} flips a coin and gets HEADS.".format(me))
	else:
		notify("{} flips a coin and gets TAILS".format(me))

def PlayFaceUp(card, x = 0, y = 0):
	mute()
	notify("{} places {} Face-Down.".format(me, card))
	if me._id == 1:
		card.moveToTable(0, 0)
	else:
		card.moveToTable(0, -88)

def PlayFaceDown(card, x = 0, y = 0):
	mute()
	notify("{} places a card Face-Down.".format(me))
	if me._id == 1:
		card.moveToTable(0, 0, True)
	else:
		card.moveToTable(0, -88, True)
	card.peek()

def FlipCard(card, x = 0, y = 0):
	mute()
	if card.isFaceUp == True:
		notify("{} flips {} face down.".format(me, card))
		card.isFaceUp = False
		card.peek()
	elif card.isFaceUp == False:
		notify("{} flips {} face up.".format(me, card))
		card.isFaceUp = True

def Draw(group, x = 0, y = 0):
	mute()
	if len(group) == 0:
		return
	card = group[0]
	notify("{} draws a card from {}.".format(me, group.name))
	card.moveTo(me.hand)

def Shuffle(group, x = 0, y = 0):
	mute()
	notify("{} shuffles {}.".format(me, group.name))
	group.shuffle()

def ShuffleIntoDeck(card, group):
	mute()
	notify("{} shuffles {} into their {}.".format(me, card, group.name))
	card.moveTo(group)
	group.shuffle()

def ShuffleIntoServantDeck(card, x = 0, y = 0):
	mute()
	targetPile = me.piles['Servant Deck']
	ShuffleIntoDeck(card, targetPile)

def ShuffleIntoSkillDeck(card, x = 0, y = 0):
	mute()
	targetPile = me.piles['Skill Deck']
	ShuffleIntoDeck(card, targetPile)

def	ShuffleIntoEnvironmentDeck(card, x = 0, y = 0):
	mute()
	targetPile = me.piles['Environment Deck']
	ShuffleIntoDeck(card, targetPile)

def PlaceInHand(card, x = 0, y = 0):
	mute()
	notify("{} places {} into their Hand.".format(me, card))
	card.moveTo(me.hand)

def PlaceOnTopOfDeck(card, group):
	mute()
	notify("{} places {} on top of their {}.".format(me, card, group.name))
	card.moveTo(group)

def	PlaceOnTopOfServantDeck(card, x = 0, y = 0):
	mute()
	targetPile = me.piles['Servant Deck']
	PlaceOnTopOfDeck(card, targetPile)

def	PlaceOnTopOfSkillDeck(card, x = 0, y = 0):
	mute()
	targetPile = me.piles['Skill Deck']
	PlaceOnTopOfDeck(card, targetPile)

def	PlaceOnTopOfEnvironmentDeck(card, x = 0, y = 0):
	mute()
	targetPile = me.piles['Environment Deck']
	PlaceOnTopOfDeck(card, targetPile)

def	MoveToPositionDeck(card, group):
	mute()
	position = askInteger("Move to which postion in {}?".format(group.name), 1)
	notify("{} places {} in postion {} of their {}.".format(me, card, position, group.name))
	card.moveTo(group, position - 1)

def MoveToPositionServantDeck(card, x = 0, y = 0):
	mute()
	targetPile = me.piles['Servant Deck']
	MoveToPositionDeck(card, targetPile)

def	MoveToPositionSkillDeck(card, x = 0, y = 0):
	mute()
	targetPile = me.piles['Skill Deck']
	MoveToPositionDeck(card, targetPile)

def	MoveToPositionEnvironmentDeck(card, x = 0, y = 0):
	mute()
	targetPile = me.piles['Environment Deck']
	MoveToPositionDeck(card, targetPile)

def MoveToVoid(card, x = 0, y = 0):
	mute()
	notify("{} moves {} to {}'s Void.".format(me, card, card.owner))
	card.moveTo(card.owner.piles['Void'])

def MoveXToVoid(group, x = 0, y = 0):
	(mute)
	number = askInteger("Move how many cards to Void?", 1)
	if number > len(group):
		number = len(group)
	cards = group.top(number)
	for c in cards:
		c.moveTo(me.piles['Void'])

def PeekX(group, x = 0, y = 0):
	mute()
	number = askInteger("How many cards to look at?", 1)
	notify("{} looks at the top {} cards of their {}.".format(me, number, group.name))
	group.lookAt(number)

def PeekXOpponent(group, x = 0, y = 0):
	mute()
	number = askInteger("How many cards to look at?", 1)
	if number == 0:
		return
	notify("{} looks at {} random cards of {} their Hand.".format(me, number, players[1]))
	remoteCall(players[1], "SendXPeek", number)
	
def SendXPeek(number):
	mute()
	cards = []
	if number > len(me.hand):
		number = len(me.hand)
	places = []
	for x in range(0, len(me.hand)):
		places.append(x)
	for i in range(0, number):
		place = rnd(0, len(places) -1)
		cards.append(me.hand[places[place]])
		places.remove(places[place])
	remoteCall(players[1], "ReceiveXPeek", [cards])

def ReceiveXPeek(cards):
	mute()
	dlg = cardDlg(cards)
	cardlist = dlg.show()

def ViewDeck(group, x = 0, y = 0):
	mute()
	notify("{} looks at their {}.".format(me, group.name))
	group.lookAt(len(group))

def RevealCard(card, x = 0, y = 0):
	mute()
	notify("{} reveals {} from their {}.".format(me, card, card.group.name))
	if me._id == 1:
		card.moveToTable(0, 0)
	else:
		card.moveToTable(0, -88)

def RevealTopCard(group, x = 0, y = 0):
	mute()
	notify("{} reveals the top card from their {}.".format(me, group.name))
	card = group[0]
	if me._id == 1:
		card.moveToTable(0, 0)
	else:
		card.moveToTable(0, -88)

def RevealX(group, x = 0, y = 0):
	mute()
	number = askInteger("Reveal how many cards?", 1)
	if number > len(group):
		number = len(group)
	notify("{} reveals {} cards from their {}.".format(me, number, group.name))
	for i in range (0, number):
		place = rnd(0, len(group) - 1)
		notify("{} reveals {}.".format(me, group[place]))
		card = group[place]
		if me._id == 1:
			card.moveToTable(0, 0)
		else:
			card.moveToTable(0, -88)

def GiveControl(card, x = 0, y = 0):
	mute()
	notify("{} gives control of {} to {}.".format(me, card, players[1]))
	if card.controller._id == 1:
		card.moveToTable(0, -88)
	else:
		card.moveToTable(0, 0)
	card.controller = players[1]

#---------------------------------------------------------------------------
# Marker Manipulations
#---------------------------------------------------------------------------

counters = {
	'Damage': ('Damage', '3A19FC59-9119-4DEC-8C90-7FD2A1229380'),
	'Rank': ('Rank', 'F5BB27F0-2A05-438D-BDED-09533D375AA1')
}

def AddDamageMarker(card, x = 0, y = 0):
	mute()
	notify("{} adds a damage counter to {}.".format(me, card))
	card.markers[counters['Damage']] += 1

def RemoveDamageMarker(card, x = 0, y = 0):
	mute()
	if counters['Damage'] in card.markers:
		notify("{} removes a damage counter from {}.".format(me, card))
		card.markers[(counters['Damage'])] -= 1

def AddRankMarker(card, x = 0, y = 0):
	mute()
	notify("{} adds a rank counter to {}.".format(me, card))
	card.markers[counters['Rank']] += 1

def RemoveRankMarker(card, x = 0, y = 0):
	mute()
	if counters['Rank'] in card.markers:
		notify("{} removes a rank counter from {}.".format(me, card))
		card.markers[(counters['Rank'])] -= 1

def AddMarker(card, x = 0, y = 0):
	mute()
	marker, quantity = askMarker()
	if quantity == 0:
		return
	card.markers[marker] += quantity
 	notify("{} adds {} {} counters to {}.".format(me, quantity, marker[0], card))