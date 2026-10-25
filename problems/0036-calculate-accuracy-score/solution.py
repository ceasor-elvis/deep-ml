import numpy as np

def accuracy_score(y_true, y_pred):
	right = 0

	for t, p in zip(y_true, y_pred):
		if t == p:
			right+=1
	return (right / len(y_true))