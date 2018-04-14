# Uses python3
import sys
from collections import namedtuple
# import pdb

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
	# ( set of pairs of integers ) -> list of integers # really a set, because they will be unique
	# [ (4,7), (1,3) , (2, 5) , (5,6) ] --> [3,6]
#    pdb.set_trace()
	points = {}
	#write your code here
	for s in segments:
		if s.end in points :
			points[s.end].append( s.start )
		else :
			points[s.end] = [s.start]

	return r_points( points )

def r_points( points ) :
#	pdb.set_trace()
	# ( dict{ r-point : [ list of l-point] } -> list of optimal r-points
	if not points :
		return []
	r = min( points.keys() )	# get the left-most right-point
	reduced_points = {}
	for r_point in points.keys() :
		for l_point in points[r_point] :		# confusing, but points.r_point is a list of l-points..
			if l_point > r :
				if r_point in reduced_points :
					reduced_points[ r_point ].append( l_point )
				else :
					reduced_points[ r_point ] = [l_point]
		
	return [ r ] + r_points( reduced_points )
		

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

# math formulation - given already - segments, and minimize the number of points chosen
# such that each segment has a designated points

# algorithm :  (greedy)
# arranged the right-most points of all segments from left to right (ascending)
# then, for each point, add that point to the result and eliminate all segments that touch this point
# repeat with the list that's left

# we use a function that takes a dict and calls itself recursively
# the dict contains the r-points of the segments and the values are the l-points
# it takes the min of the keys and then loops over the list building up a new dict
# that contains all items whose l-points are > the r-point being considered.
# it then calls itself with the new dict and returns the list that is the r-point just
# processed and the list returned by the recursive call

# did not : write tests prior to coding.. :(