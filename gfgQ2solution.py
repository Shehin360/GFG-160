class Solution:
	def pushZerosToEnd(self, arr):
		n = len(arr)
		temp = [0] * n
		j = 0
		for i in range(n):
			if arr[i] != 0:
				temp[j] = arr[i]
				j += 1

		while j < n:
			temp[j] = 0
			j += 1

		for i in range(n):
			arr[i] = temp[i]