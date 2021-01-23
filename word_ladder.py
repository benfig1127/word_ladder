#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):

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
		
		
		for dict_word in word_list:
			
			if _adjacent(current_stack[-1],dict_word):
				
				if dict_word==end_word:
					current_stack.append(dict_word)
					
					#removes duplicate entries
					#cleaned_output=[]
					#for i in current_stack:
						#if i not in cleaned_output:
							#cleaned_output.append(i)
					
					return current_stack
				
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
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
