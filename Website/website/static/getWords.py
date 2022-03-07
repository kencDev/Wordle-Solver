import csv

class Solve:

	def __init__(self):			
	#need to write a test asserts doc to make sure read csv is same as the made dict in wordGen.
		self.wordDict = {}
		path = 'website\static'
		with open(path + '\dictionary.csv', mode = 'r') as infile:
			reader = csv.reader(infile)
			count = 0
			for row in reader:
				if row: 
					self.wordDict[chr(count + 97)] = row
					count = count + 1
		
#works except for problem where double character guess e.g. "litty" will produce one green and one grey.
#this removes all t words. 
#another problem may be that if there are two 't's one green one yellow. it will not remove all one 't' words, but this is not as serious as first error.
#how to solve this error. #keep a dictionary of the green words?
#if grey word encountered and it is in the dictionary. then dont remove the word. 
#if yellow word encountered and it is already in dictionary, there are two 't's in the answer. remove all non two 't' words.
#can i just do a set? maybe, but if theres 3 of the same character, what happens.
	def wordSolver(self, green, yellow,grey):
		greenDict = {}
		self.setA = set()
		#accounts for greens
		for i in range(len(green)):
			if green != "" and green[i] not in greenDict:
				greenDict[green[i]] = set()
				greenDict[green[i]].add(i)
			else :
				greenDict[green[i]].add(i)


			if (green[i]):
				if len(self.setA) ==0: 
					self.setA = self.setA.union( (word for word in self.wordDict[green[i]] if word[i] == green[i]))
				else :

					self.setA = self.setA.intersection( (word for word in self.wordDict[green[i]] if word[i] == green[i]))
			#print(setA)
			#accounts for yellows
		for i in range(len(yellow)):
			if (yellow[i]):
				if len(self.setA) ==0: 
					self.setA = self.setA.union( (word for word in self.wordDict[yellow[i]] if yellow[i] in word))
				else :
					self.setA = self.setA.intersection( (word for word in self.wordDict[yellow[i]] if (yellow[i] in word) and yellow[i] != word[i]))
					#if this yellow character is in the dictionary. allow only word with char > len(greenDict[dict['character']]) 
					if yellow[i] in greenDict:
						self.setA = self.setA.intersection( (word for word in self.wordDict[yellow[i]] if  word.count(yellow[i]) > len(greenDict[yellow[i]])   ) )

#print(setA)
		for i in range(len(grey)):
			if (grey[i]):
				if len(self.setA) ==0: 
					break
				else : 
					
					#avoids removal of all grey words that have previously appeared as a green word.
					if grey[i] not in greenDict:
						self.setA = self.setA.intersection(word for word in self.setA if not grey[i] in word)
		


	def printSolution(self):
		word = ""
		for key in self.setA:
			word += key + ", "
		return word[:-2]
