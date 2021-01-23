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
	
	#read in dictionary file 
	word_list=[]
	f = open("words5.dict", "r")
	for line in f:
		word_list.append(line.strip())
	
	
	if start_word==end_word:
		return [start_word]
	
	
	stack=[]
	stack.append(start_word)
	
	queue=[]
	queue.append(stack)
	
	while queue:
		current_stack=queue.pop(0)
		
		#print('top of stack:',top_of_stack)
		#print('bottom of stack:', current_stack[0])
			
		
		for dict_word in word_list:
			
			if _adjacent(current_stack[-1],dict_word):
				
				if dict_word==end_word:
					current_stack.append(dict_word)
					
					#removes duplicate entries
					cleaned_output=[]
					for i in current:
						if i not in cleaned_output:
							cleaned_output.append(i)
					
					return cleaned_output
				
				copy_of_current_stack=current_stack.copy()
				copy_of_current_stack.append(dict_word)
				queue.append(copy_of_current_stack)
				word_list.remove(dict_word)
				
		
	return None
		
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
		
	
	
print(word_ladder('stone','stone'))

print(word_ladder('aloof','aloof'))
	

print(word_ladder('babes','child'))	
	
	
print(word_ladder('child','babes'))	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
