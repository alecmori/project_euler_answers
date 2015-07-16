#This was a fun little problem; the tricky part is that d(a) > MAX, and you then 
#have to check that number (d(a)) as well (I don't think it changes this problem though)
MAX = 10000

#Note we are not counting num as a factor of num in this problem
def findFactors(num):
	factors = set([1])
	i = 2
	while i * i <= num:
		if num % i == 0:
			factors.add(i)
			factors.add(num / i)
		i += 1
	return list(factors)

def checkAmicable(factorSum, num):
	return num < MAX and factorSum[num] != num and factorSum[factorSum[num]] == num

if __name__ == "__main__":
	factorSum = dict()
	for num in range(1, MAX): 
		factorSum[num] = sum(findFactors(num))
	newFactors = []
	for num in factorSum:
		if factorSum[num] not in factorSum:
			#We need to add a new key value pair, but cannot add it during iteration
			newFactors.append((factorSum[num], findFactors(factorSum[num])))
	for key, value in newFactors:
		factorSum[key] = value

	total = 0
	for num in factorSum:
		if checkAmicable(factorSum, num):	
			total += num
	print total