# Uses python3
import sys

def get_majority_element(a, left, right):
	#write your code here
	# ( [list of nums] , int, int ) --> num
	# ( [sorted list of nums] , pointer to first element in range to be processed,
	# 			1 + index of last element in range to be processed ) --> value of majority elem or -1
	if left == right:	# degenerate case. Even a single element list would be N, N+1 (0,1) for Eg
		return -1
	if left + 1 == right:	# single element case -- we never expect to see this..
		return a[left]
	if left + 2 == right :	# two elements - return -1 if not equal, else, return the element
		if a[left] == a[left+1] : 
			return a[left]
		else :
			return -1
	if left + 3 == right :	# three elements - sorted list => if #1==#2 or #2==#3, you have a majority elem
		if a[left] == a[left+1] :
			return a[left]
		elif a[left+1] == a[left+2] :
			return a[left+1]
		else :
			return -1
	# now, combine the recursive calls
	# you have two calls. If the left call returned a non -1 (i.e.), a majority elem  was found
	# then, count the number of occurrences of this majority element in entire range
	# same for the right list - if it says yes, then...
	# now, do you have a winner?
	l_result = get_majority_element( a, left, left + int( 0.5*(left+right) ) )
	num_elems = right - left
	if -1 != l_result :
		if a[left:right].count( l_result ) > int( num_elems / 2 ) :
			return l_result
	r_result = get_majority_element( a, left + int( 0.5*(left+right) ) , right )
	if -1 != r_result :
		if a[left:right].count( r_result ) > int( num_elems / 2 ) :
			return r_result

	return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element( sorted(a), 0, n) != -1:
        print(1)
    else:
        print(0)

# given a list of numbers, return the majority element (has more occurrences than
# half the list size) else, return -1

# how to solve - for a 2-element list, both elements have to be equal for a majority
# element to exist

# for a 3-element list, you have to have at least two of the elements equal

# recursion : there is one list always - whose reference gets passed in each recursive call..