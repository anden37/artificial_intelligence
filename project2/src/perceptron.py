#usr/bin/env python
from reader_function import Reader

class Perceptron():

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.w = [0] * 3 #We assume 2 features (as in training set)

	def train(self):
		print "Training..."
		print ""
		miss_rate = 1.0
		while (miss_rate > 0.1):
			idx = 0
			n_misses = 0.0
			for dictionary in self.x:
				n_misses += self.simple_update(dictionary, self.y[idx])
				idx += 1
			miss_rate = n_misses / len(y)

		print "Miss rate", miss_rate, n_misses, len(y)

	def get_params(self):
		return self.w

	def classify(self, x):
		classification_val = self.w[0] + self.w[1]*x[1] + self.w[2]*x[2]
		guessed_y = 0
		if classification_val > 0:
			guessed_y = 1
		return guessed_y

	def simple_update(self, x, y):
		guessed_y = self.classify(x)
		self.w[0] = self.w[0] + (y - guessed_y)
		self.w[1] = self.w[1] + x[1]*(y - guessed_y)
		self.w[2] = self.w[2] + x[2]*(y - guessed_y)

		if (y-guessed_y) == 0:
			return 0
		return 1

	def simple_test(self):
		self.test(self.y, self.x)

	def test(self, y, dicts):
		idx = 0
		classification_list = []
		for dictionary in dicts:
			classification_list.append(self.classify(dictionary))
		
		print "Classifications: "
		print classification_list,
		print "Actual classes: "
		print y

if __name__ == "__main__":
	r = Reader()
	r.libsvm_read_file("../test/test1.txt")
	y, x = r.get_randomized_data()
	p = Perceptron(x, y)
	p.train()
	print "params: "
	print p.get_params()
	p.simple_test()




