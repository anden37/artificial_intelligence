#!usr/bin/env python
import game

class AI():

	def __init__(self, game, depth, ai_piece):
		self.depth = depth
		self.alpha = -float("inf")
		self.beta = float("inf")
		self.ai_piece = ai_piece
		self.game = game
		
	def get_next_state(self):
		self.root = Node(self.game, self.game.get_init_state(), self.ai_piece, self.ai_piece)
		alphabeta()
		max_v = -float("inf")
		max_node = None
		for node in self.root.get_children():
			if max_v < node.get_v():
				max_v = node.get_v()
				max_node = node
			ctr += 1
		return max_node.get_state()

	def make_move(self):
		alphabeta()

	def alphabeta(self, node, depth, alpha, beta, maximizingPlayer):
		if (depth == 0 or len(node.child_list) == 0):
			return node.value
		if maximizingPlayer:
			v = -float("inf")
			for child in node.child_list:
				v = max(v, alphabeta(child, depth-1, alpha, beta, False))
				alpha = max(alpha, v)
				if beta <= alpha:
					break
				return v
		else:
			v = float("inf")
			for child in node.child_list:
				v = min(v, alphabeta(child, depth-1, alpha, beta, True))
				beta = min(beta, v)
				if beta <= alpha:
					break
				return v

class Node():

	def __init__(self, game, state, ai_piece, current_piece):
		self.game = game
		self.child_list = []
		self.value = None
		self.state = state
		self.ai_piece = ai_piece
		self.current_piece = current_piece
		self.heuristic_point = self.game.get_score(state, ai_piece)
		self.v = self.heuristic_point

	def set_v(self, v):
		self.v = v

	def get_v(self):
		return v

	def add_children(self):
		moves = self.game.get_possible_moves(self.state, self.current_piece)
		for move in moves:
			#piece = game.get_state_piece(self.state)
			state, next_piece = self.game.play_from_state(self.state, self.current_piece, move[0], move[1])
			n = Node(state, next_piece)
			self.child_list.append(n)

	def get_children(self):
		return self.child_list

	def get_state(self):
		return self.state
	







