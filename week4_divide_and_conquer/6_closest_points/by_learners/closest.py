#Uses python3
import sys
import math
import pdb

# beware of copying lists - that's very expensive time-wise
def minimum_distance(x, y):
	# ( list of ints, list of ints ) --> float
	#write your code here
	# this one is just a facade - we call our real thing from this one..
	n = len(x)
	xy = sorted( zip( x, y) )
	x,y = map( list, zip(*xy) )	# now, both sorted, according to x
	y1x1 = sorted( zip( y, x ) )
	y1, x1 = map( list, zip( *y1x1) )
	return fast_min_dist( x, y, 0, n-1, x1, y1, n)
	
def fast_min_dist( x, y, l, r, x1, y1 , n ) :		# pass n so you don't have to compute it each time..
	# (list of ints, list of ints, int, int, list of ints, list of ints, int ) --> float
	# points sorted by x-coord, index of left-most, index of rightmost, points sorted by y-coord, num points --> min distance
	if r == l :
		return 1e18		# infinity
	if r == l + 1 :
		return ( ( x[l] - x[r] )**2 + (y[l] - y[r])**2 )**0.5
	else :
		mid = (l+r) >> 1	# right-shift = divide by 2
		d1 = fast_min_dist( x,y,l,mid,x1,y1 , n)		# S1
		d2 = fast_min_dist( x,y,mid+1,r,x1,y1 , n)	# S2 
		d = min( d1, d2 )
		d_p = d
		x_div = ( x[mid]  + x[mid+1] ) >> 1
		# now for the little business of figuring out whether there are any offenders -
		# that is, pairs of points, one in each of S1 and S2 which are closer than d..
		# you navigate ALL (don't know a way around this) points using the ones sorted by y-coord
		# for each point, you process 7 points or until you find one on the other side that has del y > d
		# a point qualifies for comparison (or reference) if it is within d of the mid line's x-coord
		# you also discard a point from comparison if it's on the same side of the line. So,
		for i in range( n-1 ) : # no need to process that last one because every other point processes it
			if x1[i] - x_div > d :
				continue
			else :
				for j in range( i+1, min(i+7,n) ) :
					if abs(y1[j] - y1[i]) > d  or abs(x1[j] - x1[i]) > d :
						break
					else :
						dist = ( (x1[i] - x1[j])**2 + (y1[i] - y1[j])**2 )**0.5
						if dist < d :
							d = dist
				
		return d

def naive_min_dist( x , y ) :
	n = len(x )
	dist = 1e11		# infinity
	for i in range( n-1 ) :
		for j in range( i+1, n ) :
			dist_i = ( (x[i] - x[j])**2 + (y[i] - y[j])**2 )**0.5
			if dist > dist_i :
				dist = dist_i
	return dist
		
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]		# list of the x-coordinates -- any order => unsorted
    y = data[2::2]		# list of the y-coordinates
    #pdb.set_trace()
    print("{0:.9f}".format(minimum_distance(x, y)))
    #print("{0:.9f}".format(naive_min_dist(x, y)))


# seems to me like we need a new sorting algorithm that takes two lists
# one is the master, one is the slave. It sorts the master and the slave
# elements just follow. How easy?
	
# exercise break answer : if you had more than 4 points in a square, then
# you would have two points that are closer than d

# the way, the truth and the life :
# sort the points by x-coordinates and also by y-coordinates
# So, you end up with x, y - which are the sorted originals - sorted by x
# and, x1, y1 - which are the originals, sorted according to y
# the latter are useful for the sliver processing..