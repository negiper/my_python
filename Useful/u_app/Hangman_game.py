#coding=utf-8
#刽子手游戏字符串的实现
# Hangman game
#2016年 02月 26日 星期五 22:59:00 CST

import random
import string
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

HANGMANPICS = ['''
  +----+
  |    |
       |
       |
       |
       |
==========''','''
  +----+
  |    |
  0    |
       |
       |
       |
==========''','''
  +----+
  |    |
  0    |
  |    |
       |
       |
==========''','''
  +----+
  |    |
  0    |
 /|    |
       |
       |
==========''','''
  +----+
  |    |
  0    |
 /|\   |
       |
       |
==========''','''
  +----+
  |    |
  0    |
 /|\   |
 o     |
       |
==========''','''
  +----+
  |    |
  0    |
 /|\   |
 o o   |
       |
==========''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra \
cougar coyote crow deer dog donkey duck eagle ferret fox frog \
goose hawk lion lizard llama mole monkey moose mouse mule newt \
otter owl panda tiger toad trout turkey turtle weasel whale wolf \
wombat zebra'.split()

def getRandomWord(wordList):
#This function returns a random string from the passed list of words.
	wordIndex = random.randint(0,len(wordList)-1)
	return wordList[wordIndex]

def display(HANGMANPICS,missedLetters,correctLetters,secretWord):
	print(HANGMANPICS[len(missedLetters)])
	print()
	
	print('Missed letters:', end=' ')
	for ch in missedLetters:
		print(ch,end=' ')
	print()
	
	showString = '_'*len(secretWord)
	for i in range(len(secretWord)):  #replace showString with correctly guessed letter
		if secretWord[i] in correctLetters:
			showString = showString[:i] + secretWord[i] + showString[i+1:]
	
	for ch in showString:
		print(ch, end=' ')
	print()
	
def getGuess(alreadyGuessed):
#Returns the letter the player entered. This function make sure the player entered a single letter, and not something else.
	while True:
		print('Guess a letter: ', end=' ')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print('Please enter a single letter!')
		elif guess in alreadyGuessed:
			print('You have already guessed that letter. Choose again.')
		elif guess not in alpha:
			print('Please enter a letter.')
		else:
			return guess

def playAgain():
#This function returns True if the player wants to play again, otherwise it returns False.
	print('Do you want to play again?(yes or not):', end=' ')
	return input().lower().startwith('y')

#Main program
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
	display(HANGMANPICS,missedLetters,correctLetters,secretWord)
	
	#Let the player type in letter.
	guess = getGuess(missedLetters + correctLetters)
	
	if guess in secretWord:
		correctLetters = correctLetters + guess
		
		#Check the player has won.
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print('Yes! The secret word is: ',secretWord,'You have won!')
			gameIsDone = True
	else:
		missedLetters = missedLetters + guess
		
		#Check the player has guessed too many times and lost.
		if len(missedLetters) == len(HANGMANPICS) -1:
			display(HANGMANPICS,missedLetters,correctLetters,secretWord)
			print('You have run out of guesses!\nAfter',len(missedLetters),'missed guesses and ',len(correctLetters),'correct guesses, the word was ',secretWord)
			gameIsDone = True
	
	#Ask the player if they want to play again
	if gameIsDone:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameIsDone = False
			secretWord = getRandomWord(words)
		else:
			break
 
