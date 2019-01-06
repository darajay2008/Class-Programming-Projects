# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util, gridworld, math

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
		"""self.mdp = mdp
		self.discount = discount
		self.iterations = iterations
		self.values = util.Counter() # A Counter is a dict with default 0
		for i in range(self.iterations):
			temp1 = self.values
			for s in self.mdp.getStates():
				val = self.getValue(s)
				opt_action, opt_action_value = self.getAction(s)
				if opt_action_value > val:
					val = opt_action_value
				temp1[s] = val
			self.values = temp1"""
		self.mdp = mdp
		self.discount = discount
		self.iterations = iterations
		self.values = util.Counter() # A Counter is a dict with default 0
		self.qValues = util.Counter()
		
		for k in range(self.iterations):
			for state in self.mdp.getStates():
				for action in self.mdp.getPossibleActions(state):
					self.qValues[(state, action)] = self.getQValue(state, action)
			for state in self.mdp.getStates():
				if self.mdp.isTerminal(state):
					continue
				self.values[state] = max([self.qValues[(state, action)] for action in self.mdp.getPossibleActions(state)])
		
		
    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
		P = self.mdp.getTransitionStatesAndProbs(state, action)
		exp_value = 0.0
		for entry in P:
			next_state = entry[0]
			prob = entry[1]
			reward = self.mdp.getReward(state, action, next_state)
			exp_value += reward + self.discount * self.values[next_state]* prob
		return exp_value
        #util.raiseNotDefined()

    def computeActionFromValues(self, state):
		#max_action_value = 0.0
		self.qValues1 = util.Counter()
		if self.mdp.isTerminal(state):
			return ('exit')
		else:
			#optimal_action = 'exit'
			for a in self.mdp.getPossibleActions(state):
				self.qValues1[(state, a)] = self.getQValue(state, a)
			optimal_action = self.qValues1.argMax()
			return optimal_action[1]
        #util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
