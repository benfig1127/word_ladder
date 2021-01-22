#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
	'''
	Returns a list satisfying the following properties:

	1. the first element is `start_word`
	2. the last element is `end_word`
	3. elements at index i and i+1 are `_adjacent`
	4. all elements are entries in the `dictionary_file` file

	For example, running the command
	```
	word_ladder('stone','money')
	```
	may give the output
	```
	['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
	```
	but the possible outputs are not unique,
	so you may also get the output
	```
	['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
	```
	(We cannot use doctests here because the outputs are not unique.)

	Whenever it is impossible to generate a word ladder between the two words,
	the function returns `None`.
	'''


def verify_word_ladder(ladder):
	'''
	Returns True if each entry of the input list is adjacent to its neighbors;
	otherwise returns False.
	'''
	#check to make sure our ladder is non empty
	if not ladder:
		return False
	
	index=0
	queue=[]
	stop_point=len(ladder)
	output=True
	
	while index<stop_point:
		#if the queue is empty add item to the queue and continue
		if not queue:
			queue.append(ladder[index])
			index+=1 
			continue
		#compare the current word and the word in the queue
		is_adjacent=_adjacent(ladder[index],queue[0])
		if not is_adjacent:
			output=False 
			break
		#if the words are adjacent, clear the queue and add the current word to it and continue
		queue=[]
		queue.append(ladder[index])
		index+=1
		
	return output 




def _adjacent(word1, word2):
	'''
	Returns True if the input words differ by only a single character;
	returns False otherwise.

	>>> _adjacent('phone','phony')
	True
	>>> _adjacent('stone','money')
	False
	'''
	#previous_char_was_different=False
	#current_char_is_different=False
	different=False
	
	for index, char in enumerate(word1):
		if char!=word2[index]:
			if different:
				return False
			else:
				different=True
	return True
		
			
	
	
	
#print(_adjacent('phone','phony'))
#print(_adjacent('stone','money'))
