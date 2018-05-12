# Uses python3
import sys
# import itertools
import pdb

def partition3(A):
	# list --> int (1 or 0)
	# list of ints --> 1 if you can build three sub-lists that all total to sum(A)/3
	total = sum( A )
	if total % 3 != 0 :
		return 0
	else :
		target = total // 3
		( subTot , used ) = optimal_weight( target, A )
		if subTot != target :
			return 0
		else :
			for elem in used :
				A.remove( elem )
			( subTot, used) = optimal_weight( target, A )
			if subTot == target :
				return 1

	return 0

def optimal_weight(W, w):
	# ( int, list of ints ) --> int, list
	# ( int1, list of ints ) --> the largest int, B,  that can be constructed 
	# 			using ints from the list, each element used at most once, 
	#			such that B <= int1 ............ AND
	#  a list of elements actually used - so that the caller can use
	# this list to cull the original list :)
    # write your code here
	# you have n+1 rows (n = len( w) ) and W+1 columns (0 to W)
	# first row is 0's - the optimal value using no element, for any W
	n = len( w ) 
	V = []
	used = []
	for i in range( n+1 ) :
		V.append( [0] * (W+1) )

	for i in range( 1 , n+1 ) :
		for wi in range( 1 , W+1 ) :
			V[i][wi] = V[i-1][wi]	# case of the ith item not being used
			if w[i-1] <= wi :
				val = V[i-1][wi-w[i-1] ] + w[i-1]	# a case of weight = value :)
				if V[ i][wi] < val :
					V[ i][wi] = val
	W_sav = W				
	for i in range( n, 1, -1 ) :
		if w[i-1] <= W and V[i-1][W] <= V[i-1][W-w[i-1]] + w[i-1] :		# means w[i] was used
			used.append( w[i-1] )
			W -= w[i-1]
					
	return (V[n][W_sav], used )
	
	
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    
	#pdb.set_trace()
    #print(partition3( sorted(A) ))
    print(partition3( A ))

# from what I can tell, this is a knapsack with repetitions problem

# check that the sum is a multiple of 3 - else, abort immediately..
# then, total/3 is the knapsack capacity, start filling..
# can you fill three knapsacks to full capacity is what it's all 
# about :)

# so, this is a knapsack with repetitions and reconstruction problem.. nice :)

# so, you call once, starter list, see if you fill the bag
# call again - and, if you fill the bag completely a second time, then you
# know you're done..

# okay it's not k with reps according to the prof's definition where
# you have infinitely many of each. Here, you have some items being
# available more than once - duplicates..
# so, it's knapsack without repetitions but with reconstruction :)

# how does the back-tracking work? YOu look at the optimal value and 
# compare the optimal value of the used V[n-1][W-wn] and not-used
# V[n-1][W] + vi(value) cases and if the latter is larger, you know that the nth
# item was not used.. go back that way and you're done :)