# Uses python3
import sys
import pdb

def fast_count_segments(starts, ends, points):
	# ( list of ints length n, list of ints length n, list of ints length p) 
	#				-- > list of ints length p, each entry corresponding to 
	# 						the number of segments points[i] is contained in
	p = len( points )
	cnt = [0] * p
	final_cnt = [0] * p
	n = len( starts )
	#write your code here
	lcl_p = points[:]		# make a copy to sort
	randomized_quick_sort( lcl_p, 0, p - 1 )
	randomized_quick_sort( starts, 0, n-1 )
	randomized_quick_sort( ends, 0, n-1 )
	
	traverse( starts, 0, n-1, ends, 0, n-1, lcl_p, 0, p-1, 0, cnt )
	for i, point in enumerate( points ) :
		final_cnt[i] = cnt[binary_search( lcl_p, 0, p, point )]
	
	return final_cnt

def traverse( starts, l_s, r_s, ends, l_e, r_e, points , l_p, r_p, counter, count_list) :
	# sorted list of ints, index of first elem, index of last elem,
	#		sorted list of ints , index of first elem, index of last elem,
	#		sorted list of ints , index of first elem, index of last elem ,
	#		int, list (uses the reference to insert ints ) --> nothing
	# the side effect is that the count_list is updated
	# it looks at starts[l_s], ends[l_e], points[l_p] and, if the smallest is
	# the points entry, then it sets count_list[l_p] to the prevailing counter value
	# and then calls itself with l_p+1 (unless we're at the end..)
	# likewise for starts and ends -- they affect the counter increment/decrement
	if l_p > r_p or l_e > r_e :
		return		# because you have already initialized all points to zero, nothing left to process if you see the last end point..
	
	if l_s > r_s : # we've been through all start points..
		s_ptr = r_s
	else :
		s_ptr = l_s
	
	p_count = 1		# this is spaghetti to handle multiple identical points
	
	# that is, if all three coincide, or, the point is left-most of the three candidates (queued up start/end points)
	if (points[l_p] == starts[s_ptr] == ends[l_e]) :
		count_list[l_p] = counter+1
		traverse( starts, l_s, r_s, ends, l_e, r_e, points, l_p+1, r_p, counter, count_list)
		return
	elif (points[l_p] < starts[s_ptr] and points[l_p] < ends[l_e]) :
		count_list[l_p] = counter
		traverse( starts, l_s, r_s, ends, l_e, r_e, points, l_p+1, r_p, counter, count_list)
		return
	
	if l_s <= r_s :		# then, process start point
		if starts[l_s] == ends[l_e] :	# we have already taken care of the case of point being the left-most..
			traverse( starts, l_s+1, r_s, ends, l_e+1, r_e, points, l_p, r_p, counter, count_list )
		elif starts[l_s ] <= points[l_p] and starts[l_s] < ends[l_e] :
			traverse( starts, l_s+1, r_s, ends, l_e, r_e, points, l_p, r_p, counter+1, count_list )
		elif ends[l_e] <= points[l_p] and ends[l_e] < starts[l_s] :
			if ends[l_e] == points[l_p] :
				count_list[l_p] = counter
				while l_p + p_count <= r_p and ends[l_e] == points[l_p + p_count] :
					count_list[l_p+p_count] = counter
					p_count += 1
				traverse( starts, l_s, r_s, ends, l_e+1, r_e, points, l_p+p_count, r_p, counter-1, count_list )
			else :
				traverse( starts, l_s, r_s, ends, l_e+1, r_e, points, l_p, r_p, counter-1, count_list )
		return
	else :		# always ignore the start point..
		if ends[l_e] < points[l_p] :
			traverse( starts, l_s, r_s, ends, l_e+1, r_e, points, l_p, r_p, counter-1, count_list )
		else :
			count_list[l_p] = counter
			traverse( starts, l_s, r_s, ends, l_e, r_e, points, l_p+1, r_p, counter, count_list )
		return
		
	
def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:	# O( n * p )
                cnt[i] += 1
    return cnt

def partition3(a, l, r):
    #write your code here
	# ( [list of nums] , int, int) --> ( int, int )
	# ( [list of nums] , index of left-most element in range to process, index of right-most ) -->
	#						( index of right-most element in "less than" group 
	# 							, index of left-most element in "greater than" group 
	
	if l == r :		# should not ever see this..
		return (l,r)
		
	x = a[l]
	m1 = l
	m2 = l
	for i in range( l+1 , r+1) :
		if a[i] < x :
			m1 += 1
			m2 += 1
			a[m2] , a[i] = a[i] , a[m2]
			# now, if m2 > m1, then, you also have to do another swap ( look at 6 22 9 1 3 4 6 3 6 )
			if m2 > m1 :
#				a[m2 - 1 ] , a[m2] = a[m2] , x
				a[m1] , a[m2] = a[m2], x	# after implementing testing
		elif a[i] == x :
			m2 += 1
			a[m2] , a[i] = x , a[m2]
	
	a[l] , a[m1] = a[m1] , x

	return ( m1 , m2 )	
			

def randomized_quick_sort(a, l, r):
    # list of ints , index of left-most, index of right-most --> nothing, side effect : a sorted
    if l >= r:
        return
    # k = random.randint(l, r)
    # a[l], a[k] = a[k], a[l]
    #use partition3
    (m1, m2 ) = partition3( a , l , r )
    
    # m = partition2(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);
    # randomized_quick_sort(a, l, m - 1);
    # randomized_quick_sort(a, m + 1, r);

def binary_search(a, left, right, x):
	#pdb.set_trace()
	# left, right = 0, len(a)	# this tripped me up early on..
	# write your code here
	# ( [list of numbers ] , index of left-most, num of elems, one number ) --> integer
	# ( [sorted list of numbers ] , index of left-most, num of elems , one number )
	#									--> index of the number x in a, if exists in a, else -1
#	b = len(a) + 1	# just to see what this does to the execution time
# interstingly, that didn't kill it - 3.39 --> 3.92 - so length computation doesn't kill
#	b = a[0:]	# also a test - to see what impact this has -- ans - completely killed it - blew up time
	if x < a[left] or x > a[right-1] :
		return -1
	else :
		if left + 1 == right :
			if x == a[left] :
				return left
			else :
				return -1
		mid = (left + right) >> 1
		if x == a[ mid ] :
			return mid
		else :
			if x > a[mid] :
				return binary_search( a , mid + 1, right , x )
			else :
				return binary_search( a , 0 , mid , x )
	
	
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    pdb.set_trace()
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')



# cheating off a web solution skeleton - make one list of all points and traverse it
# the recursion is only in the sorting of the lists :( not sure if that's what is called for..