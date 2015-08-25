
# Author: Greg Scott
# Date: 1/28/2015
#
# Title: Guess Game

# class to establish the nodes in my tree
class QuestionTree:
	
	def __init__(self, data, ifAnswer):
		self.data = data
		self.answerR = None
		self.answerL = None
		self.ifAns = True
		
	def setData(self, data):
		self.data = data
				
	def setRight(self, answerRdata):
		self.answerR = answerRdata
		
	def setLeft(self, answerLdata):
		self.answerL = answerLdata
		
	def getRight(self):
		return self.answerR
		
	def getLeft(self):
		return self.answerL
	
	def getData(self):
		return self.data
		
	def setAnswer(self, value):
		self.ifAns = value
		
	def ifAnswer(self):
		return self.ifAns
		
# method to handle questions and movement through the tree based upon answers
def question(currNode):
	print(currNode.getData())
	answer = str(raw_input('')).lower()
	if answer == 'yes':
		nextNode = currNode.getRight()
	elif answer == 'no':
		nextNode = currNode.getLeft()
	else:
		print('Incorrect response. Please answer Yes or No.')
		print('I\'ll ask again.')
		nextNode = question(currNode)
	return nextNode

# The initial question and the answers to it
currNode = QuestionTree('Does it have legs?', False)
rightAns = QuestionTree('Dog', True)
leftAns = QuestionTree('Snake', True)
currNode.setRight(rightAns)
currNode.setLeft(leftAns)
rootNode = currNode
print('Think of an animal. I will guess it by asking yes/no questions.')

#while loop that moves through game until user specifies to end game
while True:
	prevNode = currNode
	currNode = question(currNode)
	if currNode.ifAnswer() == True:
		response = str(raw_input('Is it a ' + currNode.getData() + '? ')).lower()
		if response == 'yes':
			print('Excellent. I win.')
		elif response == 'no':
			nextResp = str(raw_input('Ok, what is it? '))
			print('Please type a question to distinguish the animal from a ' + currNode.getData() + ':')
			nextQues = str(raw_input())
			newRight = QuestionTree(nextResp, True)
			newLeft = QuestionTree(currNode.getData(), True)
			currNode.setData(nextQues)
			currNode.setAnswer(False)
			currNode.setRight(newRight)
			currNode.setLeft(newLeft)
		else:
			print('Incorrect response. Please answer Yes or No.')
			
		nextResp = str(raw_input('Continue the game? '))
		if nextResp == 'Yes':
			currNode = rootNode
			print('Think of an animal. I will guess it by asking yes/no questions.')
		else:
			break
		
		
		
		
