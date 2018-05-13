# Uses python3
import pdb

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax( i, j, m, M , ops) :
	# (int, int ) --> ( int, int )
	Min = 1e18
	Max = -1e18	# -inf essentially :)
	if i == j :
		return (m[i][i], M[i][i] )
	elif j == i + 1 :
		result = evalt( m[i][i], m[j][j], ops[i] )
		return (result, result )
	else :
		for k in range( i, j ) :
			a = evalt( M[i][k], M[k+1][j], ops[k] ) # max, max
			b = evalt( M[i][k], m[k+1][j], ops[k] ) # max, min
			c = evalt( m[i][k], M[k+1][j], ops[k] ) # min, max
			d = evalt( m[i][k], m[k+1][j], ops[k] ) # min, min
			Min = min( Min, a, b, c, d)
			Max = max(Max, a, b, c, d )
	return ( Min, Max )

	
def get_maximum_value(dataset):
    #write your code here
	digits = list( map( int, dataset[::2] ) )
	ops = dataset[1::2]
	n = len( digits )
	m = []
	M = []
	for i in range( n ) :
		m.append( [0] * i + [digits[i]] + [0] * ( n - i - 1 ) )
		M.append( [0] * i + [digits[i]] + [0] * ( n - i - 1 ) )
	for s in range( n-1 ) :
		for i in range( n-1 - s ) :
			j = i + s + 1		# this is essentially translating the pseudocode... the poor guys don't count like hackers :(
			m[i][j], M[i][j] = MinAndMax( i, j, m, M, ops )
	return M[0][n-1]


if __name__ == "__main__":
    #pdb.set_trace()
    print(get_maximum_value( list(input() ) ))


# future work : can you add a switch so someone can easily get the minimum value
# if they want?

# can you support the division operator?

# dump out the expression with the parantheses added? (reconstruction)