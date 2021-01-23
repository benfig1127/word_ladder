#!/bin/python3

from pythonds.basic import Stack
from pythonds.basic import Deque


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
	
	#read in dictionary file 
	word_list=[]
	f = open("words5.dict", "r")
	for line in f:
		word_list.append(line.strip())
	
	s=Stack()
	s.push(start_word)

	d=Deque()
	d.addRear(s)
	
	#while not d.isEmpty():
		#print(d.size())
		#print(d.removeFront())
	
	while not d.isEmpty():
		current_stack=d.removeFront()
		
		for dict_word in word_list:
			top_of_stack=current_stack.peek()
			
			if _adjacent(top_of_stack,dict_word):
				
				if dict_word==end_word:
					current_stack.push(word)
					
					return current_stack
				
				copy_of_stack=current_stack
				copy_of_stack.push(dict_word)
				d.addrear(copy_of_stack)
				word_list=word_list.remove(dict_word)
				
	return None
		
	#q=collections.deque()
	#q.append(1)
	#q.append(2)
	#return q.popleft()

def verify_word_ladder(ladder):
	
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
	
	different=False
	
	for index, char in enumerate(word1):
		if char!=word2[index]:
			if different:
				return False
			else:
				different=True
	return True
		
	
	
#print(word_ladder('stone','money'))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
