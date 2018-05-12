# Uses python3
import sys
import pdb

def optimal_weight(W, w):
	# ( int, list of ints ) --> int
	# ( int1, list of ints ) --> the largest int, B,  that can be constructed 
	# 			using ints from the list, each element used at most once, 
	#			such that B <= int1
    # write your code here
	# you have n+1 rows (n = len( w) ) and W+1 columns (0 to W)
	# first row is 0's - the optimal value using no element, for any W
	n = len( w ) 
	V = []
	for i in range( n+1 ) :
		V.append( [0] * (W+1) )

	for i in range( 1 , n+1 ) :
		for wi in range( 1 , W+1 ) :
			V[i][wi] = V[i-1][wi]	# case of the ith item not being used
			if w[i-1] <= wi :
				val = V[i-1][wi-w[i-1] ] + w[i-1]	# a case of weight = value :)
				if V[ i][wi] < val :
					V[ i][wi] = val
					
	
	return V[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    # pdb.set_trace()
    print(optimal_weight(W, w))
