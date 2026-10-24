def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	# Row
	if mode == "row":
		for row in matrix:
			means.append(sum(row) / len(row))
	else:
		for j in range(len(matrix[0])):
			v_sum = 0
			for i in range(len(matrix)):
				v_sum += matrix[i][j]
			means.append(v_sum / len(matrix))
	return means