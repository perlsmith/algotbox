#Uses python3
import sys
import pdb

def lcs2(a, b):
	#write your code here
	# ( list, list ) --> int
	n = len( a )
	m = len( b )
	D = [ list( map( lambda x : [x,0] , range( m + 1 ) ) ) ]

	for i in range(1, n + 1) :
		D.append( [[i,0]] + [[0,0]] * m )
	
	for j in range( 1,m+1 ) :
		for i in range( 1, n+1 ) : 
			ins = D[ i ][ j-1 ][0] + 1
			deletion = D[ i - 1][ j ][0] + 1
			match = D[ i-1 ][ j-1 ][0]
			mismatch = 2 + D[ i-1 ][ j-1 ][0]
			if a[i-1] == b[j-1] :
				if ins == min( ins, deletion, match ) :
					D[i][j] = [ins, D[i][j-1][1] ]
				elif deletion == min( ins, deletion, match ) :
					D[i][j] = [ deletion , D[i-1][j][1] ]
				else :
					D[i][j] = [ match , 1 + D[i-1][j-1][1] ]
			else :
				if ins == min( ins, deletion, mismatch ) :
					D[i][j] = [ins, D[i][j-1][1] ]
				elif deletion == min( ins, deletion, mismatch ) :
					D[i][j] = [ deletion , D[i-1][j][1] ]
				else :
					D[i][j] = [ mismatch , D[i-1][j-1][1] ]
	
	return D[n][m][1]

def pp_matrix( matrix ) :
	# matrix --> printed
	s = [[str(e) for e in row] for row in matrix]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print( '\n'.join(table) )

	
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    #pdb.set_trace()
    print(lcs2(a, b))

# per the lecture, LCS is nothing but the alignment score with mu = sigma = 0
# that is, there is no penalty for insertions and deletions and mismatches..

# or, you can just keep track of the matches.. 
# so, for each entry in the D matrix, instead of an int, you also record
# an M where that is the number of matches..